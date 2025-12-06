import os
import sys
import pytest
# Add the project root (one level above this file) to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from app.database import init_db


@pytest.fixture(scope="session", autouse=True)
def init_test_db():
    init_db()
