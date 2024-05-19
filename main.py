import os
import argparse
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from icecream import install, ic
from nicegui import APIRouter, app, ui

from piccolo_admin.endpoints import create_admin
from piccolo_api.csrf.middleware import CSRFMiddleware
from session_auth.endpoints import session_login, session_logout
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase
from starlette.middleware.authentication import AuthenticationMiddleware

from app.piccolo_app import APP_CONFIG

fapp = FastAPI()

router = APIRouter(prefix='')

fapp.add_middleware(
            AuthenticationMiddleware,
                backend=SessionsAuthBackend(
                    admin_only=False,
                    allow_unauthenticated=True,
                    increase_expiry=datetime.timedelta(minutes=30)
                ),
        )

"""
#
# This middleware sometimes causes issues when using Chrome.
#
fapp.add_middleware(
        # CSRF middleware provides additional protection for older browsers, as
        # we're using cookies.
            CSRFMiddleware,allow_form_param=True,
        )
"""

fapp.mount('/admin/',
            create_admin(
                    tables=APP_CONFIG.table_classes,
            ),
        )

fapp.mount(
        path="/login/",
        app=session_login(
            session_table=SessionsBase,
            redirect_to=None,
            ),
        )

fapp.add_route(
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
def base(request: Request):
    ic()
    ic(request.url)
    if request.user.user == None:
        return RedirectResponse('/login/?nextURL=/base')
    ui.label('Base page - authenticated required!')
    ui.label('You are logged in as user: %s ' % request.user.username)
    with ui.row():
        ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
        ui.button('sub_page', on_click=lambda: ui.navigate.to('/sub_page'))

@router.page('/sub_page')
def sub_page(request: Request):
    ic()
    if request.user.user == None:
        return RedirectResponse('/login/?nextURL=/sub_page')
    ui.label('sub page - authenticated required!')
    ui.label('You are logged in as user: %s ' % request.user.username)
    with ui.row():
        ui.button('Logout', on_click=lambda: ui.navigate.to('/logout/'))
        ui.button('base page', on_click=lambda: ui.navigate.to('/base'))    

fapp.include_router(router)

ui.run_with(fapp,
        storage_secret=os.getenv('STORAGE_SECRET'),
    )


if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--port", help="http Port",
                         default=8080, action="store")

    parser.add_argument("-v", "--verbose", help="Print detailed debugging information.",
                        action="store_true")

    parser.add_argument("-r", "--reload", help="Reload on changes, default False.",
                        action="store_true", default=False)

    parser.add_argument("-d", "--debug", help="Print debugging information.",
                        action="store_true", default=False)

    args = parser.parse_args()
    log_level = "info"
    if args.verbose:
        log_level = "debug"
    port = int(args.port)

    #  Used for printing debug information
    install()
    ic.disable()

    if args.debug:
        ic.enable()
        os.environ['IC_DEBUG'] = 'True'
    ic(args)

    uvicorn.run("main:fapp", host="127.0.0.1", port=port, reload=args.reload,
                log_level=log_level)