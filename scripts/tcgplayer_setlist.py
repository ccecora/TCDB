from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_set_list(pokemon_set: str):
    url = f"https://www.tcgplayer.com/search/pokemon/sv-scarlet-and-violet-151"

    # Get chrome webdriver setup
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)