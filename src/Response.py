import logging as logger
import json

category_list = ["Strength", "Barry's", "Barre", "Dance", "Mind", "Pilates", "Recovery", "Specialty", "Yoga",
                 "Instructors"]
complexity_list = ["Beginner", "Intermediate", "Advanced"]
category_dict = {}
complexity_dict = {}
workout_session_dict = {}


def ValidateWorkoutFilter(response):
    logger.info('Verify response headers for Workout Filter')
    json_data = json.loads(response.text)
    for items in json_data:
        # assert items['created_date'] <= items['updated_date'], "Updated Date is before Created Date"
        # assert items['id'] > 0, "Null id field in User body response"

        assert len(items['name']) > 0, "Null workout name field in body response"
        assert len(items['description']) > 0, "Null workout description field in body response. Item ID is {}".format(
            items['id'])
        assert items['condition']['category'] in category_list, "Category value is response is not part of Category " \
                                                                "List : {}".format(items['condition']['category'])
        assert items['order'] > 1, "Order value is less than 1"
    return 0


def ValidateWorkoutSessions(response):
    logger.info('Verify response headers for Workout Sessions')
    global workout_session_dict
    json_data = json.loads(response.text)
    for items in json_data:
        assert items['id'] > 0, "ID field is less than 0"
        for fields in items:
            if fields == 'id':
                workout_session_dict[items['id']] = {}
            elif fields == 'category':
                workout_session_dict[items['id']][fields] = items['category']
            elif fields == 'complexity':
                workout_session_dict[items['id']][fields] = items['complexity']
            elif fields == 'session_type':
                workout_session_dict[items['id']][fields] = items['session_type']
            elif fields == 'status':
                workout_session_dict[items['id']][fields] = items['status']
            else:
                pass
    logger.info(
        "Category, Complexity, Session Type and Status fields have been added to Workout Session Data Structure")

    return 0


def ValidateWorkoutSessionsByCategory(response, category):
    logger.info('Verify response headers for Workout Sessions by {}'.format(category))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['category'] == workout_session_dict[items['id']][
            'category'], "Category value is not in workout dictionary"
        assert items['category'] == category, "{} does not match {} from category list.".format(items['category'],
                                                                                                category)
        logger.info(
            "Workout ID:{} contains Category:'{}' in Workout Session Data Structure".format(items['id'],
                                                                                            items['category']))
        count += 1
    logger.info("Total fields with Category:'{}' = {}".format(category, count))
    return 0


def ValidateWorkoutSessionsByComplexity(response, complexity):
    logger.info('Verify response headers for Workout Sessions by {}'.format(complexity))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['complexity'] == workout_session_dict[items['id']][
            'complexity'], "complexity value is not in workout dictionary"
        assert items['complexity'] == complexity, "{} does not match {} from category list.".format(items['complexity'],
                                                                                                    complexity)
        logger.info(
            "Workout ID:{} contains Complexity:'{}' in Workout Session Data Structure.".format(items['id'],
                                                                                               items['complexity']))
        count += 1
    logger.info("Total fields with Complexity:'{}' = {}".format(complexity, count))
    return 0


def ValidateWorkoutSessionsBySessionType(response, session):
    logger.info('Verify response headers for Workout Sessions by {}'.format(session))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['session_type'] == workout_session_dict[items['id']][
            'session_type'], "Session typevalue is not in workout dictionary"
        assert items['session_type'] == session, "{} does not match {} from Session type list.".format(
            items['session_type'],
            session)
        logger.info(
            "Workout ID:{} contains Session_Type:'{}' in Workout Session Data Structure".format(items['id'],
                                                                                                items['session_type']))
        count += 1
    logger.info("Total fields with Session_Type:'{}' = {}".format(session, count))
    return 0


def ValidateWorkoutSessionsByStatus(response, status):
    logger.info('Verify response headers for Workout Sessions by {}'.format(status))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['status'] == workout_session_dict[items['id']][
            'status'], "Status value is not in workout dictionary"
        assert items['status'] == status, "{} does not match {} from Status list.".format(
            items['status'],
            status)
        logger.info(
            "Workout ID:{} contains Status:'{}' in Workout Session Data Structure".format(items['id'],
                                                                                          items['status']))
        count += 1
    logger.info("Total fields with Status:'{}' = {}".format(status, count))
    return 0


