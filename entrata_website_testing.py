import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Fixture to set up the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_navigation_to_main_sections(driver):
    """
    Test Case 1: Verify navigation to the main sections of the website.
    This test checks if the user can successfully navigate to the 'Products' section
    from the homepage.
    """
    driver.get("https://www.entrata.com/")  # Open the homepage
    driver.maximize_window()

    # Step 1: Handle the cookie consent popup
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.COOKIE_CLOSE))
        )
        cookies.click()
    except Exception as e:
        print("Cookie consent button not displayed or clickable:", e)

    # Step 2: Hover over the 'Products' link
    action = ActionChains(driver)
    products_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.PRODUCTS_LINK))
    )
    action.move_to_element(products_link).perform()

    # Step 3: Click on 'Resident Services' link
    resident_service = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, Locators.RESIDENT_SERVICES_LINK))
    )
    driver.execute_script("arguments[0].click();", resident_service)

    # Step 4: Click on 'Watch Demo' button
    watch_demo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.WATCH_DEMO_BUTTON))
    )
    watch_demo.click()

    # Verify the title of the new page
    assert WebDriverWait(driver, 10).until(EC.title_is("Entrata | Property Management the Way It Should Be")), \
        "Page did not open as expected: Title did not match."

    # Fill out the demo request form using IDs
    first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.FIRST_NAME)))
    last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.LAST_NAME)))
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.EMAIL)))
    company_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.COMPANY_NAME)))
    phone_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PHONE_NUMBER)))
    job_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.JOB_TITLE)))
    schedule_demo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.SCHEDULE_DEMO)))
    # Use XPath for dropdowns
    unit_count_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.UNIT_COUNT_DROPDOWN)))
    demo_request_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.DEMO_REQUEST_DROPDOWN)))

    # Fill the form fields
    first_name.send_keys("Saurabh")
    last_name.send_keys("Magdum")
    email.send_keys("smagdum701@gmail.com")
    company_name.send_keys("entrata")
    phone_number.send_keys("1234567899")
    job_title.send_keys("phone_number")

    # Select options from dropdowns
    select = Select(unit_count_dropdown)
    select.select_by_index(1)

    select = Select(demo_request_dropdown)
    select.select_by_visible_text("a Resident")

    if schedule_demo.is_displayed():
        assert True  # This assertion will always pass if the condition is met
    else:
        assert False, "Schedule Demo button is not displayed."


def test_basecamp_explore_more(driver):
    """
    Test Case 2: Check if the main banner is visible on the homepage.
    This test ensures that the main promotional banner is displayed correctly.
    """
    driver.get("https://www.entrata.com/")  # Open the homepage
    driver.maximize_window()

    # Step 1: Handle the cookie consent popup
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.COOKIE_CLOSE))
        )
        cookies.click()
    except Exception as e:
        print("Cookie consent button not displayed or clickable:", e)

    # Step 2: Click the Basecamp link
    basecamp_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, Locators.BASECAMP_LINK))
    )
    driver.execute_script("arguments[0].click();", basecamp_link)

    # Optional: Replace this sleep with an explicit wait for the new window to load
    time.sleep(5)

    # Step 3: Switch to the new window
    driver.switch_to.window(driver.window_handles[1])

    # Verify the title of the new page
    assert WebDriverWait(driver, 10).until(EC.title_is("Basecamp 2025 | Entrata")), \
        "Page did not open as expected: Title did not match."

    # Step 4: Click 'Why Attend' link
    why_attend_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Locators.WHY_ATTEND_LINK))
    )
    why_attend_link.click()

    # Verify 'Why Attend' section is displayed
    why_attend_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.WHY_ATTEND_TITLE))
    )
    assert why_attend_title.is_displayed(), "Why Attend title is not displayed."

    # Step 5: Click on 'Agenda' link
    agenda_link = driver.find_element(By.XPATH, Locators.AGENDA_LINK)
    driver.execute_script("arguments[0].click();", agenda_link)

    # Step 6: Search for 'Lunch'
    search_box = driver.find_element(By.XPATH, Locators.SEARCH_BOX)
    search_box.send_keys("Lunch")

    search_result = driver.find_element(By.XPATH, Locators.SEARCH_RESULT)
    assert search_result.is_displayed(), "Search result for 'Lunch' is not displayed."


def test_sign_in_and_navigation(driver):
    """
    Test Case 3: Sign in to the website, navigate through various sections
    """
    driver.get("https://www.entrata.com/")  # Open the homepage
    driver.maximize_window()

    # Step 1: Handle the cookie consent popup
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.COOKIE_CLOSE))
        )
        cookies.click()
    except Exception as e:
        print("Cookie consent button not displayed or clickable:", e)

    # Step 2: Click the SignIn button
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.SIGN_IN_BUTTON)))
    driver.execute_script("arguments[0].click();", sign_in_button)

    # Step 3: Click on Resident Login
    resident_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.RESIDENT_LOGIN)))
    resident_login.click()

    # Step 4: Click 'View the Website' button
    view_website = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.VIEW_WEBSITE)))
    view_website.click()

    # Step 5: Click the Features tab and validate page content
    features_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.FEATURES_TAB)))
    features_tab.click()

    # Validate content on the Features page
    features_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.FEATURES_CONTENT))
    )
    assert features_content.is_displayed(), "Features content is not displayed."
