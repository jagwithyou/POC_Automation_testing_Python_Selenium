import os
BASE_DIRECTORY = os.getcwd()
BASE_URL = "https://www.google.com"

#DRIVER
DRIVER_PATH = os.path.join(BASE_DIRECTORY, 'drivers') #use os.path.join to create a path
WEB_DRIVER_WAIT = 120
HEADLESS = True
ACTION_DELAY = 2
DOWNLOAD_WAIT_TIME = 60
DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY,'media','download')

#Reporting
REPORT_TITLE = "Google Search Testing"
REPORT_FOLDER = os.path.join(BASE_DIRECTORY, 'reports')
INDIVIDUAL_REPORT = False
LOG_FOLDER = os.path.join(BASE_DIRECTORY, 'logs')

