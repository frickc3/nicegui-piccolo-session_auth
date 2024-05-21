import os
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from icecream import install, ic
from nicegui import APIRouter, ui

from piccolo_admin.endpoints import create_admin
from piccolo_api.csrf.middleware import CSRFMiddleware
from session_auth.endpoints import session_login, session_logout
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase
from starlette.middleware.authentication import AuthenticationMiddleware

from app.piccolo_app import APP_CONFIG

app = FastAPI()

install()
ic.disable()                        # comment this out for debugging

router = APIRouter(prefix='')

app.add_middleware(
            AuthenticationMiddleware,
                backend=SessionsAuthBackend(
                    admin_only=False,
                    allow_unauthenticated=True,
                    increase_expiry=datetime.timedelta(minutes=30)
                ),
        )

app.add_middleware(
        # CSRF middleware provides additional protection for older browsers, as
        # we're using cookies.
            CSRFMiddleware,allow_form_param=True,
        )


app.mount('/admin/',
            create_admin(
                    tables=APP_CONFIG.table_classes,
            ),
        )

app.mount(
        path="/login/",
        app=session_login(
            session_table=SessionsBase,
            redirect_to=None,
            ),
        )

app.add_route(
            path="/logout/",
            route=session_logout(session_table=SessionsBase,
                                redirect_to='/'),
            methods=["GET","POST"],
        )

@ui.page('/')
def root(request: Request):
    ic()
    ui.label('Root Page - no authorization required')
    if request.user.user:
        ui.label('You are logged in as user: %s ' % request.user.username)
    with ui.row():
        if request.user.user:
            ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
        ui.button('base page', on_click=lambda: ui.navigate.to('/base'))   
        ui.button('sub page', on_click=lambda: ui.navigate.to('/sub_page'))   


@router.page('/base')
async def base(request: Request):
    ic()
    if request.user.user == None:
        return RedirectResponse('/login/?nextURL=/base')
    ui.label('Base page - authenticated required!')
    ui.label('You are logged in as user: %s ' % request.user.username)
    with ui.row():
        ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
        ui.button('sub_page', on_click=lambda: ui.navigate.to('/sub_page'))

@router.page('/sub_page')
async def sub_page(request: Request):
    ic()
    if request.user.user == None:
        return RedirectResponse('/login/?nextURL=/sub_page')
    ui.label('sub page - authenticated required!')
    ui.label('You are logged in as user: %s ' % request.user.username)
    with ui.row():
        ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
        ui.button('base page', on_click=lambda: ui.navigate.to('/base'))    

app.include_router(router)

ui.run_with(app,
        storage_secret=os.getenv('STORAGE_SECRET'),
    )
