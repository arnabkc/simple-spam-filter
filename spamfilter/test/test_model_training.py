import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from spamfilter.main.config import basedir

from spamfilter.main.service.train_model import train

class TestModelTrain(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.DevelopmentConfig')
        return app

    def test_model_train(self):
        returnvalue, returncode = train()

        print(returncode)
        print(returnvalue)
        
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()


