from selenium.webdriver.common.by import By
from pageObjects.shopPage import ShopPage
from utilities.baseClass import BaseClass


class TestEndToEnd(BaseClass):
    def test_end_to_end(self):
        shop_page = ShopPage(self.driver)
        shop_page.get_add_to_cart().click()
        shop_page.get_cart_button().click()
        shop_page.get_view_button().click()
        self.driver.find_element(By.XPATH, "//a[@aria-label='Add a coupon' ]").click()
        self.driver.find_element(By.ID, "wc-block-components-totals-coupon__input-0").send_keys("Tojtech-10$")
        self.driver.find_element(By.XPATH, "//span[text ()= 'Apply'] ").cLick()
        self.driver.find_element(By.XPATH, "//span[text()='Proceed to Checkout']").cLick()
        self.driver.find_element(By.CSS_SELECTOR, "#components-form-token-input-0").send_keys("Uni")
        list_of_countries = self.driver.find_elements(By.CSS_SELECTOR, ".components-form-token-field__suggestion")
        for country in list_of_countries:
            if country.text == "United Kingdom (UK)":
                country.click()
                break

        frame_element = self.driver.find_elements(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(frame_element[1])
        self.driver.find_element(By.CSS_SELECTOR, "#Field-numberInput").send_keys("4242424242424242")
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "//span[text()='Place Order']").click()