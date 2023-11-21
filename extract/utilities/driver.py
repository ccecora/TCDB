from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# May use to create custom modules for this project but not yet
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service)