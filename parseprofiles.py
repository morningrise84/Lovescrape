from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

# PREPARE .CSV TO STORE PROFILE DETAILS #
exportcsv = open('Profiles.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['ID', 'Nickname', 'Age', 'City', 'Last Login', 'Intro', 'Readiness', 'Status', 'Has Kids', 'Wants Kids', 'Height', 'Figure', 'Zodiac Sign', 'Smoker', 'Marriage', 'Languages', 'Profile Link'])

# LOAD PROFILE LINKS ON A PREVIOUSLY OPENED BROWSER WINDOW #
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome = r"""C:\Users\HP\Desktop\chromedriver.exe""" # ChromeDriver is needed, select here the folder where it is stored
driver = webdriver.Chrome(chrome, options=options)
driver.maximize_window()
time.sleep(2)

def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj, delimiter = ',')
    for line in reader:
        url = line['Profile Link']
        driver.get(url)
        time.sleep(5)

# PARSE DATA #
        link = driver.current_url
        ID = link.split('/')[5]
        ID = ID.split('?')[0]
        nickname = driver.find_element_by_class_name("profile-infos__nickname").text
        agecity = driver.find_element_by_class_name("profile-infos__age-city").text
        age = agecity.split(',')[0]
        age = age.replace(' Jahre alt', '')
        city = agecity.split(',')[1]
        city = city.replace(' ', '')
        lastlogin = driver.find_element_by_class_name("last-connection-date").text

        try:
            intro = driver.find_element_by_class_name("profile-essay__text ").text
            intro = intro.split('\n')[0]
        except Exception as e:
            intro = 'N/A'

        try:
            readinessQ = driver.find_element_by_xpath("//*[contains(text(), 'Beziehung')]")
            readinessA = readinessQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            readinessA = 'N/A'

        try:
            statusQ = driver.find_element_by_xpath("//*[contains(text(), 'Familienstand')]")
            statusA = statusQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            statusA = 'N/A'

        try:
            haskidsQ = driver.find_element_by_xpath("//*[contains(text(), 'habe Kinder')]")
            haskidsA = haskidsQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            haskidsA = 'N/A'

        try:
            wantskidsQ = driver.find_element_by_xpath("//*[contains(text(), 'möchte Kinder')]")
            wantskidsA = wantskidsQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            wantskidsA = 'N/A'

        try:
            heightQ = driver.find_element_by_xpath("//*[contains(text(), 'Größe')]")
            heightA = heightQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            heightA = heightA.replace(' cm', '')
        except Exception as e:
            heightA = 'N/A'

        try:
            figureQ = driver.find_element_by_xpath("//*[contains(text(), 'Statur')]")
            figureA = figureQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            figureA = 'N/A'

        try:
            zodiacsignQ = driver.find_element_by_xpath("//*[contains(text(), 'Sternzeichen')]")
            zodiacsignA = zodiacsignQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            zodiacsignA = 'N/A'

        try:
            smokerQ = driver.find_element_by_xpath("//*[contains(text(), 'Raucher')]")
            smokerA = smokerQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            smokerA = 'N/A'

        try:
            marriageQ = driver.find_element_by_xpath("//*[contains(text(), 'Ehe ist für mich')]")
            marriageA = marriageQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            marriageA = 'N/A'

        try:
            languagesQ = driver.find_element_by_xpath("//*[contains(text(), 'spreche')]")
            languagesA = languagesQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            languagesA = 'N/A'

        print(ID)
        print(nickname)
        print(age)
        print(city)
        print(lastlogin)
        print(intro)
        print(readinessA)
        print(statusA)
        print(haskidsA)
        print(wantskidsA)
        print(heightA)
        print(figureA)
        print(zodiacsignA)
        print(smokerA)
        print(marriageA)
        print(languagesA)
        print(link)

        # EXPORT PROFILE DETAILS TO .CSV #
        csvwriter.writerow([ID, nickname, age, city, lastlogin, intro, readinessA, statusA, haskidsA, wantskidsA, heightA, figureA, zodiacsignA, smokerA, marriageA, languagesA, link])

if __name__ == '__main__':
    with open ('Links.csv') as url_obj:
        csv_url_reader(url_obj)

exportcsv.close()

driver.close()
