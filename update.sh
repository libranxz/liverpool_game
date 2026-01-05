#!/bin/bash

# Get the directory where the script is located
cd "$(dirname "$0")"

echo "--- Starting Liverpool schedule update program ---"

# 1. If venv folder doesn't exist, create one
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Ensure necessary libraries are installed (check each run to ensure environment is OK)
echo "Checking dependencies..."
pip install -q requests icalendar pytz python-dotenv

# 4. Run Python script
echo "Fetching latest match information and generating calendar..."
python3 football_cal.py

# 5. Automatically open generated .ics file with Mac Calendar
if [ -f "football_schedule.ics" ]; then
    echo "Success! Importing to Mac Calendar..."
    open football_schedule.ics
else
    echo "Error: Failed to generate .ics file, please check API Token or network."
fi

echo "--- Update complete ---"