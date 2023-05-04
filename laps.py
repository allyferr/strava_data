import requests
import json

activities_url = "https://www.strava.com/api/v3/athlete/activities"


# Get ID for selected activity name
def get_id(activity, my_activities):
    selected_activity = [act for act in my_activities if act['name'] == activity]
    selected_activity_id = selected_activity[0]["id"]
    print(f"Activity ID: {selected_activity_id}\n")
    return selected_activity_id


# Get the laps
def get_laps(selected_activity_id, header):
    laps_url = f"https://www.strava.com/api/v3/activities/{selected_activity_id}/laps"
    laps = requests.get(laps_url, headers=header).json()
    print(f"Laps:\n{laps}")
    return laps


# Export laps to JSON
def export_json(laps):
    export = input('Would you like to export the laps to JSON? (Y/N)?: ')
    if export.upper() == 'Y':
        activities_json = json.dumps(laps, indent=4)
        with open(f"strava_laps_{laps[0]['id']}", "w") as outfile:
            outfile.write(activities_json)
        print('Your laps have been exported.')
