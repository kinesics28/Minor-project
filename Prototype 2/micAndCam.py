from controlFunctions import meetLogin
from VoiceInputModule import speechToText

def mic():
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
    driver.implicitly_wait(3000)
    pass


def video():
    pass