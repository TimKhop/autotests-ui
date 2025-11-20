from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state_courses.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state_courses.json')
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    text_name_head = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(text_name_head).to_be_visible()
    expect(text_name_head).to_have_text('Courses')

    icon_directory = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_directory).to_be_visible()

    text_result_final = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_result_final).to_be_visible()
    expect(text_result_final).to_have_text('There is no results')

    text_result = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_result).to_be_visible()
    expect(text_result).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)