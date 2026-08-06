from tests.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructors:

    def test_navigate_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 5)

        driver.find_element(*MainPageLocators.SAUCES_TUB).click()
        driver.find_element(*MainPageLocators.BUNS_TUB).click()

        buns = wait.until(EC.visibility_of_element_located(MainPageLocators. BUNS_TUB_CLICK))
        assert buns.is_displayed()


    def test_navigate_to_sauces(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 5)
    
        driver.find_element(*MainPageLocators.SAUCES_TUB).click()
        
    
        souces = wait.until(EC.visibility_of_element_located(MainPageLocators.SAUCES_TUB_CLICK))
        assert souces.is_displayed()

    def test_navigate_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 5)
    
        driver.find_element(*MainPageLocators.FILLINGS_TUB).click()
        
    
        fillings = wait.until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_TUB_CLICK))
        assert fillings.is_displayed()
    