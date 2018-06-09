import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    CONFIG_DICT = {
        'spam_directory' : '/Users/semba/SACON2018/app/data/email/enron1/spam',
        'ham_directory' : '/Users/semba/SACON2018/app/data/email/enron1/ham',
        'model_file' : './temp/spam-filter-nb.mdl',
        'vectorizer_file' : './temp/spam-filter-tfidf-verctorizer.vect'
    }
    
    FINAL_MODEL = {
        'max_features' : 8000,
        'smoothing_factor' : 2.0,
        'fit_prior' : True
    }

    CONFIG_TYPE = 'Dev'
    # TEST_ARR = {'id':'1'}

class DevelopmentConfig(Config):
    DEBUG = True
    # CONFIG_TYPE = 'Dev'

class TestConfig(Config):
    DEBUG = True
    CONFIG_TYPE = 'Test'


class ProductionConfig(Config):
    DEBUG = False
    CONFIG_TYPE = 'Prod'

config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestConfig,
    prod = ProductionConfig
)