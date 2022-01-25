import requests
from FormeAPITest.src import Requests
import configparser
import json

workout_dict = {}
workout_dict_by_status = {}
config = configparser.ConfigParser()
config_file_path = '/Users/uday/PycharmProjects/pythonProject1/FormeAPITest/utils/config.ini'
config.read(config_file_path)

'''
This method returns a dictionary of all the workouts with their id's as key and name as value
Return : workout_dict
'''


def GetWorkoutList(response):
    global workout_dict
    json_data = json.loads(response.text)
    for items in json_data:
        if items['id'] not in workout_dict:
            workout_dict[items['id']] = items['name']
        else:
            if workout_dict[items['id']] != items['name']:
                workout_dict[items['id']] = items['name']
    return workout_dict


'''
This method returns a dictionary of all the workouts with their id's and their status
Return : workout_dict_by_status
'''


def GetWorkoutListByStatus(response, status):
    global workout_dict_by_status
    json_data = json.loads(response.text)
    for items in json_data:
        if items['id'] == 'id':
            workout_dict_by_status[items['id']] = status
    return workout_dict_by_status


'''
This method returns a count of all the workouts with their status
Return : count
'''


def GetWorkoutListCountByStatus(status):
    count = 0
    for key in workout_dict_by_status:
        if workout_dict_by_status[key] == status:
            count += 1
    return count
