# Liverpool FC & Big Games Calendar

A Python script that automatically fetches Liverpool FC matches and major European club fixtures from the Football Data API and generates an iCal (.ics) file for easy calendar import.

## Features

- 🏆 Fetches all Liverpool FC matches across multiple competitions
- ⚽ Includes big club matchups (Man City, Arsenal, Barcelona, Real Madrid, etc.)
- 📅 Generates iCal format calendar file
- 🔄 Automatic virtual environment setup
- 🍎 macOS integration (auto-opens calendar file)

## Supported Competitions

- Premier League (2021)
- Champions League (2001)
- La Liga (2014)
- Serie A (2019)
- Bundesliga (2002)
- Ligue 1 (2015)

## Prerequisites

- Python 3.x
- Internet connection
- Football Data API token (free tier available at [football-data.org](https://www.football-data.org/))

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd liverpool_game
```

2. Make the update script executable:
```bash
chmod +x update.sh
```

3. Set up your API token:
   - Copy `.env.example` to `.env`: `cp .env.example .env`
   - Edit `.env` and replace `your-api-token-here` with your actual token from [football-data.org](https://www.football-data.org/)

## Usage

### Quick Start

Simply run the update script:

```bash
./update.sh
```

This will:
1. Create a Python virtual environment (if it doesn't exist)
2. Install required dependencies
3. Fetch the latest match data
4. Generate `football_schedule.ics`
5. Open the calendar file in macOS Calendar (on Mac)

### Manual Usage

If you prefer to run the Python script directly:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install requests icalendar pytz python-dotenv

# Run the script
python3 football_cal.py
```

## Project Structure

```
liverpool_game/
├── football_cal.py      # Main Python script
├── update.sh            # Automated update script
├── .env                 # Your API token (not tracked in git)
├── .env.example         # Template for .env file
├── football_schedule.ics # Generated calendar file (not tracked in git)
└── README.md            # This file
```

## Configuration

You can customize the script by modifying the configuration section in `football_cal.py`:

- `FOOTBALL_API_TOKEN`: Set in `.env` file (see Installation step 3)
- `LIVERPOOL_ID`: Team ID for Liverpool (default: 64)
- `BIG_CLUBS`: Dictionary of major club IDs and names
- `COMPETITIONS`: List of competition IDs to fetch matches from

## Dependencies

- `requests` - HTTP library for API calls
- `icalendar` - iCal file generation
- `pytz` - Timezone handling
- `python-dotenv` - Load environment variables from .env file

## Security

✅ **API Token Security**: The API token is stored in a `.env` file which is excluded from version control (see `.gitignore`). This keeps your token secure and private.

- Never commit your `.env` file to git
- The `.env.example` file serves as a template for other users
- Your actual token stays local to your machine

## License

This project is open source and available for personal use.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this project!

## Acknowledgments

- Data provided by [Football Data API](https://www.football-data.org/)
- Built for Liverpool FC fans who want to never miss a match!

