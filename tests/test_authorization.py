from tests.locators import MainPageLocators, RegistrationPageLocators, EnterPageLocators, Authorization
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAuthorization:

    def test_successful_authorization_button_personal_account(self, driver, auth_data):
        driver.get("https://stellarburgers.education-services.ru/")
    
        # Найти кнопку "личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()

        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()

        constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()



    def test_successful_authorization_button_enter_account(self, driver, auth_data): 
        driver.get("https://stellarburgers.education-services.ru/")
        
            # Найти кнопку "Войти в аккаунт" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        enter_acc = wait.until(EC.element_to_be_clickable(MainPageLocators.ENTER_ACCOUNT_BUTTON))
        enter_acc.click()
    
        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()
    
        constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()


    def test_successful_authorization_in_registration_form(self, driver, auth_data): 
        driver.get("https://stellarburgers.education-services.ru/")
        
            # Найти кнопку "Войти в аккаунт" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        enter_acc = wait.until(EC.element_to_be_clickable(MainPageLocators.ENTER_ACCOUNT_BUTTON))
        enter_acc.click()

            # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        reg_link = wait.until(EC.element_to_be_clickable(EnterPageLocators.REGISTRATION_LINK))
        reg_link.click()

            # Найти кнопку "Войти" и кликнуть по ней
        enter_link = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.AUTH_LINK))
        enter_link.click()
    
        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()
    
        constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()


    def test_successful_authorization_in_recover_form(self, driver, auth_data): 
        driver.get("https://stellarburgers.education-services.ru/")
            
        # Найти кнопку "Войти в аккаунт" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        enter_acc = wait.until(EC.element_to_be_clickable(MainPageLocators.ENTER_ACCOUNT_BUTTON))
        enter_acc.click()
    
        # Найти ссылку "Востановить пароль" и кликнуть по ней
        recover_link = wait.until(EC.element_to_be_clickable(EnterPageLocators.RECOVER_PASSWORD_LINK))
        recover_link.click()
    
        # Найти кнопку "Войти" и кликнуть по ней
        enter_rec_link = wait.until(EC.element_to_be_clickable(EnterPageLocators.RECOVER_ENTER_LINK))
        enter_rec_link.click()
        
        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()
        
        constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()        


    

    



