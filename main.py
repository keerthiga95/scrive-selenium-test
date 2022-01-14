from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

#url is declared
scriveStagingUrl = 'https://staging.scrive.com/t/9221714692410699950/7348c782641060a9'

#Below Function is called when internet explorer browser is used
def runInSauceLabs():
    capabilities = {
        'browserName': 'internet explorer',
        'browserVersion': '11',
        'platformName': 'Windows 10',
        'sauce:options': {
        }
    }
    authurl="https://oauth-keerthigajayakumar95-51d69:507ef198-686c-4b1e-97ba-48d506c56334@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(authurl,capabilities)
    eSign(driver)

def eSign(driver):
    try:
        #locators are initialized
        scrollArrowSelector = 'svg.scroll-arrow'
        nameToType = 'Test'
        driver.get(scriveStagingUrl) #launch the url
        driver.maximize_window() #maximize the page
        scrollElement= WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, scrollArrowSelector)))
        scrollElement.click() #wait time is added until the page gets load
        driver.find_element(By.ID, 'name').send_keys(nameToType) #Full name is entered
        driver.find_element(By.XPATH, '//div[@class="label"]//span[text()="Next"]').click() #Next button is clicked
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #Scrolling the page to get the view of modal pop up
        driver.find_element(By.CSS_SELECTOR, 'div.section.sign.above-overlay').screenshot('screenshot.png') #taking screenshot of modal popup
        driver.find_element(By.XPATH, '//div[@class="label"]//span[text()="Sign"]').click() #clicking the sign element
        checkIfDocumentSigned(driver) #function is called to validate Document signed diaplayed or not
    finally:
        driver.quit() #terminate the browser

def checkIfDocumentSigned(driver):
    try:
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//h1[@class="follow"]//span[contains(text(),"Document signed!")]')))
        print("Document Signed!")
    except TimeoutException:
        print("Loading took too much time!")

if __name__ == "__main__":
    firefoxDriver = webdriver.Firefox() #initializing firefoxdriver
    chromeDriver = webdriver.Chrome() #initializing chromedriver
    eSign(chromeDriver) #calling esign function for chrome with driver as arguments
    eSign(firefoxDriver) #calling esign function for firefox with driver as arguments
   # runInSauceLabs()   #function is called to run internet exlporer



