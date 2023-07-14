# Lovescrape
A semi-automated approach to scrape user information from a popular German dating site. Use at your own risk.

## Status
Currently (December 2019) this solution works like a charm. Should the site change, the scripts might need to be updated accordingly.
I will not maintain the code in the future: feel free step in as a maintainer.

## Prerequisites
These scripts take advantage of the Chrome DevTools Protocol to connect Selenium/Chromedriver to an already opened Chrome window (special thanks to S. Ansari for the insights).
This allows us to bypass the CAPTCHA we would otherwise encounter immediately after logging in (using a fully automated approach).

To make sure everything works fine you will need to:
- Have Chromedriver stored somewhere, locally
- Define Chromedriver's path in both scripts
- Add Chrome to PATH (don't know how? Google is your friend!)
- Launch Chrome from command line using custom flags: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\Automation"

## Usage
Please make sure the prerequisites are met before moving forward with the following steps: 
1) Manually login to lovescout24 with the browser opened via command line
2) If prompted, complete all CAPTCHAs
3) Navigate to the search page and refine the search criteria as desired
4) Run retrieveurls.py: this connects Chromedriver to the already opened browser and converts your search results into a list of URLs, stored in a .csv file
5) Run parseprofiles.py: this crawls the URLs and parse the user information from each profile

At this point you'll have the user details in a separate .csv file for you to analyse the data, load them into a target system or do whatever you feel like.

For each profile the following information will be stored (of course, if available in the profile):

- ID (for later reference; also useful to load profile information into a target system)
- Nickname
- Age
- City
- Last login
- Intro (this is the first line of a short introduction, many users leave it empty though)
- Readiness (availability for a relationship)
- Status (single, etc.)
- Has kids
- Wants kids
- Height
- Figure
- Zodiac sign
- Smoker
- Marriage (important, not important, etc.)
- Spoken languages
- Desired Minimum Age (of a potential partner)
- Desired Maximum Age (of a potential partner)
- Desired Minimum Height (of a potential partner)
- Desired Maximum Height (of a potential partner)
- Does the potential partner want kids
- Link to the full profile
