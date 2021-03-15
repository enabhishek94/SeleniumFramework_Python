from Library import *
from selenium.webdriver.support.ui import Select

class SeleniumWrapper:

    def __init__(self,driver):
        self.driver = driver

    def enter_text(self,element,*,value):
        locator_type, locator_value=element
        self.driver.find_element(locator_type,locator_value).clear()
        self.driver.find_element(locator_type,locator_value).send_keys(value)

    def click_element(self,element):
        locator_type, locator_value=element
        self.driver.find_element(locator_type,locator_value).click()

    def select_list_item(self, element, *, item):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        if isinstance(item,str):
            select.select_by_visiable_text(item)
        else:
            select.select_by_index(item)

    def select_multiple_items(self, element, *, item):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        select.deselect_all()
        if isinstance(item,str):
            select.select_by_visiable_text(item)
        else:
            select.select_by_index(item)

    def switch_to_window(self,window_index):
        if window_index< len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])

        else:
            raise NoSuchWindowException("window doesn't exist")

    def close_window(self,window_index):
        if window_index< len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            self.driver.close()

        else:
            raise NoSuchWindowException("window doesn't exist")

    def cloase_all_child_window(self):
        handles = self.driver.window_handles
        for index in range(1,len(handles)):
            self.driver.switch_to.window(handles[index])
            self.driver.close()

    def get_page_title(self):
        return self.driver.title.strip()

    def get_web_elements(self,elements):
        locator_type, locator_value = elements
        return self.driver.find_elements(locator_type,locator_value)

    def send_keyboard_input(self,key):
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()

    def mouse_hover(self,element):
        locator_type,locator_value=element
        action = ActionChains(self.driver)
        element = self.driver.find_element(locator_type,locator_value)
        action.move_to_element(element).perform()

    def js_enter_text(self,element,*,value):
        locator_type,locator_value = element
        element  = self.driver.find_element(locator_type,locator_value)
        self.driver.execute_script('arguments[0].value=arguments[1]',element,value)

    def js_scroll_up(self):
        self.driver.execute_script("window.scrollBy(0,-300)")

    def js_scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,300)")

    def js_scroll_right(self):
        self.driver.execute_script("window.scrollBy(300,0)")

    def js_scroll_left(self):
        self.driver.execute_script("window.scrollBy(-300,0)")

    def js_page_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def js_page_up(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    def js_scroll_element(self,element):
        locator_type, locator_value = element
        element = self.driver.find_element(locator_type,locator_value)
        self.driver.execute_script('arguments[0].scrollIntoView()',element)

    @staticmethod
    def get_date_time_stamp():
        temp_date_time = datetime.datetime.now()
        return  str(temp_date_time)[:19].replace(':','').replace(' ','_'.replace('-','_'))

    @staticmethod
    def get_random_number():
        temp_date_time = datetime.datetime.now()
        return str(temp_date_time)[20:]

    @staticmethod
    def get_by_type(loc):
        if len(loc)!=2:
            raise AttributeError("Missing Locator",loc)
        locator_type, locator_value = loc
        if locator_type.upper() not in {'XPATH','NAME','ID','CSS_SELECTOR','CLASS_NAME','TAG_NAME'}:
            raise ValueError("Invalid Locator Type",locator_type)
        if locator_type.upper() == 'XPATH':
            return By.XPATH, locator_value
        elif locator_type.upper() == 'Name':
            return By.NAME, locator_value
        elif locator_type.upper() == 'ID':
            return By.ID, locator_value
        elif locator_type.upper() == 'CSS_SELECTOR':
            return By.CSS_SELECTOR, locator_value
        elif locator_type.upper() == 'CLASS_NAME':
            return By.CLASS_NAME, locator_value

        @staticmethod
        def log_message(message):
            print('<br>' +str(message))


