import auth
import activities

header = auth.get_new_token()
amt_activities = input('How many activities would you like to fetch?\nType the amount or "All": ')

if amt_activities.upper() == 'ALL':
    activities.export_json(activities.all_activities(amt_activities=amt_activities, header=header))
elif int(amt_activities) > 200:
    activities.export_json(activities.all_activities(amt_activities=amt_activities, header=header))
elif int(amt_activities) <= 200:
    activities.export_json(activities.limited_activities(amt_activities=amt_activities, header=header))
else:
    print("Error, try again.")
