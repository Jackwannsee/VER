from selenium import webdriver
from bs4 import BeautifulSoup
import json

with open ("credentials/credentials.json","r+") as jf:
    creds = json.load(jf)

b = webdriver.Chrome()
b.get("https://accounts.veracross.eu/asb/portals/login")

Username = b.find_element_by_id("username")
Username.send_keys("Enter Username Here")

Password = b.find_element_by_id("password")
Password.send_keys("Enter Password Here)

Login = b.find_element_by_id("recaptcha")
Login.click()
