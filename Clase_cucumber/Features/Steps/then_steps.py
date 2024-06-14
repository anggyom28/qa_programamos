from behave import then
from selenium.webdriver.common.by import By


@then('I should see "{expected_text}" in the results')
def step_verify_search_results(context, expected_text):
    search_results = context.driver.find_elements(By.XPATH, "//h3[@class='LC20lb']")
    found = False
    for result in search_results:
        if expected_text in result.text:
            found = True
            break
    assert found, f"Expected text '{expected_text}' not found in search results."
from behave import when