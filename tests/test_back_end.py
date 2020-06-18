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

class TestProduct(TestBase):
    def productTesting(self):
        res1 = self.client.post(
                '/login',
                data=dict(
                    email="test@test.com",
                    password="test"
                    ),
                follow_redirects=True
                )
        self.assertEqual(res1.status_code, 200)

        res2 = self.client.get(url_for('post'))

        self.assertEqual(res2.status_code, 200)

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):

    def test_add_new_post(self):
        """
        Test that when I add a new post, I am redirected to the homepage with the new post visible
        """
        with self.client:
            response = self.client.post(
                '/post',
                data=dict(
                    name="Test Title",
                    style="Test Content"

                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)
