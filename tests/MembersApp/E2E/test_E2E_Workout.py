from FormeAPITest.utils import Readconfig
from FormeAPITest import src
from FormeAPITest.src import Login, Workout
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
workout_list_dict = {}


def setup_module(module):
    global base_url
    global email
    global password
    global contentType
    base_url, email, password = Readconfig.GetTestData()
    contentType = Readconfig.GetLoginContentType()


@pytest.mark.members_app_e2e_workout
def test_successful_login():
    logger.info('TEST: Validate Successful Login with Existing User')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)
    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 201


@pytest.mark.members_app_e2e_workout
def test_get_workout_sessions_list():
    global workout_list_dict
    logger.info('TEST: Validate API Response for WorkOut Sessions List')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    response = Requests.GetRequest(url, headers)
    workout_list_dict = Workout.GetWorkoutList(response)
    validated_result = Response.ValidateWorkoutSessions(response)
    assert validated_result == 0


@pytest.mark.members_app_e2e_workout
def test_get_workout_sessions_completed_list():
    logger.info('TEST: Get Completed WorkOut Sessions List')
    url = Generator.GenerateUrl('completed-workouts', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    response = Requests.GetRequest(url, headers)
    validated_result = Response.ValidateCompletedWorkoutSessions(response, workout_list_dict)
    assert validated_result == 0


@pytest.mark.members_app_e2e_workout
def test_get_workout_list_by_status():
    logger.info('TEST: Get List of Workouts Based On Status')
    url = Generator.GenerateUrl('workout-session', base_url)
    token = Readconfig.ReadUserToken()
    auth = 'Bearer '
    authentication = auth + str(token)
    headers = Generator.GenerateAuthorizationHeader(authentication)
    for status in status_list:
        response = Requests.GetRequest(url, headers)
        temp_dict = Workout.GetWorkoutListByStatus(response, status)
        logger.info("List of Workouts Based On '{}': {}".format(status, temp_dict))
        assert len(temp_dict) <= len(workout_list_dict)

@pytest.mark.members_app_e2e_workout
def test_get_workout_list_count_by_status():
    logger.info('TEST: Get Count of Workouts Based On Status')
    for status in status_list:
        count = Workout.GetWorkoutListCountByStatus(status)
        logger.info("Count of Workouts Based On '{}': {}".format(status, count))
        assert count <= len(workout_list_dict)