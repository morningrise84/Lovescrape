from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import csv

# PREPARE .CSV TO STORE PROFILE LINKS #
exportcsv = open('Links.csv', 'w', newline='')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['Profile Link'])

# LOAD RESULT PAGE ON A PREVIOUSLY OPENED BROWSER WINDOW #
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome = r"""C:\Users\HP\Desktop\chromedriver.exe""" # ChromeDriver is needed, select here the folder where it is stored
driver = webdriver.Chrome(chrome, options=options)
load = driver.get('https://www.lovescout24.de/d/search/results')
driver.maximize_window()
time.sleep(3)

# SCROLL DOWN & DISPLAY MORE RESULTS #
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
seemore = driver.find_element_by_class_name('see-more-profiles-cta')
seemore.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
seemore = driver.find_element_by_class_name('see-more-profiles-cta')
seemore.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)

# RETRIEVE PROFILE LINKS #
links = driver.find_elements_by_xpath("//a[contains(@href, '/d/profile-display/')]")
for ii in links:
    print(ii.get_attribute('href'))

# EXPORT PROFILE LINKS TO .CSV #
    csvwriter.writerow([ii.get_attribute('href')])

exportcsv.close()

# REMOVE DUPLICATE ENTRIES #
df = pd.read_csv('Links.csv')
df.drop_duplicates(subset=None, inplace=True)
df.to_csv('Links.csv', index=False)