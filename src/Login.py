import requests
from FormeAPITest.src import Requests
import configparser
import logging as logger


def PortalSignIn(url, header, payload):
    response = Requests.PostRequest(url, header, payload)
    data = response.json()
    token = data['token']
    logger.info('TOKEN : {}'.format(token))
    WriteTokenToConfig(token)
    return response

def ValidateResponse(response, email):
    data = response.json()
    #assert data['user']['id'] == "auth0"
    assert data['user']['email'] == email, "Email ID of the user is wrong"
    assert len(data['user']['first_name']) > 0, "Null first_name field in User body response"
    assert len(data['user']['last_name']) > 0, "Null last_name field in User body response"
    assert data['user']['gender'] == 0 or data['user']['gender'] == 1, "Gender value is neither 0 nor 1"
    assert data['user']['height'] > 1, "Height value is less than 1"
    assert data['user']['weight'] > 1, "Weight value is less than 1"
    assert data['user']['image'] == '', "Image value is not null"
    return 0

def LoginAsStudio(device_id):
    pass

def WriteTokenToConfig(token):
    config = configparser.ConfigParser()
    config_file_path = '/Users/uday/PycharmProjects/pythonProject1/FormeAPITest/utils/config.ini'
    config.read(config_file_path)
    if not config['Bearer_token']:
        config.add_section('Bearer_token')
    config.set('Bearer_token', 'token', token)
    with open(config_file_path, 'w') as configfile:  # save
        config.write(configfile)



