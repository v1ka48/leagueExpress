import json
import os

import openai
from dotenv import load_dotenv


def generate_script(summary):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    prompt = f"""
    Create a funny and engaging script for a video summarizing the weekly performance of a Yahoo Fantasy Sports league.
    Here are the details:
    - Total Points: {summary['Total Points']}
    - Average Points: {summary['Average Points']}
    - Top Performer: {summary['Top Performer']['name']} with {summary['Top Performer']['score']} points
    - Lowest Performer: {summary['Lowest Performer']['name']} with {summary['Lowest Performer']['score']} points
    - Upcoming Matchups: {', '.join([f"{matchup}" for matchup in summary['Upcoming Matchups']])}
    
    Make sure the script includes jokes, banter, playful roasting for the lowest-scoring team, hyping the big winner, and playful trash talk for upcoming matchups.
    Ensure the tone is humorous, lively, and suitable for a sports video presentation.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a witty and humorous sports commentator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.8,
    )

    script = response['choices'][0]['message']['content'].strip()
    
    os.makedirs('scripts', exist_ok=True)
    with open('scripts/weekly_summary.txt', 'w') as f:
        f.write(script)
    
    print("Script generated and saved successfully.")
    return script