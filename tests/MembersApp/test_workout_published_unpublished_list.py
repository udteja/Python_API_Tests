from FormeAPITest.utils import Readconfig
from FormeAPITest import src
from FormeAPITest.src import Login
from FormeAPITest.src import Generator
from FormeAPITest.src import Response
from FormeAPITest.src import Requests
from FormeAPITest.utils import Readconfig
import logging as logger
import pytest
import json

base_url = None
email = None
password = None
contentType = None
loginObj = None
category_list = ["Strength", "Barry's", "Barre", "Dance", "Mind", "Pilates", "Recovery", "Specialty", "Yoga",
                 "Instructors"]
complexity_list = ["Beginner", "Intermediate", "Advanced"]
session_type_list = ["Planned Session", "Video on Demand"]
status_list = ["published", "unpublished"]
workout_dict_by_status = {}

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
def test_workout_sessions_list():
    logger.info('TEST: Verify WorkOut Sessions List')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    response = Requests.GetRequest(url, headers)
    validated_result = Response.ValidateWorkoutSessions(response)
    assert validated_result == 0

@pytest.mark.members_app_e2e
def test_workout_sessions_by_status():
    logger.info('TEST: Verify WorkOut Session by Status')
    global workout_session_dict
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    status = 'published'
    temp_dict['status'] = status
    parameter = temp_dict
    response = Requests.GetRequest(url, headers, parameter)
    for items in json.loads(response.text):
        for fields in items:
            if fields == 'status' and fields['status'] == 'published':
                workout_session_dict[fields['id']] = 'published'
            elif fields == 'status' and fields['status'] == 'unpublished':
                workout_session_dict[fields['id']] = 'unpublished'
    validated_result = Response.ValidateWorkoutSessionsByStatus(response, status)
    assert validated_result == 0

@pytest.mark.members_app_e2e
def test_workout_sessions_by_published_status():
    logger.info('TEST: Get all workouts with Published Status')
    count = 0
    for items in workout_dict_by_status:
        if workout_dict_by_status[items] == "published":
            count += 1

