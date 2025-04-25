import json
import os
import requests
from dotenv import load_dotenv


def fetch_data():
    load_dotenv()
    
    CLIENT_ID = os.getenv('YAHOO_CLIENT_ID')
    CLIENT_SECRET = os.getenv('YAHOO_CLIENT_SECRET')
    LEAGUE_ID = os.getenv('YAHOO_LEAGUE_ID')
    
    # Obtain OAuth2 access token
    auth_url = "https://api.login.yahoo.com/oauth2/get_token"
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    auth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    auth_response = requests.post(auth_url, data=auth_data, headers=auth_headers)
    
    if auth_response.status_code == 200:
        access_token = auth_response.json().get('access_token')
    else:
        raise Exception(f"Failed to authenticate with Yahoo API: {auth_response.status_code} - {auth_response.text}")
    
    # Fetch weekly stats
    stats_url = f"https://fantasysports.yahooapis.com/fantasy/v2/league/{LEAGUE_ID}/scoreboard"
    stats_headers = {
        'Authorization': f"Bearer {access_token}"
    }
    
    stats_response = requests.get(stats_url, headers=stats_headers)
    
    if stats_response.status_code == 200:
        stats_data = stats_response.json()
        with open('data/weekly_stats.json', 'w') as f:
            json.dump(stats_data, f, indent=4)
        print("Weekly stats fetched and saved successfully.")
    else:
        raise Exception(f"Failed to fetch weekly stats: {stats_response.status_code} - {stats_response.text}")