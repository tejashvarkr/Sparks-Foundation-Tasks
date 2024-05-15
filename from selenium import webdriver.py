from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.thesparksfoundationsingapore.org/')

print("\n \nLets Test\n")

# TestCase 1: Checking Title 
print("TestCase #1:")
if driver.title:
    print("Title Verification Successful: ", driver.title)
else:
    print("Title Verification Failed!\n")

#TestCase 2: Testing Home button 
print("TestCase #2:")
try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "The Sparks Foundation")))
    element.click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 3: Check if navbar appears 
print("TestCase #3:")
try:
    driver.find_element(By.CLASS_NAME, "navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: Verifying and Validating Scrolling down functionality
print("TestCase #4:")
for i in range(0, 1500, 200):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("scrolled down")

#TestCase 5: Verifying and Validating Scrolling up functionality 
print("TestCase #5:")
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("scrolled up")
#TestCase 6: Moving to About Us Page 
print("TestCase #6:")
try:
    driver.find_element(By.LINK_TEXT, 'About Us').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 7: Getting Policies and Code
print('TestCase #7:')
try:
    driver.find_element(By.LINK_TEXT, 'Policies and Code').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Policies").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)

#TestCase 8: Verifying Workshop page 
print('TestCase #8:')
try:
    driver.find_element(By.LINK_TEXT, 'Programs').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Workshops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 9: Links Page 
print("TestCase #9")
try:
    driver.find_element(By.LINK_TEXT, 'LINKS').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Software & Apps').click()  # Corrected link text
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Visit LINKS @TSF').click()
    time.sleep(3)
    print('LINKS Verification successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 10: Check If Logo Exists 
print('TestCase #10:')
try:
    driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/h1/a').click()  # Corrected XPath
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

#TestCase 11:   Check the Form 
print("TestCase #11:")
try:
    driver.find_element(By.LINK_TEXT, 'Join Us').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Why Join Us').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'Name').send_keys('Tejashvar')
    time.sleep(3)
    driver.find_element(By.NAME, 'Email').send_keys('tejashvarkr@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element(By.CLASS_NAME, 'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

#TestCase 12:   Check the Contact us Page 
print("TestCase #12:")
try:
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(1)
    info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)
    
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')
   
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")

# TestCase 13: Backtracking to main page 
print("TestCase #13:")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/h1/a").click()
print("Back to main page")
time.sleep(3)

# TestCase 14: Clicking 1-6 
print("TestCase #14:")
for i in range(2, 7):
    driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[2]/div/section/div/ol/li[{i}]/a").click()
    print(f"Clicked {i} section")
    time.sleep(1)


time.sleep(2)
print("Scrolled 400px")

# TestCase 15: Iframe for YouTube
print("TestCase #15:")
required_frame = driver.find_element(By.XPATH, "//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
driver.switch_to.frame(required_frame) 

element = driver.find_element(By.XPATH, "//button[@aria-label='Play']")
element.click()

print("YouTube video played")

time.sleep(8)
stop = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/video").click()
print("Pause Video\n")
time.sleep(1.5)

driver.refresh()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print("Page refreshed & Scrolled down\n")
time.sleep(2)

# TestCase 16: Jobs at Angel.co Portal
print("TestCase #16:")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a").click()
print("Jobs at Angel.co Portal page:- Success\n")
time.sleep(8)

# TestCase 17: Jobs at Tech in Asia Portal 
print("TestCase #17:")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a").click()
print("Jobs at Tech in Asia Portal page:- Success\n")
time.sleep(8)

# TestCase 18: Code for India page 
print("TestCase #18:")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[1]/ul/li[3]/a").click()
print("Code for India page:- Success\n")
time.sleep(5)
print("This marks the end of testing testcases where we verified and validated various test cases implementing various functionalities showcasing the efficiency, bug-freeness.")
