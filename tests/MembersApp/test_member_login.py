import requests
import json
import pytest
import logging as logger

from FormeAPITest.src import Login
from FormeAPITest.src import Generator
from FormeAPITest.tests.MembersApp.Init_Test import Initialize
from FormeAPITest.utils import Readconfig
from FormeAPITest.src import *
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
def test_successful_login():
    logger.info('TEST: Verify successful login with existing email and password credentials')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 201


@pytest.mark.regression
def test_failed_login_no_pwd():
    logger.info('TEST: Verify failed login with email credential but no password')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 400


@pytest.mark.regression
def test_failed_login_no_email():
    logger.info('TEST: Verify failed login with password credential but no email')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    assert response.status_code == 400


@pytest.mark.data
def test_successful_login_response_header():
    logger.info('TEST: Verify response headers for successful login')
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)

    response = Login.PortalSignIn(url, headers, payload)
    validated_result = Login.ValidateResponse(response, email)
    assert validated_result == 0


@pytest.mark.stress
def test_login_stress_same_user():
    logger.info('TEST: Verify successful login in stress scenario with same user')
    count = 1
    failed_response = 0
    url = Generator.GenerateUrl('login', base_url)
    payload_dict = {"email": email, "password": password}
    payload = Generator.GenerateLoginPayload(payload_dict)
    headers = Generator.GenerateLoginHeaders(contentType)
    response_code_dict = {}
    while count <= 100:
        logger.info('Request : {}'.format(count))
        response = Login.PortalSignIn(url, headers, payload)
        if response.status_code != 201:
            if response.status_code not in response_code_dict:
                response_code_dict[response.status_code] = 1
            else:
                response_code_dict[response.status_code] += 1
            failed_response += 1
            logger.info('Failed Response : {}'.format(failed_response))
            logger.info('Failed Response Code : {}'.format(response.status_code))
        count += 1
    for items in response_code_dict:
        print(items)
    assert failed_response == 0, "Received {} Failed Responses".format(failed_response)
