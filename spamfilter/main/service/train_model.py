from spamfilter.main.model.machine_learning.bayesian.naive_baysian import train_model
from spamfilter.main.util.email_util import read_emails, get_clean_emails

from manage import app

def train():
    spam_directory = app.config['CONFIG_DICT']['spam_directory']
    ham_directory = app.config['CONFIG_DICT']['ham_directory']

    print(' ')
    print('>> Reading email samples.....')

    emails, labels = read_emails({
        'spam_file_location' : spam_directory,
        'ham_file_location' : ham_directory
    })

    print('>>>> Number of emails: {0} :: Number of labels: {1}'.format(len(emails), len(labels)))

    # Clean emails - stopword removal, lemmatization, name entity removal
    print(' ')
    print('>> Cleaning emails.......')

    cleaned_emails = get_clean_emails(emails)

    print('>>>> Number of cleaned emails: {0}'.format(len(cleaned_emails)))

    # Now, train the model
    print(' ')
    print('>> Training model......')
    # The following hyper parameters are found from model selection exercise. These parameters gave 
    # the best result (99.44%)

    model_hyper_param_dict = {}

    model_hyper_param_dict['max_features'] = app.config['FINAL_MODEL']['max_features']         # 8000
    model_hyper_param_dict['smoothing_factor'] = app.config['FINAL_MODEL']['smoothing_factor'] # 2.0
    model_hyper_param_dict['fit_prior'] = app.config['FINAL_MODEL']['fit_prior']               # True

    # File names for persistence
    model_file = app.config['CONFIG_DICT']['model_file']            # 'spam-filter-nb.mdl'
    vectorizer_file = app.config['CONFIG_DICT']['vectorizer_file']  # 'spam-filter-tfidf-verctorizer.vect'

    # Now, train the model
    train_model(emails, labels, model_hyper_param_dict, model_file, vectorizer_file)

    print(' ')
    print('>> Training complete')

    return 'Training complete', 201