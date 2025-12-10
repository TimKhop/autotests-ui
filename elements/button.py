from elements.base_element import BaseElement
from playwright.sync_api import expect


class Button(BaseElement):
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to.be.enabled()

    def check_disabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to.be.disabled()