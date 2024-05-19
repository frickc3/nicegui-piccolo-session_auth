import os
import pytest
import sys
from dotenv import load_dotenv, find_dotenv
from fastapi.testclient import TestClient

sys.path.append('..\\')
print(sys.path)
from main import fapp

@pytest.fixture(scope='session', autouse=True)
def load_env():
    env_file = find_dotenv('.env.test')
    load_dotenv(env_file)

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(fapp)
    yield client
