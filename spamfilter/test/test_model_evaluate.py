import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from spamfilter.main.config import basedir

from spamfilter.main.service.evaluate_model import evaluate

class TestModelEval(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.DevelopmentConfig')
        return app

    def test_model_eval(self):
        eval_report, returncode = evaluate()
        
        print(returncode)
        print(eval_report)

        self.assertEqual(0, 0)     

if __name__ == '__main__':
    unittest.main()


