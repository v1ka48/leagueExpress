import json
import os


def process_data():
    with open('data/weekly_stats.json', 'r') as f:
        data = json.load(f)
    
    # Example: Extract team scores and rankings
    teams = []
    for matchup in data['scoreboard']['matchups']:
        team1 = matchup['teams'][0]
        team2 = matchup['teams'][1]
        teams.append({
            'name': team1['team']['name'],
            'score': team1['team']['team_points']['total'],
            'ranking': team1['team']['rank']
        })
        teams.append({
            'name': team2['team']['name'],
            'score': team2['team']['team_points']['total'],
            'ranking': team2['team']['rank']
        })
    
    # Calculate total points, average points
    total_points = sum(team['score'] for team in teams)
    average_points = total_points / len(teams) if teams else 0
    
    # Identify top and lowest performers
    top_performer = max(teams, key=lambda x: x['score'], default=None)
    lowest_performer = min(teams, key=lambda x: x['score'], default=None)
    
    # Upcoming matchups (this example assumes you have such data)
    # Adjust based on actual data structure
    upcoming_matchups = []  # Populate with actual upcoming data
    
    summary = {
        'Total Points': total_points,
        'Average Points': round(average_points, 2),
        'Top Performer': top_performer,
        'Lowest Performer': lowest_performer,
        'Upcoming Matchups': upcoming_matchups
    }
    
    # Save summary to JSON
    os.makedirs('data', exist_ok=True)
    with open('data/summary.json', 'w') as f:
        json.dump(summary, f, indent=4)
    
    print("Data processed and summary saved successfully.")
    return summary