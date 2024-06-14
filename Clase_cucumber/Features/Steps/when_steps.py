from behave import when
from Lib.pages.home_page import HomePage

@when('I search for "{keyword}"')
def step_search_for_facebook(context, keyword):
    context.home_page.search_for(keyword)
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()

