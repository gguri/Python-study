# headless options\n
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# disable image
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

# visible all log
caps = webdriver.DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

# driver = webdriver.Chrome('C:/Users/ff/Downloads/chromedriver', desired_capabilities=caps, chrome_options=options)
driver = webdriver.Chrome('/usr/bin/chromedriver', desired_capabilities=caps, chrome_options=options)

# log timeout
driver.set_page_load_timeout(20)
driver.set_script_timeout(20)