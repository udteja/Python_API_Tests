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
category_list = ["Strength", "Barry's", "Barre", "Dance", "Mind", "Pilates", "Recovery", "Specialty", "Yoga",
                 "Instructors"]
complexity_list = ["Beginner", "Intermediate", "Advanced"]
session_type_list = ["Planned Session", "Video on Demand"]
status_list = ["published", "unpublished"]


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
def test_workout_sessions_by_category():
    logger.info('TEST: Verify WorkOut Session by Category')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for category in category_list:
        if category != "Instructors":
            temp_dict['category'] = category
            parameter = temp_dict
            response = Requests.GetRequest(url, headers, parameter)
            validated_result = Response.ValidateWorkoutSessionsByCategory(response, category)
            assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_complexity():
    logger.info('TEST: Verify WorkOut Session by Complexity')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for complexity in complexity_list:
        temp_dict['complexity'] = complexity
        parameter = temp_dict
        response = Requests.GetRequest(url, headers, parameter)
        validated_result = Response.ValidateWorkoutSessionsByComplexity(response, complexity)
        assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_session_type():
    logger.info('TEST: Verify WorkOut Session by Session Type')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for session in session_type_list:
        temp_dict['session_type'] = session
        parameter = temp_dict
        response = Requests.GetRequest(url, headers, parameter)
        validated_result = Response.ValidateWorkoutSessionsBySessionType(response, session)
        assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_status():
    logger.info('TEST: Verify WorkOut Session by Status')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for status in status_list:
        temp_dict['status'] = status
        parameter = temp_dict
        response = Requests.GetRequest(url, headers, parameter)
        validated_result = Response.ValidateWorkoutSessionsByStatus(response, status)
        assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_category_and_complexity():
    logger.info('TEST: Verify WorkOut Session by Category and Complexity')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for category in category_list:
        if category != "Instructors":
            for complexity in complexity_list:
                temp_dict['category'] = category
                temp_dict['complexity'] = complexity
                parameter = temp_dict
                response = Requests.GetRequest(url, headers, parameter)
                validated_result = Response.ValidateWorkoutSessionsByCategoryAndComplexity(response, category,
                                                                                           complexity)
                assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_category_and_session_type():
    logger.info('TEST: Verify WorkOut Session by Category and Session Type')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for category in category_list:
        if category != "Instructors":
            for session in session_type_list:
                temp_dict['category'] = category
                temp_dict['session_type'] = session
                parameter = temp_dict
                response = Requests.GetRequest(url, headers, parameter)
                validated_result = Response.ValidateWorkoutSessionsByCategoryAndSessionType(response, category, session)
                assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_complexity_and_session_type():
    logger.info('TEST: Verify WorkOut Session by Complexity and Session Type')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for complexity in complexity_list:
        for session in session_type_list:
            temp_dict['complexity'] = complexity
            temp_dict['session_type'] = session
            parameter = temp_dict
            response = Requests.GetRequest(url, headers, parameter)
            validated_result = Response.ValidateWorkoutSessionsByComplexityAndSessionType(response, complexity, session)
            assert validated_result == 0


@pytest.mark.members_app_e2e
def test_workout_sessions_by_all_test_filters():
    logger.info('TEST: Verify WorkOut Session by Category, Complexity, Session Type and Status')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    temp_dict = {}
    for category in category_list:
        if category != "Instructors":
            for complexity in complexity_list:
                for session in session_type_list:
                    for status in status_list:
                        temp_dict['category'] = category
                        temp_dict['complexity'] = complexity
                        temp_dict['session_type'] = session
                        temp_dict['status'] = status
                        parameter = temp_dict
                        response = Requests.GetRequest(url, headers, parameter)
                        validated_result = Response.ValidateWorkoutSessionsByAllTestFilters(response, category,
                                                                                            complexity, session, status)
                        assert validated_result == 0
