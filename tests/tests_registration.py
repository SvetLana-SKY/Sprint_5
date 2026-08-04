from tests.locators import MainPageLocators, RegistrationPageLocators, EnterPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")

        # Найти кнопку "Личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()

        # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        reg_link = wait.until(EC.element_to_be_clickable(EnterPageLocators.REGISTRATION_LINK))
        reg_link.click()

        
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT))
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Svetlana")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("svetlana_51@ya.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("111111")
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()

        auth_page = driver.find_element(*EnterPageLocators.AUTH_PAGE)
        assert auth_page.is_displayed()

    def test_error_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
                # Найти кнопку "Личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()
        
        # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        reg_link = wait.until(EC.element_to_be_clickable(EnterPageLocators.REGISTRATION_LINK))
        reg_link.click()
        
                
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT))
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Svetlana")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("svetlana_51@ya.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("111")
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()

        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        assert error_message.is_displayed()
        
         

    