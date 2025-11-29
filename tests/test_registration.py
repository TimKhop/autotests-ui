import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.email_input.fill('user.name@gmail.com')
    registration_page.username_input.fill('username')
    registration_page.password_input.fill('password')
    registration_page.registration_button.click()
    dashboard_page.check_visible_dashboard_title()