def ValidateWorkoutSessionsByCategoryAndComplexity(response, category, complexity):
    logger.info('Verify response headers for Workout Sessions by {} and {}'.format(category, complexity))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['category'] == workout_session_dict[items['id']][
            'category'] and items['complexity'] == workout_session_dict[items['id']][
                   'complexity'], "Category value and complexity value combo is not in workout dictionary"
        assert items['category'] == category, "{} does not match {} from category list.".format(items['category'],
                                                                                                category)
        assert items['complexity'] == complexity, "{} does not match {} from category list.".format(items['complexity'],
                                                                                                    complexity)
        logger.info(
            "Workout ID:{} contains both Category:'{} and Complexity:'{}'' in Workout Session Data Structure".format(
                items['id'],
                items['category'], items['complexity']))
        count += 1
    logger.info("Total fields with both Category:'{}' and Complexity:'{}' = {}".format(category, complexity, count))
    return 0


def ValidateWorkoutSessionsByCategoryAndSessionType(response, category, session):
    logger.info('Verify response headers for Workout Sessions by {} and {}'.format(category, session))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['category'] == workout_session_dict[items['id']][
            'category'] and items['session_type'] == workout_session_dict[items['id']][
                   'session_type'], "Category value and Session type value combo is not in workout dictionary"
        assert items['category'] == category, "{} does not match {} from category list.".format(items['category'],
                                                                                                category)
        assert items['session_type'] == session, "{} does not match {} from category list.".format(
            items['session_type'],
            session)
        logger.info(
            "Workout ID:{} contains both Category:'{} and Session Type:'{}'' in Workout Session Data Structure".format(
                items['id'],
                items['category'], items['session_type']))
        count += 1
    logger.info("Total fields with both Category:'{}' and Session Type:'{}' = {}".format(category, session, count))
    return 0


def ValidateWorkoutSessionsByComplexityAndSessionType(response, complexity, session):
    logger.info('Verify response headers for Workout Sessions by {} and {}'.format(complexity, session))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['complexity'] == workout_session_dict[items['id']][
            'complexity'] and items['session_type'] == workout_session_dict[items['id']][
                   'session_type'], "Complexity value and Session type value combo is not in workout dictionary"
        assert items['complexity'] == complexity, "{} does not match {} from category list.".format(items['complexity'],
                                                                                                    complexity)
        assert items['session_type'] == session, "{} does not match {} from category list.".format(
            items['session_type'],
            session)
        logger.info(
            "Workout ID:{} contains both Complexity:'{} and Session Type:'{}'' in Workout Session Data Structure".format(
                items['id'],
                items['complexity'], items['session_type']))
        count += 1
    logger.info("Total fields with both Complexity:'{}' and Session Type:'{}' = {}".format(complexity, session, count))
    return 0


def ValidateWorkoutSessionsByAllTestFilters(response, category, complexity, session, status):
    logger.info(
        'Verify response headers for Workout Sessions by {}, {}, {} and {}'.format(category, complexity, session,
                                                                                   status))
    json_data = json.loads(response.text)
    count = 0
    for items in json_data:
        assert items['category'] == workout_session_dict[items['id']][
            'category'] and items['complexity'] == workout_session_dict[items['id']][
                   'complexity'] and items['session_type'] == workout_session_dict[items['id']][
                   'session_type'] and items['session_type'] == workout_session_dict[items['id']][
                   'session_type'], "Category, Complexity value, Session type value and Status combo is not in workout " \
                                    "dictionary "
        assert items['category'] == category, "{} does not match {} from category list.".format(items['category'],
                                                                                                category)
        assert items['complexity'] == complexity, "{} does not match {} from category list.".format(items['complexity'],
                                                                                                    complexity)
        assert items['session_type'] == session, "{} does not match {} from category list.".format(
            items['session_type'],
            session)
        assert items['status'] == status, "{} does not match {} from Status list.".format(items['status'], status)
        logger.info(
            "Workout ID:{} contains Category: '{}', Complexity:'{}, Session Type:'{}' and Status:'{}' in Workout "
            "Session Data Structure".format(
                items['id'], items['category'], items['complexity'], items['session_type'], items['status']))
        count += 1
    logger.info(
        "Total fields with Category:'{}', Complexity:'{}', Session Type:'{}' and Status:'{}' = {}".format(category,
                                                                                                          complexity,
                                                                                                          session,
                                                                                                          status,
                                                                                                          count))
    return 0


def ValidateCompletedWorkoutSessions(response, workout_dict):
    logger.info('Verify response headers for Completed Workout Sessions')
    json_data = json.loads(response.text)
    for items in json_data:
        assert items['workout_id'] > 0, "ID field is less than 0"
        assert items['workout_id'] in workout_dict, "Completed Workout ID: '{}' is not in Master Workout Session Data Structure" \
            .format(items['workout_id'])
    return 0



