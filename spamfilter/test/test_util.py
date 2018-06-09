import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from spamfilter.main.config import basedir
from spamfilter.main.util.email_util import read_emails, get_clean_emails

class TestEmailUtil(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.DevelopmentConfig')
        return app

    def test_read_emails(self):
        emails, labels = read_emails()

        self.assertEqual(len(emails), 5172)
        self.assertEqual(len(labels), 5172)
        self.assertEqual(len(emails), len(labels))

    def test_clean_emails(self):
        emails, _ = read_emails()
        cleaned_email = get_clean_emails(emails)

        self.assertEqual(len(cleaned_email), 5172)


if __name__ == '__main__':
    unittest.main()


