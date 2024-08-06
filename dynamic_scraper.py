from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the Service object using ChromeDriver
service = ChromeService(ChromeDriverManager().install())

# Initialize the Chrome WebDriver with the Chrome service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_player_stats(url):
    # Extract player_id from URL
    player_id = url.split('/')[-1]
    
    # Fetch the page
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(5)
    
    # Get the page source
    page_content = driver.page_source
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Find the div containing the statistics table
    stats_div = soup.find('div', class_='stats-table col-md-7 col-xs-12')
    
    if stats_div:
        # Initialize the dictionary with the player_id
        stats_dict = {"player_id": player_id}
        
        # Extract table rows
        for row in stats_div.find_all('div', class_='stats-row'):
            cols = row.find_all('div')
            if len(cols) == 2:
                key = cols[0].text.strip()
                value = cols[1].text.strip()
                # Convert value to int if possible, otherwise keep as string
                stats_dict[key] = int(value) if value.isdigit() else value
        
        return stats_dict
    else:
        return None

# URL to scrape
url = 'https://www.football.co.il/player/45897'

# Scrape the player stats
player_stats = scrape_player_stats(url)

# Quit the driver
driver.quit()

# Print the resulting dictionary
if player_stats:
    print(player_stats)
else:
    print("Statistics not found on the page.")