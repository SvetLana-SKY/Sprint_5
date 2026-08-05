import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

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

@pytest.fixture
def rendom_data():
    email = f"svetlana_{random.randint(10000, 99999)}@ya.ru"
    password = "".join(str(random.randint(0, 9)) for _ in range(6))
    return email, password