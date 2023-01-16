import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a utility class for fixture optimisation
# Inherit this class into test method class
# It is for removing fixture redundant code


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifySearchBoxPresence(self, name):

        wait = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_locatepresence_of_element_locatedd((By.ID, name))
        )

    def verifyLinkPresence(self, link_name):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_name))
        )

    def selectOptionByText(self, locator, text):
        dropdown_option = Select(locator)
        dropdown_option.select_by_visible_text(text)


