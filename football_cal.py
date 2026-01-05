import requests
import datetime
from icalendar import Calendar, Event
import pytz
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
API_TOKEN = os.getenv('FOOTBALL_API_TOKEN')
if not API_TOKEN:
    raise ValueError("FOOTBALL_API_TOKEN not found in environment variables. Please create a .env file with your API token.")
LIVERPOOL_ID = 64
BIG_CLUBS = {
    64: "Liverpool", 65: "Man City", 57: "Arsenal", 66: "Man Utd", 61: "Chelsea",
    81: "Barcelona", 86: "Real Madrid", 78: "Atleti",
    157: "Bayern", 4: "Dortmund",
    108: "Inter", 109: "Juventus", 110: "Milan",
    524: "PSG"
}
COMPETITIONS = [2021, 2001, 2014, 2019, 2002, 2015]

def get_matches():
    headers = {'X-Auth-Token': API_TOKEN}
    all_selected_matches = []
    
    for comp in COMPETITIONS:
        url = f"https://api.football-data.org/v4/competitions/{comp}/matches?status=SCHEDULED"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                matches = response.json().get('matches', [])
                for m in matches:
                    home_id = m['homeTeam']['id']
                    away_id = m['awayTeam']['id']
                    if home_id == LIVERPOOL_ID or away_id == LIVERPOOL_ID:
                        all_selected_matches.append(m)
                    elif home_id in BIG_CLUBS and away_id in BIG_CLUBS:
                        all_selected_matches.append(m)
            else:
                print(f"Failed to fetch data for competition {comp}: {response.status_code}")
        except Exception as e:
            print(f"Network error: {e}")
            
    return all_selected_matches

def create_ics(matches):
    cal = Calendar()
    # Add X-WR-CALNAME property for automatic calendar naming when importing
    cal.add('x-wr-calname', 'Liverpool & European Big Games')
    cal.add('prodid', '-//Liverpool & Big Games Calendar//mx//')
    cal.add('version', '2.0')

    # Get current time as basis for event updates
    now = datetime.datetime.now(pytz.utc)

    for m in matches:
        event = Event()
        
        # --- Core fix: prevent duplicates ---
        # 1. Use unique match ID as UID, this is key for deduplication
        match_id = str(m['id'])
        event.add('uid', f"football_match_{match_id}@gemini_script")
        
        # 2. Add DTSTAMP (creation/update timestamp)
        event.add('dtstamp', now)
        
        # 3. Add SEQUENCE (sequence number), if match time changes, calendar will update based on this
        event.add('sequence', int(now.timestamp()))
        # ------------------------

        summary = f"⚽ {m['homeTeam']['name']} vs {m['awayTeam']['name']}"
        desc = f"Competition: {m['competition']['name']}"
        
        start_time = datetime.datetime.strptime(m['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
        start_time = start_time.replace(tzinfo=pytz.utc)
        
        event.add('summary', summary)
        event.add('dtstart', start_time)
        event.add('dtend', start_time + datetime.timedelta(hours=2))
        event.add('description', desc)
        
        cal.add_component(event)

    with open('football_schedule.ics', 'wb') as f:
        f.write(cal.to_ical())
    print(f"Successfully updated! Total of {len(matches)} matches.")

if __name__ == "__main__":
    matches = get_matches()
    create_ics(matches)