from Library import *

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
