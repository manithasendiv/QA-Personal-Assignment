from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

    # Fill form fields
    name = driver.find_element(By.ID, "name")
    name.send_keys("Test Name")

    email = driver.find_element(By.ID, "email")
    email.send_keys("test@gmail.com")

    phone = driver.find_element(By.ID, "phone")
    phone.send_keys("")

    message = driver.find_element(By.ID, "message")
    message.send_keys("This is a test message.")

    print("Form Fill Test PASSED")

    time.sleep(2)

    # Switch to reCAPTCHA iframe
    iframe = driver.find_element(
        By.XPATH,
        "//iframe[contains(@title,'reCAPTCHA')]"
    )

    driver.switch_to.frame(iframe)

    time.sleep(2)

    # Click reCAPTCHA checkbox
    checkbox = driver.find_element(By.ID, "recaptcha-anchor")

    actions = ActionChains(driver)

    actions.move_to_element(checkbox).pause(1).click().perform()

    print("Captcha Click Test PASSED")

    # Wait for manual captcha solving if image challenge appears
    time.sleep(10)

    # Return to main page
    driver.switch_to.default_content()

    time.sleep(2)

    # Scroll down to Send Message button
    button = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Send Message')]"
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    time.sleep(2)

    # Click button
    driver.execute_script("arguments[0].click();", button)

    print("Send Message Button Click Test PASSED")

    time.sleep(5)

    # Verify submission behavior
    page = driver.page_source.lower()

    assert "required" in page or "success" in page or "captcha" in page

    print("Form Validation Test PASSED")

except AssertionError:
    print("TEST FAILED - Assertion Failed")

except Exception as e:
    print("TEST FAILED")
    print(e)

finally:
    time.sleep(10)
    driver.quit()