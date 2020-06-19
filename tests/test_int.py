import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users, Product, Orders, Order_line
from datetime import datetime
from flask_login import login_user, current_user

test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

test_admin_name="admin board"
test_admin_volume=55.0
test_admin_size=9.0
test_admin_price=500.0
test_admin_style="fish"
test_admin_stock=10

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('SURF_URI'))
        app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/jamesljeffrey1995/surfBoardShop/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

        testUser= Users(first_name="test", last_name="user", email="test@test.com", password=(bcrypt.generate_password_hash("test")))
        db.session.add(testUser)
        testProduct=Product(name="testBoard", style="Fish", volume=55.0, size=9.0, price=500, stock=10, user_id=1)
        db.session.add(testProduct)
        testOrder=Orders(user_id=1)
        db.session.add(testOrder)
        theOrder = Orders.query.order_by(Orders.id.desc()).first()
        testOrder_line=Order_line(order_id=theOrder.id,product_id=1,quantity=10,total=2500)
        db.session.add(testOrder_line)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestRegistration(TestBase):

    def test_registration(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be
        redirected to the login page
        """

        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)

        # Fill in registration form
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to login page
        assert url_for('login') in self.driver.current_url

class TestLogin(TestBase):
    def test_login(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@test.com')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('test')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url
    
if __name__ == '__main__':
    unittest.main(port=5000)        
