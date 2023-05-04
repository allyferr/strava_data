<h1>Strava Data</h1>
<p>This repository contains code that interacts with the Strava API to retrieve and export activities, laps and decoded polyline data.</p>

<p><h2>Getting Started</h2></p>
To use this code, you will need to have a Strava account and create an application in the Strava API. You will also need Python 3 and the following packages installed:
<ul>
  <li>requests</li>
  <li>json</li>
  <li>datetime</li>
  <li>os</li>
  <li>urllib3</li>
  <li>polyline</li>
  <li>pandas</li>  
</ul>

To get started, clone this repository to your local machine and open the strava_data.ipynb notebook in Jupyter or a compatible environment. Follow the instructions in the notebook to authorize access to your Strava data and retrieve your activities and associated data.

<p><h2>Features</h2></p>
The strava_data notebook includes the following features:
<ul>
  <li>Authorization to access Strava data using the OAuth2 protocol</li>
  <li>Retrieval and JSON export of a user's activities from the Strava API</li>
  <li>Retrieval and JSON export of laps for a specific activity</li>
  <li>Retrieval of lat/long coordinates for a specific route</li>
</ul> 
  
<p><h2>Author</h2></p>
This code was written by Allyson Ferretti as an exploration of Python.

<p><h2>Acknowledgements</h2></p>
This code was written using the Strava API documentation and examples from the following resources:
<ul>
  <li>Strava API v3</li>
  <li>Requests: HTTP for Humans</li>
  <li>Pandas: Powerful data analysis tools for Python</li>
  <li>Polyline: A Python implementation of Google's Encoded Polyline Algorithm Format</li>
</ul> 
<p><h2>Personal Aside</h2></p>
<p>This is my first Python project that I created myself. Although there are easier ways to pull Strava data, I wanted to test my skills and see if I could put together a logical tool. I understand that it's not perfect, especially when it comes to error handling or searching duplicated names of activities, but I believe it's a good start, and I learned a lot from it.</p>
