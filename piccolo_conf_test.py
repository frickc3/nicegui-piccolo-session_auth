import os
from dotenv import load_dotenv, find_dotenv
from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine

DB = SQLiteEngine(path="session_auth.db")

# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=[
                "piccolo_admin.piccolo_app",
])
