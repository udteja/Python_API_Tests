import logging as logger
import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store")
    logger.info("Added --env as command line argument")


@pytest.fixture
def env(request):
    logger.info("Getting Environment to Test")
    return request.config.getoption("--env")








'''
def test_env(getEnv):
    assert getEnv == 'Beta'
'''
