import pytest
import re as re
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGISTRATION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourse:
    @allure.title("Check displaying of empty course list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.check_visible_empty_view()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible('username')

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course.check_visible(title="", description="", estimated_time="", max_score="0",
                                                       min_score="0")
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course.fill(title="Playwright", estimated_time="2 weeks", description="Playwright",
                                              max_score="100", min_score="10")
        create_course_page.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title="Playwright", max_score="100", min_score="10",
                                                    estimated_time="2 weeks")

    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score='10'
        )
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/picture.png')
        create_course_page.click_create_course_button()
        courses_list_page.check_current_url(re.compile('#/courses'))
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course.fill(
            title="Python", estimated_time="1 weeks", description="Playwright", max_score="10", min_score='1'
        )
        create_course_page.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0, title="Python", max_score="10", min_score="1", estimated_time="1 weeks"
        )