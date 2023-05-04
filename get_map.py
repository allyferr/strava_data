import auth
import activities
import laps
import polyline_decode

header = auth.get_new_token()

lookup_method = input('Would you like to look-up the activity by name or ID?  Type "Name" or "ID": ')

# When looking up by name, you first need to find the activity ID
if lookup_method.upper() == 'NAME':
    activity = input("Type the activity name exactly as it appears in Strava: ")
    # Pulling all activities takes a long time, giving option to pull from recent activities to improve performance
    lookback = input("Is this a somewhat recent activity (within last 200 logged activities)?  Y/N: ")
    if lookback.upper() == 'Y':
        my_activities = activities.limited_activities(amt_activities=200, header=header)
    else:
        my_activities = activities.all_activities(amt_activities='ALL', header=header)
    activity_id = laps.get_id(activity=activity, my_activities=my_activities)

elif lookup_method.upper() == 'ID':
    activity_id = input("Type the activity ID: ")


my_activity = polyline_decode.activity_by_id(activity_id, header)
polyline_decode.decode_polyline(my_activity)
