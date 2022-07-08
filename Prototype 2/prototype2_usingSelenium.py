# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

###################### creating chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {

	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

######################################################

####################################
def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
 
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
 
    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
 
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)
####################################

############function to join meeting##################3
##############funtion not debugged----------------------->
def joinMeet():
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
    driver.implicitly_wait(3000)


##################### function to turn off mic and cam on start screen
def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
 
    # turn off camera
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)

    time.sleep(2)
    joinMeet()
##########################################################


if __name__ == '__main__':
    
    ###############mail id and pass ##############
    mail_address="testforminorproject@gmail.com"
    password="minorproject"
    ###########login google################
    Glogin(mail_address,password)

    #########################go to google meet##############
    driver.get('https://meet.google.com/iqv-icbu-xbg')
    ##################################################

    ##########calling fuctions########
    turnOffMicCam()

    #joinMeet() #function calling shifted inside turnOffMicCam()