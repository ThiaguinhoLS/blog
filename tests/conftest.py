# -*- coding: utf-8 -*-
from app import app, db
import pytest

@pytest.fixture
def client():
    return app.test_client()

