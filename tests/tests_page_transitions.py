from tests.locators import MainPageLocators, RegistrationPageLocators, EnterPageLocators, Authorization
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPageTransitions:

    def  test_click_personal_account_button_redirects_to_auth_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")

        # Найти кнопку "личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click() 

        auth_page = wait.until(EC.visibility_of_element_located(EnterPageLocators.AUTH_PAGE))
        assert auth_page.is_displayed()


    def  test_redirect_from_personal_account_to_constructor(self, driver, auth_data):
        driver.get("https://stellarburgers.education-services.ru/")
            
        # Найти кнопку "личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()
        
        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()

        # Найти кнопку "Конструктор" и кликнуть по ней
        constructor = wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK))
        constructor.click()

        constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        constructor_page.is_displayed()


    def  test_redirect_from_personal_account_to_stellar_burgers(self, driver, auth_data):
            driver.get("https://stellarburgers.education-services.ru/")
                
            # Найти кнопку "личный кабинет" и кликнуть по ней
            wait = WebDriverWait(driver, 5)
            cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
            cabinet_btn.click()
            
            driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
            driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
            driver.find_element(*Authorization.BUTTON_ENTER).click()
    
            # Найти кнопку "Логотип" и кликнуть по ней
            logo = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOTIPE))
            logo.click()
    
            constructor_page = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
            constructor_page.is_displayed()


    def test_logout_button_in_personal_cabinet(self, driver, auth_data):
        driver.get("https://stellarburgers.education-services.ru/")
                        
        # Найти кнопку "личный кабинет" и кликнуть по ней
        wait = WebDriverWait(driver, 5)
        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()
                    
        driver.find_element(*Authorization.EMAIL).send_keys(auth_data["email"])
        driver.find_element(*Authorization.PASSWORD).send_keys(auth_data["password"])
        driver.find_element(*Authorization.BUTTON_ENTER).click()  

        cabinet_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        cabinet_btn.click()

        # Найти кнопку "Выход" и кликнуть по ней 
        logout = wait.until(EC.element_to_be_clickable(Authorization.BUTTON_EXIT))
        logout.click()

        auth_form = wait.until(EC.visibility_of_element_located(EnterPageLocators.AUTH_PAGE))
        assert auth_form.is_displayed()      

                    
    