import json
from FormeAPITest.utils import Readconfig
import logging as logger

url_dict = {
    'login': '/v1/login',
    'studio_login': '/v1/login?device_id=',
    'workout_filter': '/v1/workout-filter',
    'workout-session': '/v1/workout-session',
    'completed-workouts': '/v1/user/me/completed-workouts'
}


def GenerateLoginPayload(payload_dict):
    logger.info("Generating Payload for Login Tests......")
    generated_payload = json.dumps(payload_dict)
    return generated_payload


def GenerateLoginHeaders(contentType):
    logger.info("Generating Headers for Login Tests......")
    headers = {
        'Content-Type': contentType
    }
    return headers


def GenerateUrl(key, base_url):
    logger.info("Generating URL Tests......")
    if key == 'studio_login':
        device_id = Readconfig.ReadStudioDeviceId()
        generated_url = base_url + url_dict[key] + device_id
    else:
        generated_url = base_url + url_dict[key]

    return generated_url

def GenerateAuthorizationHeader(authorization):
    logger.info("Generating Headers for Browse Workouts Tests......")
    headers = {
        'Authorization': authorization
    }
    return headers
