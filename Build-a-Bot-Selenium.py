#importing required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#creating class for various method
class LinkedinBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #opening chrome
        self.driver = webdriver.Chrome()
    
    def login(self):
        bot = self.driver
       
        #browsing to linkedin
        bot.get("https://www.linkedin.com/")
        #maximize browser
        bot.maximize_window()
        #paush after page load
        time.sleep(3) 
        #find email and password input
        email = bot.find_element_by_id("session_key")
        password = bot.find_element_by_id("session_password")      
        #clear previous data
        email.clear()
        password.clear()
        #enter inputs
        email.send_keys(self.username)
        password.send_keys(self.username)
        #paush after inputs
        time.sleep(3)
        #hit enter
        password.send_keys(Keys.RETURN)
        #results found or not
        assert "No results found." not in bot.page_source
        #close
        bot.close()

#instances of the class
linkedin = LinkedinBot("xyz@gmail.com", "Xyz\"123")
linkedin.login()