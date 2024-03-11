# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestWarsztatrejestracjafailed():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_warsztatrejestracjafailed(self):
    self.driver.get("http://127.0.0.1:8000/home/")
    self.driver.set_window_size(1384, 780)
    self.driver.find_element(By.CSS_SELECTOR, ".tile1:nth-child(2) .icon-user").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("test")
    self.driver.find_element(By.ID, "id_first_name").click()
    self.driver.find_element(By.ID, "id_first_name").send_keys("test")
    self.driver.find_element(By.ID, "id_last_name").click()
    self.driver.find_element(By.ID, "id_last_name").send_keys("test")
    self.driver.find_element(By.ID, "id_email").click()
    self.driver.find_element(By.ID, "id_email").send_keys("asd@gmail.com")
    self.driver.find_element(By.ID, "id_password1").click()
    self.driver.find_element(By.ID, "id_password1").send_keys("test1234")
    self.driver.find_element(By.ID, "id_password2").send_keys("test1234")
    self.driver.find_element(By.ID, "id_password2").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "id_password1").click()
    self.driver.find_element(By.ID, "id_password1").send_keys("Test1234")
    self.driver.find_element(By.ID, "id_password2").send_keys("Test1234")
    self.driver.find_element(By.ID, "id_password2").send_keys(Keys.ENTER)
    assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) li:nth-child(1)").text == "To hasło jest zbyt powszechne."
    self.driver.find_element(By.ID, "id_password1").click()
    self.driver.find_element(By.ID, "id_password1").send_keys("12345678")
    self.driver.find_element(By.ID, "id_password2").click()
    self.driver.find_element(By.ID, "id_password2").send_keys("12345678")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorlist > li:nth-child(2)").text == "Hasło składa się wyłącznie z cyfr."
  