import requests
import json
from datetime import date

activities_url = "https://www.strava.com/api/v3/athlete/activities"


# When user wants the most recent 200 activities or fewer
def limited_activities(amt_activities, header):
    param = {'per_page': int(amt_activities), 'page': 1}
    my_activities = requests.get(activities_url, headers=header, params=param).json()
    print(f'{amt_activities} have been fetched.')
    return my_activities


# When user wants All activities
def all_activities(amt_activities, header):
    per_page = 200
    request_page_num = 1
    my_activities = []
    print('Fetching activities...')
    while True:
        param = {'per_page': per_page, 'page': request_page_num}
        # initial request, where we request the first page of activities
        my_dataset = requests.get(activities_url, headers=header, params=param).json()

        # Check the response to make sure it is not empty. If it is empty, that means there is no more data left.
        if len(my_dataset) == 0:
            break

        # If the all_activities list is already populated, that means we want to add additional data via extend.
        if my_activities:
            my_activities.extend(my_dataset)

        # If the all_activities list is empty, this is the first time adding data so set it equal to my_dataset
        else:
            my_activities = my_dataset

        # If we don't want all activities, we need to reduce the per_page
        if amt_activities.upper() != 'ALL':
            activities_remaining = int(amt_activities) - 200 * request_page_num
            if 0 < activities_remaining <= 200:
                per_page = activities_remaining
            elif activities_remaining <= 0:
                per_page = 0
            elif activities_remaining > 200:
                per_page = 200

            # print(f'per_page: {per_page}\n')
            # print(f'activities_remaining {activities_remaining}\n')
            # print(f'loop {request_page_num}')

            request_page_num += 1

    print(f'{len(my_activities)} have been fetched.')
    return my_activities


# Export JSON File
def export_json(my_activities):
    export = input('Would you like to export the activities to JSON? (Y/N)?: ')
    if export.upper() == 'Y':
        activities_json = json.dumps(my_activities, indent=4)
        with open(f"strava_activities_{date.today()}", "w") as outfile:
            outfile.write(activities_json)
        print('Your activities have been exported.')
