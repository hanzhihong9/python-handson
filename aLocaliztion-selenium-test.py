#!/usr/bin/python
# coding=utf-8


##  coding=utf-8 is important , because there  are unicode string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import unittest, time, re
import ConfigParser, getopt, os, subprocess, sys
import datetime
import random


from onesna_testing_utils.config import ConfigSectionMap

'''
 change the browser language and check the login page is translated or not
'''

# Please add more if has new language supported
g_supported_locale = [ 
                        'de_DE',
                         'en',
                         'es_ES',
                         'es_LA',
                         'fr_FR',
                         'fr_CA',
                         'it_IT',
                         'ja',
                         'ko_KR',
                         'pt_BR',
                         'ru',
                         'zh_CN',
                         'zh_HK'
                         ]

url = ConfigSectionMap("Testing_URL")['testing_site']
url_login  = url + '/account/login'
onusing_browser = ConfigSectionMap("Browser")['onusing']

class Login_page_localization(unittest.TestCase):
    def setUp(self):
        print ' change the browser language and check the login page is translated or not'

        if onusing_browser == "1":

            this_dir, this_filename = os.path.split(__file__)
            geckodriver_path = os.path.join(this_dir, "../")
            os.environ["PATH"] += os.pathsep + geckodriver_path
            #geckodriver_path = os.path.join(this_dir, "../geckodriver")
            geckodriver_path = os.path.join(this_dir, "../")
            sys.path.append(geckodriver_path)


        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        pass

    def formatLocale(self, language):
        if isinstance(language, unicode):
            language = language.encode('utf8')

        p = language.find(b'_')
        if p >= 0:
            return language[:p].lower()+b'-'+language[p+1:].lower()
        else:
            return language.lower()

    def check_login_page_by_language(self, language):

        if onusing_browser == "1":
            firefoxProfile = FirefoxProfile()
            firefoxProfile.set_preference( "intl.accept_languages", language )
            self.driver = webdriver.Firefox(firefox_profile = firefoxProfile)

        elif onusing_browser == "2":
            options = ChromeOptions()
            options.add_argument("--lang=" + language)
            options.add_argument("--window-size=1920,1080")
            self.driver = webdriver.Chrome(chrome_options=options)

        elif onusing_browser == "3":

            self.assertTrue(False, " Do not use IE, Cannot set IE browser language" )
        else:
            print "We don't support other browsers currently."

        self.driver.get(url_login)
        self.driver.implicitly_wait(15)
        self.check_login_page_UI_by_language(language)
        time.sleep(3)
        self.driver.close()
        time.sleep(1)
        if self.driver and onusing_browser != "1":
            self.driver.quit()

    def check_login_page_UI_by_language(self, language):
        getStartedBtn = self.driver.find_element_by_xpath("//button[@id='GetStartedBtn']")
        text = getStartedBtn.text
        '''
        'de_DE',
                         'en',
                         'es_ES',
                         'es_LA',
                         'fr_FR',
                         'fr_CA',
                         'it_IT',
                         'ja',
                         'ko_KR',
                         'pt_BR',
                         'ru',
                         'zh_CN',
                         'zh_HK'
        '''
        if language == b'en':
            self.assertEqual( text, u'Get Started' , msg=unicode(language) + u' '+ unicode(text) +u' should show Get Started')
        elif language.startswith(b'de'):
            self.assertEqual( text, u'Los geht\'s' , msg=unicode(language) + u' '+ unicode(text) +u' should show Los geht\'s')
        elif language.startswith(b'es_es'):
            self.assertEqual( text, u'Comencemos' , msg=unicode(language) + u' '+ unicode(text) +u' should show Comencemos')
        elif language.startswith(b'es_la'):
            self.assertEqual( text, u'Comencemos' , msg=unicode(language) + u' '+ unicode(text) +u' should show Comencemos')
        elif language.startswith(b'fr_fr'):
            self.assertEqual( text, u'Commencer' , msg=unicode(language) + u' '+ unicode(text) +u' should show Commencer')
        elif language.startswith(b'fr_ca'):
            self.assertEqual( text, ur'Démarrer' , msg=language + u' '+ unicode(text) +ur' should show Démarrer')
            pass
        elif language.startswith(b'it_it'):
            self.assertEqual( text, u'Inizia' , msg=unicode(language) + u' '+ unicode(text) +u' should show Inizia')
        elif language.startswith(b'ko_kr'):
            self.assertEqual( text, ur'시작하기' , msg=unicode(language) + u' '+ unicode(text) +u' should show 시작하기')
        elif language.startswith(b'js'):
            self.assertEqual( text, ur'開始' , msg=unicode(language) + u' '+ unicode(text) +u' should show 開始')
        elif language.startswith(b'pt_br'):
            self.assertEqual( text, u'Iniciar' , msg=unicode(language) + u' '+ unicode(text) +u' should show Iniciar')
        elif language.startswith(b'ru'):
            self.assertEqual( text, u'Начало работы' , msg=unicode(language) +u' ' +unicode(text) +u' should show Начало работы')
        elif language.startswith(b'zh_cn'):
            self.assertEqual( text, u'开始使用' , msg=unicode(language) + u' '+ unicode(text) +u' should show 开始使用')
        elif language.startswith(b'zh-hk'):
            self.assertEqual( text, u'準備開始' ,msg= (unicode(language) + u' '+ unicode(text) +u' should show 準備開始') )
        pass

    def test_login_page(self):
        for aLanguage in g_supported_locale :
            aLanguagef = self.formatLocale(aLanguage)
            self.assertTrue(isinstance(aLanguagef, str),  'we need string not uicod' )

            self.check_login_page_by_language(aLanguagef)





if __name__ == '__main__':
     unittest.main()
