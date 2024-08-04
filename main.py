import sigma
from os import system
from time import sleep
from selenium import webdriver

# Open Firefox
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

name = input("What is the username you want to stalk? \n")
username = input("Login with your Instagram\nUsername:\n")
password = input("Password (Don't worry it's safe):   \n")

print("Stalking Begins...")
sleep(1)
system("cls")

sigma.first_login(driver, username, password, name)
while True:
    print(sigma.cycle(driver, name))
    sigma.wait_in_minutes(5)
