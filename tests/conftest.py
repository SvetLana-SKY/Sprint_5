import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver          
    driver.quit()  

@pytest.fixture
def auth_data():
    return {
        "name": "Svetlana",
        "email": "svetlana_51@ya.ru",
        "password": "111111",
    }