from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import getpass


# Tweets 
def Tweet(data):
    browser.get('https://twitter.com/compose/tweet')
    time.sleep(2)
    
    actions = ActionChains(browser)
    actions.send_keys(data)
    actions.perform()
    
    button = browser.find_element_by_css_selector("div[class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-vw2c0b r-1777fci r-eljoum r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0']")
    button.click()


# Gets the data and passes it to `Tweet`
def sendTweet(browser):
    browser.get("https://fedoramagazine.org/")
    posts = [post.text for post in browser.find_elements_by_class_name("post")]
    a = [post.find_element_by_tag_name("a").get_attribute("href") for post in browser.find_elements_by_class_name("post")]
    
    browser.get("https://fedoramagazine.org/")
    link = a[0]
        
    Tweet(posts[0] + "\n" + link)


# Logs in the browser
def prepTwitter(browser, user_name, password):
    browser.get("https://twitter.com/login")
    
    # Login
    userName = browser.find_element_by_class_name("js-username-field")
    pword = browser.find_element_by_class_name("js-password-field")
    userName.send_keys(user_name)
    pword.send_keys(password)
    pword.send_keys(Keys.RETURN)
    
    sendTweet(browser)


userName = input("Enter your Twitter UserName or Email >>> ")
password = getpass.getpass("Enter your Twitter Password >>> ")

opts = Options()
opts.headless = True
opts.add_argument('log-level=2')
assert opts.headless

browser = webdriver.Chrome(options=opts)

try:
    prepTwitter(browser, userName, password)
except:
    print('Error')

browser.close()
