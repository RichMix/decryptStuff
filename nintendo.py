#bbynocode - Usr0 — Today at 6:28 PM
# We were using rule sets that had 2mil+ rules
# The trick is to use -w3 -O and -S flags on hashcat
# I could do OneRuleToRuleThemStill.rule in less than 1 minute


import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Nintendo_Entertainment_System_games"

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check for any request errors

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize a list to store all game titles
all_game_titles = []

# Find all tables on the page
tables = soup.find_all('table')

# Loop through each table and extract game titles
for table in tables:
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if columns:
            title = columns[0].get_text(strip=True)  # First column is the game title
            all_game_titles.append(title)

# Output the list of all game titles
for game in all_game_titles:
    print(game)