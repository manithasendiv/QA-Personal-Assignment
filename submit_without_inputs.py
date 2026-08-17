from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://safora.se/en/")

try:
    # Open Contact Us page
    contact_us = driver.find_element(
        By.XPATH,
        "//a[contains(@href,'/en/contact.html')]"
    )

    driver.execute_script("arguments[0].click();", contact_us)

    time.sleep(5)
    
    # Find Send Message button
    button = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Send Message')]"
    )

    # Scroll to button
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    time.sleep(2)

    # Click button without filling inputs
    driver.execute_script("arguments[0].click();", button)

    print("Send Message Button Clicked")

    time.sleep(3)

    # Check validation behavior
    name = driver.find_element(By.ID, "name")
    email = driver.find_element(By.ID, "email")
    message = driver.find_element(By.ID, "message")

    # HTML5 validation check
    name_valid = name.get_attribute("validationMessage")
    email_valid = email.get_attribute("validationMessage")
    message_valid = message.get_attribute("validationMessage")

    # Assertions
    assert name_valid != ""
    assert email_valid != ""
    assert message_valid != ""

    print("Validation Test PASSED")

    print("Name Validation:", name_valid)
    print("Email Validation:", email_valid)
    print("Message Validation:", message_valid)

except AssertionError:
    print("TEST FAILED - Validation not detected")

except Exception as e:
    print("TEST FAILED")
    print(e)

finally:
    time.sleep(10)
    driver.quit()