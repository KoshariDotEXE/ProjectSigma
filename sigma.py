import csv
import math
from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def seconds_in_mins(secs):
    mins = math.floor(secs / 60)
    secs %= 60
    print("{:02d}:{:02d}".format(mins, secs))

def clear_last_line():
    print ("\033[A                             \033[A")

def wait_in_minutes(n):
    for x in range(n*60):
        seconds_in_mins(x)
        sleep(1)
        clear_last_line()

def first_login(driver, stalkername, stalkerpass, victimname):
    # Login
    sleep(3)
    username_field = driver.find_element(By.XPATH, '//input[@type="text"]')
    password_field = driver.find_element(By.XPATH, '//input[@type="password"]')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    ActionChains(driver) \
        .send_keys_to_element(username_field, stalkername) \
        .send_keys_to_element(password_field, stalkerpass) \
        .perform()
    sleep(0.1)
    login_button.click()

    # Navigate to profile
    sleep(15)
    search_button = driver.find_element(By.XPATH, '//span[text()="Search"]')
    search_button.click()
    search_field = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
    ActionChains(driver) \
        .send_keys_to_element(search_field, victimname) \
        .perform()
    sleep(5)
    profile = driver.find_element(By.XPATH, '//span[text()="' + victimname + '"]')
    profile.click()

def data_scrape(driver):
    # Page Refresh
    driver.refresh()
    # Choose the list of desired info
    print('Scraping Data')
    sleep(15)
    datalist = driver.find_element(By.XPATH, '//li[div/span]//ancestor::ul')
    data = datalist.text
    sleep(1)
    clear_last_line()

    return data


def data_extract(dirty_text):
    print("Processing Data")
    sleep(1)
    # Remove the comma
    text = dirty_text.replace(",", "")

    # Parse the numbers
    post_no_str = text.split()[0]
    follower_no_str = text.split()[2]
    following_no_str = text.split()[4]

    # Convert to integers
    post_no = int(post_no_str)
    follower_no = int(follower_no_str)
    following_no = int(following_no_str)

    # Get current date and time
    logging_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    sleep(1)
    clear_last_line()

    # Store in List
    return [logging_time, post_no, follower_no, following_no]

def data_log(victimname, info):
    print("Logging Data")
    sleep(1)
    # open the file in the write mode
    f = open(victimname + ".csv", 'a')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(info)

    # close the file
    f.close()
    sleep(1)
    clear_last_line()

def cycle(driver, victimname):
    data = data_scrape(driver)
    info = data_extract(data)
    data_log(victimname, info)
    return info
