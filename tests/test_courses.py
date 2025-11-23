from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        text_name_head = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(text_name_head).to_be_visible()
        expect(text_name_head).to_have_text('Courses')

        icon_directory = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_directory).to_be_visible()

        text_result_final = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_result_final).to_be_visible()
        expect(text_result_final).to_have_text('There is no results')

        text_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(text_result).to_be_visible()
        expect(text_result).to_have_text('Results from the load test pipeline will be displayed here')