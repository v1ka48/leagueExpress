import json
import os
import requests


def create_video(script):
    load_dotenv = False
    from dotenv import load_dotenv
    load_dotenv()
    
    SYNTHESIA_API_KEY = os.getenv('SYNTHESIA_API_KEY')
    SYNTHESIA_ENDPOINT = "https://api.synthesia.io/v2/videos"
    
    headers = {
        "Authorization": f"Bearer {SYNTHESIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "script": {
            "text": script
        },
        "template": "YOUR_TEMPLATE_ID",  # Replace with your Synthesia template ID
        "output_language": "en",
        "voice_over_settings": {
            "voice": "en_us_michael"  # Choose desired voice
        }
        # Add additional parameters as needed
    }
    
    response = requests.post(SYNTHESIA_ENDPOINT, headers=headers, json=payload)
    
    if response.status_code == 201:
        video_id = response.json().get('id')
        print(f"Video creation initiated successfully! Video ID: {video_id}")
        # Optionally, implement polling to check video status and download when ready
        return video_id
    else:
        print(f"Failed to create video: {response.status_code} - {response.text}")
        return None

def download_video(video_id):
    SYNTHESIA_API_KEY = os.getenv('SYNTHESIA_API_KEY')
    DOWNLOAD_ENDPOINT = f"https://api.synthesia.io/v2/videos/{video_id}/download"
    
    headers = {
        "Authorization": f"Bearer {SYNTHESIA_API_KEY}"
    }
    
    response = requests.get(DOWNLOAD_ENDPOINT, headers=headers)
    
    if response.status_code == 200:
        video_content = response.content
        os.makedirs('videos', exist_ok=True)
        video_path = f'videos/weekly_summary_{video_id}.mp4'
        with open(video_path, 'wb') as f:
            f.write(video_content)
        print(f"Video downloaded successfully and saved to {video_path}.")
    else:
        print(f"Failed to download video: {response.status_code} - {response.text}")