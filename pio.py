from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import glob
import os

class PioReportPull:

    def __init__(self, email: str, password: str, report_search: str):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self._login = email
        self._password = password
        self._report_search = report_search
        login_url = 'https://app.placements.io/users/sign_in'
        reports_url = 'https://app.placements.io/custom_billing'
        email_xpath  = '/html/body/div/div[2]/div/div/div/' \
                             'form/div[1]/input'
        password_xpath = '/html/body/div[2]/div[2]/div/div/div/' \
                               'form/div[2]/input'
        report_input_xpath = '/html/body/div[4]/div[2]/div/div/div/div[1]/' \
                             'div[1]/div/div/div[1]/span[1]/div[2]/input'
        download_button_xpath = '/html/body/div[4]/div[2]/div/div/div/div[2]' \
                                '/div/ul/div/div/li[2]/div/div[1]/a/i'
        #download_button_xpath is currently set to the second option that appears
        #after you search for a term. You should update this xpath to meet your needs.
        #I recommend directing it to the first option that is returned from the search.
        self.login(driver, self._login, self._password, login_url, email_xpath,
                   password_xpath)
        time.sleep(1)
        self.access_report(driver, self._report_search, report_input_xpath,
                           download_button_xpath, reports_url)
        self.path = self.report_path()

    def login(self, driver: webdriver, email: str, password: str, url: str,
              email_xpath: str, password_xpath: str):
        driver.get(url=url)
        email_box = driver.find_element_by_xpath(email_xpath)
        email_box.send_keys(email)
        email_box.submit()
        time.sleep(2)
        password_box = driver.find_element_by_xpath(password_xpath)
        password_box.send_keys(password)
        password_box.submit()

    def access_report(self, driver: webdriver, report:str ,report_xpath:str,
                      download_xpath: str, url: str):
        driver.get(url=url)
        report_input = driver.find_element_by_xpath(report_xpath)
        report_input.send_keys(report)
        report_input.send_keys(Keys.RETURN)
        time.sleep(2)
        download_button = driver.find_element_by_xpath(download_xpath)
        download_button.click()

    def report_path(self):
        time.sleep(10)
        file_path = glob.glob(#path) #insert the path to the downloads file on your computer
         latest_file = max(file_path, key=os.path.getmtime) 
        return latest_file

    def get_report_path(self):
        return self.path








