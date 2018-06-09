import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from spamfilter import TEST_VAR as tv

from spamfilter import blueprint


from spamfilter.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app)

@manager.command
def run():
    app.run()

@manager.command
def test_all():
    """Runs all unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1

@manager.command
def test_config():
    """Runs all unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_config*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1

@manager.command
def test_util():
    """Runs email utility unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_util*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1

@manager.command
def test_model():
    """Runs email utility unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_model*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1

@manager.command
def test_model_evaluate():
    """Runs email utility unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_model_evaluate*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 
    
@manager.command
def test_model_training():
    """Runs email utility unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_model_training*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1


@manager.command
def test_model_predict():
    """Runs email utility unit tests"""
    tests = unittest.TestLoader().discover('spamfilter/test', pattern = 'test_model_predict*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)

    if result.wasSuccessful():
        return 0
    
    return 1


if __name__ == '__main__':
    manager.run()


