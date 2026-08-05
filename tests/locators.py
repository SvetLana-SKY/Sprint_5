
from selenium.webdriver.common.by import By

class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")   # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # "Личный кабинет"
    CONSTRUCTOR_PAGE = (By.XPATH, "//button[text()='Оформить заказ']")  # Страница конструктора
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text() = 'Конструктор']")  # "Конструктор"
    LOGOTIPE = (By.CSS_SELECTOR, 'svg[width="290"][height="50"]') # "логотип"
    BUNS_TUB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')  # Раздел конструктора "Булки"
    BUNS = (By.XPATH, "//h2[text()='Булки']")  # Заголовок "Булки" в ленте
    SAUCES_TUB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')  # Раздел конструктора "Соусы"
    SAUCES = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок "Соусы" в ленте
    FILLINGS_TUB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')  # Раздел конструктора "Начинки"
    FILLINGS = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок "Начинки" в ленте


class EnterPageLocators:
    REGISTRATION_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']") #ссылка "Зарегистрироваться"
    AUTH_PAGE = (By.XPATH, "//div[(@class = 'Auth_login__3hAey')]")  # страница входа для зарегистрированных
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # ссылка "Восстановить пароль"
    RECOVER_FORM = (By.XPATH, "//h2[text() = 'Восстановление пароля']")  # форма "Восстановления пароля"
    RECOVER_ENTER_LINK = (By.XPATH, '//a[contains(@class, "Auth_link__1fOlj") and text() = "Войти"]')  # ссылка "Войти"

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@type='text' and @name='name']") # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name' and @value='']") # Поле ""e-mail"
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") # поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    AUTH_LINK = (By.XPATH, '//a[contains(@class, "Auth_link__1fOlj") and text() = "Войти"]')  # ссылка "Войти"
    ERROR_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # сообщение об ошибке Некорректный пароль

class Authorization:  
    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]") # поле "Email"
    PASSWORD = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]") # поле "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']") # кнопка 'Войти'
    BUTTON_EXIT = (By.XPATH, "//button[text() = 'Выход']")  # кнопка 'Выход':