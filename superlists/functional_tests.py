from selenium import webdriver

# no proxy
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 0)
profile.update_preferences()

browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title