import pytest
import logging as logger
from FormeAPITest.src import Login
from FormeAPITest.src import Generator
from FormeAPITest.utils import Readconfig

base_url = None
email = None
password = None
contentType = None
loginObj = None


def setup_module(module):
    global base_url
    global email
    global password
    global contentType
    base_url, email, password = Readconfig.GetTestData()
    contentType = Readconfig.GetLoginContentType()


@pytest.mark.smoke
def test_studio_successful_login():
    logger.info('TEST: Verify successful login with existing email and password credentials')
    url = Generator.GenerateUrl('studio_login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 201
