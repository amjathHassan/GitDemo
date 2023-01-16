from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

driver = None

def pytest_addoption(parser):

    # command line options for pytest
    # selecting browser in terminal command
    # Uses key-value pair

    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    parser.addoption(
        "--URL", action="store", default="https://"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # use request instance to return back driver object
    # create driver variable in that class
    # browser invoke setup
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        service_obj = Service("/home/amjathhassan/Desktop/selenium_web_driver/chromedriver_linux64/chromedriver")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == 'firefox':
        # firefox invocation
        service_obj = Service("/home/amjathhassan/Desktop/selenium_web_driver/geckodriver-v0.32.0-linux64/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == 'ie':
        # IE invocation
        pass

    driver.implicitly_wait(4)
    url = request.config.getoption("URL")
    driver.get(f"{url}rahulshettyacademy.com/angularpractice/")
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="../tests/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

