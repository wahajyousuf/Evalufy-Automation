from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


#initializing chrome driver
driver = webdriver.Chrome(executable_path="E:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://test.evalufy.com/")
driver.implicitly_wait(7)
#user login and entering values
driver.find_element_by_id('username').send_keys("admin@evalstar.com")
driver.find_element_by_id('password').send_keys("Test@123")
driver.find_element_by_id('kc-login').click()
#wait time to load all elements
driver.implicitly_wait(10)
driver.find_element_by_link_text('assignment').click()
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[1]/div/div/div/button').click()
driver.implicitly_wait(10)
# DEFINE ASSESSMENT NAME
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys("testing1")
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div/div[3]/button').click()
#drag and drop video question
source = driver.find_element_by_xpath('//*[@id="app"]/div[17]/div/div/div/div[1]/div/div/div[9]/span/span/div/div/div')
destination = driver.find_element_by_xpath('//*[@id="app"]/div[17]/div/div/div/div[2]/div[1]/div/div[1]')
ActionChains(driver).drag_and_drop(source, destination).perform()
#wait for video detailed screen
wait = WebDriverWait(driver, 20)
question_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#app div.v-dialog__content div.formBuilder div.questionsBuilder-block div.draggable-question div.pl-2 input')))
question_name.send_keys("Tell us about your recent projects")
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/nav/div/button[2]').click()
#Dispatching the assessment
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/div/div/button/div').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('Dispatch Assessment').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div/form/div/div[2]/div/div/div[1]/div/input').send_keys("test batch name")
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div/form/div/div[5]/div/div/div[1]/div[1]/div[1]/input').click()
driver.implicitly_wait(5)
#getting the list and select any evaluator
evaluatorList = driver.find_elements(By.CSS_SELECTOR, 'div.v-select-list a div div')

for ele in evaluatorList:
    print(ele.text)
    if ele.text == 'hanadefine personal':
        ele.click()
        break
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[3]/button[3]').click()
driver.implicitly_wait(5)
#copying shareable link
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[1]').click()
copied_url = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/span')
assess_url = copied_url.text
print(assess_url)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[3]/button[3]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div[3]/button[4]').click()
driver.implicitly_wait(10)
#taking assessment
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1
  })
driver = webdriver.Chrome(options=options, executable_path="E:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get(assess_url)
driver.implicitly_wait(10)
#filling out general information
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[2]/div/div/form/div/div[1]/div/div/div[1]/div/input').send_keys("testing")
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[2]/div/div/form/div/div[2]/div/div/div[1]/div/input').send_keys("qa")
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div[2]/div/div/form/div/div[3]/div/div/div[1]/div/input').send_keys("testingqa007@yopmail.com")
driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/div/nav/div/div/div[2]/button').click()
driver.implicitly_wait(20)
startBtn = driver.find_element_by_css_selector('div#app div.landingPage main.v-content nav div.justify-end button')
startBtn.click()
driver.implicitly_wait(20)
agreeBtn = driver.find_element_by_css_selector('div#app div.landingPage main.v-content nav div.justify-end button.primary')
agreeBtn.click()
driver.implicitly_wait(20)
recordBtn = driver.find_element_by_css_selector('div.questionsPage div#candidatesQuestions form button.record')
recordBtn.click()
driver.implicitly_wait(70)
pauseBtn = driver.find_element_by_css_selector('div.questionsPage div#candidatesQuestions form button.pause')
pauseBtn.click()
driver.implicitly_wait(30)
nextBtn = driver.find_element_by_css_selector('div#app div.questionsPage div#candidatesQuestions nav div.justify-end button.primary')
nextBtn.click()
driver.implicitly_wait(20)
