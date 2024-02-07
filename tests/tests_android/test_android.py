import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_android_search_wiki_Appium_local(context):
    print(context)
    if context == 'bs':
        pytest.skip()

    with step('Skip first screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text('New ways to explore'))

    with step('Skip second screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text('Reading lists with sync'))

    with step('Skip second screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text('Data & Privacy'))

    with step('Click on Get started'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
        browser.element((AppiumBy.CSS_SELECTOR, "android.widget.TextView")) \
            .should(have.text('Search Wikipedia'))

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

@pytest.mark.bs
def test_android_search_wiki_Appium_bstack(context):

    if context == 'local':
        pytest.skip()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
