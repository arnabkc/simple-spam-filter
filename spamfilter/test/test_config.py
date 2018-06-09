import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from spamfilter.main.config import basedir
from spamfilter.main.util.email_util import read_emails, get_clean_emails

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['CONFIG_TYPE'] is 'Dev')
        self.assertTrue(app.config['DEBUG'] is True)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.TestConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['CONFIG_TYPE'] is 'Test')
        self.assertTrue(app.config['DEBUG'] is True)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['CONFIG_TYPE'] is 'Prod')
        self.assertTrue(app.config['DEBUG'] is False)



if __name__ == '__main__':
    unittest.main()


