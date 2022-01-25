import configparser
import logging as logger
import pytest

# Read config.ini file
config = configparser.ConfigParser()
config_file_path = '/Users/uday/PycharmProjects/pythonProject1/FormeAPITest/utils/config.ini'
config.read(config_file_path)

@pytest.fixture(scope="session")
def WriteEnv(env):
    if not config['Env']:
        config.add_section('Env')
        if env == 'Beta':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)
        elif env == 'Develop':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)
        elif env == 'Production':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)
        else:
            logger.error("Not a valid Environment")
    else:
        if env == 'Beta':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)

        elif env == 'Develop':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)

        elif env == 'Production':
            config['Env']['current'] = env
            with open(config_file_path, 'w') as configfile:  # save
                config.write(configfile)

        else:
            logger.error("Not a valid Environment")


def GetTestData():
    current_env = config.get('Env', 'current')
    if current_env == 'Beta':
        logger.info("Environment used for Testing = {}".format(current_env))
        members_beta_url = config.get('Members_Beta_Env', 'loginurl')
        members_beta_email = config.get('Existing_User_Beta', 'email')
        members_beta_password = config.get('Existing_User_Beta', 'password')
        return members_beta_url, members_beta_email, members_beta_password
    elif current_env == 'Develop':
        logger.info("Environment used for Testing = {}".format(current_env))
        members_develop_url = config.get('Members_Develop_Env', 'loginurl')
        members_develop_email = config.get('Existing_User_Develop', 'email')
        members_develop_password = config.get('Existing_User_Develop', 'password')
        return members_develop_url, members_develop_email, members_develop_password
    elif current_env == 'Production':
        logger.info("Environment used for Testing = {}".format(current_env))
        members_production_url = config.get('Members_Develop_Env', 'loginurl')
        members_production_email = config.get('Existing_User_Develop', 'email')
        members_production_password = config.get('Existing_User_Develop', 'password')
        return members_production_url, members_production_email, members_production_password
    else:
        logger.error("Not a valid Environment")

def GetLoginContentType():
    logger.info("Fetching Content type from Config file....")
    content_type = config.get('Content_Type', 'content')
    return content_type

def ReadExistingUser():
    current_env = config.get('Env', 'current')
    if current_env  == "Beta":
        # Get the url from config file
        members_beta_email = config.get('Existing_User_Beta', 'email')
        return members_beta_email
    elif current_env  == "Develop":
        # Get the url from config file
        members_develop_email = config.get('Existing_User_Develop', 'email')
        return members_develop_email
    elif current_env == "Production":
        # Get the url from config file
        members_production_email = config.get('Existing_User_Develop', 'email')
        return members_production_email
    else:
        logger.error("Not a valid Environment")


def ReadExistingUserPassword(env):
    if globals()['env']  == "Beta":
        # Get the url from config file
        members_beta_password = config.get('Existing_User_Beta', 'password')
        return members_beta_password
    elif globals()['env']  == "Develop":
        # Get the url from config file
        members_develop_password= config.get('Existing_User_Develop', 'password')
        return members_develop_password
    elif globals()['env']  == "Production":
        # Get the url from config file
        members_production_password = config.get('Existing_User_Develop', 'password')
        return members_production_password
    else:
        logger.error("Not a valid Environment")

def ReadStudioDeviceId():
    id = config.get('Studio', 'device_id')
    return id

def ReadUserToken():
    token = config.get('Bearer_token','token')
    return token