import os
import unittest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class simpleAndroidTests(unittest.TestCase):
    def setUp(self):
        d_caps = {}
        d_caps["app"] = '/Users/gevans/development/DelawareNorth/app-debug.apk'
        d_caps["platformName"] = 'android'
        d_caps["appium:automationName"] = 'uiautomator2'
        d_caps["udid"] = 'G000NS05904404RJ'
        self.driver = webdriver.Remote('http://127.0.0.1:44800/wd/hub', desired_capabilities = d_caps )

    def tearDown(self):
        self.driver.quit()

    def testOne(self):
        time.sleep(6)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(simpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
