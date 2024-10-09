# Locators for various elements on the Entrata website
class Locators:
    # Cookie consent
    COOKIE_CLOSE = "//*[@id='cookie-close']"

    # Products link
    PRODUCTS_LINK = "//*[@id='w-dropdown-toggle-0']"

    # Resident Services link
    RESIDENT_SERVICES_LINK = "(//a[text()='Resident Services'])[2]"

    # Watch Demo button
    WATCH_DEMO_BUTTON = "//*[@id='product-banner-button']"

    # Basecamp link
    BASECAMP_LINK = "(//nav//a[contains(text(), 'Basecamp')])[1]"

    # Form fields (using IDs directly)
    FIRST_NAME = "FirstName"
    LAST_NAME = "LastName"
    EMAIL = "Email"
    COMPANY_NAME = "Company"
    PHONE_NUMBER = "Phone"
    JOB_TITLE = "Title"
    SCHEDULE_DEMO = "//button[text()='SCHEDULE DEMO']"

    # Dropdowns (using XPaths)
    UNIT_COUNT_DROPDOWN = "//*[@id='Unit_Count__c']"
    DEMO_REQUEST_DROPDOWN = "//*[@id='demoRequest']"

    # Why Attend link
    WHY_ATTEND_LINK = "//*[@id='bc-why-attend-link']"

    # Why Attend title
    WHY_ATTEND_TITLE = "//h2[text()='why attend?']"

    # Agenda link
    AGENDA_LINK = "(//div[text()='Agenda'])[2]"

    # Search box and result
    SEARCH_BOX = "//*[@id='search']"
    SEARCH_RESULT = "(//div[text()='Lunch'])[1]"

    # Sign-in and navigation
    SIGN_IN_BUTTON = "(//a[text()='Sign In'])[1]"
    RESIDENT_LOGIN = "//div[text()='Resident Login']"
    VIEW_WEBSITE = "//div[@class='start-button website-button']"
    FEATURES_TAB = "//div[@class='landing-nav four-content']/a[2]"
    FEATURES_CONTENT = "//div[@class='alexa-quote-icon']"
