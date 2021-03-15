import pytest

@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver_path = "C:\\Users\\abc\\Desktop\\Python P\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    request.cls.driver = driver
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()