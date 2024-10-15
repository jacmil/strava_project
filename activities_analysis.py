from strava_requests import Requester
import datetime
import json


# build personal class
jackson = Requester()

# get tokens and set new access token
tokens = jackson.get_oauth_token()
jackson.access_token = tokens["access_token"]

# get activities

le_json = json.dumps(jackson.get_activities(), indent=2)
data = json.loads(le_json)


# calculate weekly distance
'''
this code below is functional for what it is. it adds the current week's dist to a list, 
and then goes through each activity, appending the last 7 as a week into weeklydist.
the issue is that it does each 'week' as the last 7 activities, not necessarily as the
last 7 days. I need logic to check the dates of activities and compare it against the
last activity to measure how many days it has been (0 - sentinel).
'''

# weekly_dist = []
#
# current_week = 0
# today = datetime.datetime.today().weekday()
#
# for day in range(today):
#     current_week += data[day]["distance"]
# weekly_dist.append(current_week * 0.000621371)
#
# for week in range(4):
#     dist = 0
#     ob_week = []
#     for day in range((week * 7) + today, 7 + (week * 7) + today):
#         dist += data[day]["distance"]
#         ob_week.append(dist * 0.000621371)
#     weekly_dist.append([dist* 0.000621371, ob_week])

print(weekly_dist)