import requests
import polyline
import pandas as pd
import auth


# Get the full activity from Strava
def activity_by_id(activity_id, header):
    activity_url = f"https://www.strava.com/api/v3/activities/{activity_id}/"
    my_activity = requests.get(activity_url, headers=header).json()
    print(f'Activity {activity_id} has been fetched.')
    # print(my_activity)
    return my_activity


# Get the summary polyline from the file, convert to dataframe and export to CSV
def decode_polyline(activity):
    column_names = ['Long', 'Lat']
    summary_polyline = activity['map']['summary_polyline']
    df = pd.DataFrame(polyline.decode(summary_polyline, geojson=True), columns=column_names)
    decode_file = df.to_csv(f'polylines_{activity["name"]}.csv', index=True, index_label='Pos_No')
    print('The polyline decode has been exported to CSV')
