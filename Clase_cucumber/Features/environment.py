from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    
def after_sceneario(context, scenario):
    context.driver.quit()
    