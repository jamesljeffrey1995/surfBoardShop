import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Product, Orders, Order_line
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('SURF_URI'),
                SECRET_KEY=getenv('MY_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
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

        db.session.remove()
        db.drop_all()

class TestLogin(TestBase):
    def loginTest(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)

        res2 = self.client.get(url_for('home'))

        self.assertEqual(res2.status_code, 200)

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


    def test_homepage_view(self):
        """
        Test that about is accessible without login
        """
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """
        Test that register page is accessible without login
        """
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_shop(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)

        res2 = self.client.get(url_for('user_shop'))

        self.assertEqual(res2.status_code, 200)
    
    def test_submit_board(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)

        res2 = self.client.get(url_for('submit_board'))

        self.assertEqual(res2.status_code, 200)
    
    
    def test_registration_logged_in(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)
    
        target_url = url_for('register')
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
    
    
    def test_submit_board_no_login(self):
        res2 = self.client.get(url_for('submit_board'))

        self.assertEqual(res2.status_code, 302)


    def test_register_page(self):
        """ Testing register page is responsive"""

        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_product(self):
        response = self.client.get(url_for('product',productItem = 1))
        self.assertEqual(response.status_code, 302)

    def test_product_view_logged_in(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)
        response = self.client.get(url_for('product',productItem = 1))
        self.assertEqual(response.status_code, 200)
    
    def test_login_view_logged_in(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_board_update_logged_in(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)
        response = self.client.get(url_for('update_board', productItem = 1))
        self.assertEqual(response.status_code, 200)

class TestSubmitBoard(TestBase):
    def test_add_a_product(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        with self.client:
            self.assertEqual(res1.status_code, 200)
            res2 = self.client.post("/submit_board", 
                    data=dict(name="testerBoard", style="Fish", volume=55.0, size=9.0, price=500, stock=10, user_id=1),
                    follow_redirects=True
                    )
            self.assertIn(b'testerBoard',res2.data)
                
    def test_add_a_user(self):
         with self.client:
            response = self.client.post(
                '/register',
                data=dict(
                    first_name = "Tester",
                    last_name = "Tester",
                    password= "Test",
                    email = "Test@Email.com"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Tester', response.data)
