# Creating conftest.py file to help reduce duplication, logging, screenshot ect.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='edge':
        driver = webdriver.Edge()
        print("Launching edge browser.........")
    else:
        driver = driver=webdriver.Chrome()
    return driver
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Login Page'
        config.stash[metadata_key]['Tester'] = 'Dalila'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)