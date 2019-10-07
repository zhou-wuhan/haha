from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver =driver
    def find_element(self,feature,timeout=10,poll=1):
        feature_by,feature_value=feature
        element=WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find-element(feature_by,feature_value))
        return element
