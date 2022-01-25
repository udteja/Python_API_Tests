from FormeAPITest.utils import Readconfig
from FormeAPITest import src
from FormeAPITest.src import Login
from FormeAPITest.src import Generator
from FormeAPITest.src import Response
from FormeAPITest.src import Requests
from FormeAPITest.utils import Readconfig
import logging as logger
import pytest

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

@pytest.mark.members_app_e2e
def test_successful_login():
    logger.info('TEST: Verify successful login with existing email and password credentials')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 201

@pytest.mark.members_app_e2e
def test_browse_workouts():
    logger.info('TEST: Verify workouts filter')
    url = Generator.GenerateUrl('workout_filter', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    response = Requests.GetRequest(url, headers)
    validated_result = Response.ValidateWorkoutFilter(response)
    assert validated_result == 0


