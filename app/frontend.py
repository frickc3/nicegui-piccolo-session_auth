import os
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from icecream import install, ic
import httpx
from nicegui import APIRouter, app, ui

from piccolo_admin.endpoints import create_admin
from piccolo_api.csrf.middleware import CSRFMiddleware
from session_auth.endpoints import session_login, session_logout
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase
from starlette.middleware.authentication import AuthenticationMiddleware

from app.piccolo_app import APP_CONFIG
from app.tables import *

def init(fastapi_app: FastAPI) -> None:

    router = APIRouter(prefix='')

    fastapi_app.add_middleware(
                AuthenticationMiddleware,
                    backend=SessionsAuthBackend(
                        admin_only=False,
                        allow_unauthenticated=True,
                        increase_expiry=datetime.timedelta(minutes=30)
                    ),
            )
    fastapi_app.add_middleware(
            # CSRF middleware provides additional protection for older browsers, as
            # we're using cookies.
                CSRFMiddleware,allow_form_param=True,
            )

    fastapi_app.mount('/admin/',
                create_admin(
                        tables=APP_CONFIG.table_classes,
                ),
            )

    fastapi_app.mount(
            path="/login/",
            app=session_login(
                session_table=SessionsBase,
                redirect_to='/',
                ),
            )

    fastapi_app.add_route(
                path="/logout/",
                route=session_logout(session_table=SessionsBase,
                                    redirect_to='/'),
                methods=["POST"],
            )

    @ui.page('/')
    def base(request: Request):
        ic()
        ui.label('Base Page - no authorization required')
        if request.user.user:
            ui.label('You are logged in as %s ' % request.user.username)
        with ui.row():
            if request.user.user:
                ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
            ui.button('root page', on_click=lambda: ui.navigate.to('/root'))   
            ui.button('sub page', on_click=lambda: ui.navigate.to('/sub_page'))   


    @router.page('/root')
    def root(request: Request):
        ic()
        ic(request.url)
        if request.user.user == None:
            return RedirectResponse('/login/?nextURL=/')
        ui.label('Root page')
        with ui.row():
            ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
            ui.button('sub_page', on_click=lambda: ui.navigate.to('/sub_page'))

    @router.page('/sub_page')
    def sub_page(request: Request):
        ic()
        if request.user.user == None:
            return RedirectResponse('/login/?nextURL=/sub_page')
        ui.label('sub page')
        with ui.row():
            ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
            ui.button('root page', on_click=lambda: ui.navigate.to('/root'))    

    fastapi_app.include_router(router)

    ui.run_with(fastapi_app,
            storage_secret=os.getenv('STORAGE_SECRET'),
        )

"""
ui.run(port=8080,
       show=False,
       reload=True,
       storage_secret=os.getenv('STORAGE_SECRET'),
       )
"""