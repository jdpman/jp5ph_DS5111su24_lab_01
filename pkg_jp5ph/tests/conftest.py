# tests/conftest.py

import pytest

#Register custom markers

def pytest_configure(config):
    config.addinivalue_line(
            "markers", "integration: mark test as integration test"
            )
