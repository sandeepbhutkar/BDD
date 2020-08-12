from behave import given,when,then
# OR from behave import *, it will import all.
from selenium import webdriver

@given('launch chrome browser')
def LaunchBrowser(context):
    global driver
    context.driver=webdriver.Chrome()

@when('open orage hrm homepage')
def HRMHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo present on page')
def VerifyLogo(context):
    context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()

@then('close browser')
def CloseBrowser(context):
    context.driver.quit()

