from spamfilter.main.model.machine_learning.bayesian.naive_baysian import eval_model
from spamfilter.main.util.email_util import read_emails, get_clean_emails

from manage import app

def evaluate():
    spam_directory = app.config['CONFIG_DICT']['spam_directory']    
    ham_directory = app.config['CONFIG_DICT']['ham_directory']   

    # Read email samples 
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
    print('>> Evaluating model......')
    eval_report = eval_model(emails, labels)

    return eval_report, 201

    