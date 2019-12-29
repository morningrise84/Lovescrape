from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

# PREPARE .CSV TO STORE PROFILE DETAILS #
exportcsv = open('Profiles.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['ID', 'Nickname', 'Age', 'City', 'Last Login', 'Intro', 'Readiness', 'Status', 'Has Kids', 'Wants Kids', 'Height', 'Figure', 'Zodiac Sign', 'Smoker', 'Marriage', 'Languages', 'Desired Minimum Age', 'Desired Maximum Age', 'Desired Minimum Height', 'Desired Maximum Height','Does he want kids','Profile Link'])

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

        try:
            nickname = driver.find_element_by_class_name("profile-infos__nickname").text
        except Exception as e:
            nickname = 'N/A'

        try:
            agecity = driver.find_element_by_class_name("profile-infos__age-city").text
            age = agecity.split(',')[0]
            age = age.replace(' Jahre alt', '')
            city = agecity.split(',')[1]
            city = city.replace(' ', '')
        except Exception as e:
            age = 'N/A'
            city = 'N/A'

        try:
            lastlogin = driver.find_element_by_class_name("last-connection-date").text
        except Exception as e:
            lastlogin = 'N/A'

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

        try:
            desiredpartner = driver.find_element_by_link_text('Ich suche')
            desiredpartner.click()
        except Exception as e:
            pass

        try:
            desiredageQ = driver.find_element_by_xpath("//*[contains(text(), 'Sein Alter')]")
            desiredageA = desiredageQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            minimumage = desiredageA.split(' bis ')[0]
            minimumage = minimumage.replace('von ', '')
            maximumage = desiredageA.split(' bis ')[1]
            maximumage = maximumage.replace(' Jahre', '')
        except Exception as e:
            minimumage = 'N/A'
            maximumage = 'N/A'

        try:
            desiredheightQ = driver.find_element_by_xpath("//*[contains(text(), 'Seine Größe')]")
            desiredheightA = desiredheightQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
            minimumheight = desiredheightA.split(' bis ')[0]
            minimumheight = minimumheight.replace('von ', '')
            maximumheight = desiredheightA.split(' bis ')[1]
            maximumheight = maximumheight.replace(' cm', '')
        except Exception as e:
            minimumheight = 'N/A'
            maximumheight = 'N/A'

        try:
            desiredkidsQ = driver.find_element_by_xpath("//*[contains(text(), 'sich Kinder')]")
            desiredkidsA = desiredkidsQ.find_element_by_xpath("following-sibling::div").get_attribute('innerHTML')
        except Exception as e:
            desiredkidsA = 'N/A'

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
        print(minimumage)
        print(maximumage)
        print(minimumheight)
        print(maximumheight)
        print(desiredkidsA)
        print(link)

        # EXPORT PROFILE DETAILS TO .CSV #
        csvwriter.writerow([ID, nickname, age, city, lastlogin, intro, readinessA, statusA, haskidsA, wantskidsA, heightA, figureA, zodiacsignA, smokerA, marriageA, languagesA, minimumage, maximumage, minimumheight, maximumheight, desiredkidsA, link])

if __name__ == '__main__':
    with open ('Links.csv') as url_obj:
        csv_url_reader(url_obj)

exportcsv.close()

driver.close()
