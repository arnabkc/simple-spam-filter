from nltk.corpus import names
from nltk.stem import WordNetLemmatizer

import glob
import os

from manage import app

def read_emails(email_file_location_dict):
    e_mails, labels = [], []

    spam_directory = email_file_location_dict['spam_file_location']
    ham_directory = email_file_location_dict['ham_file_location']

    # print('CONFIG_DICT: {0}'.format(app.config['CONFIG_DICT']))

    # spam_directory = app.config['CONFIG_DICT']['spam_directory']    
    # ham_directory = app.config['CONFIG_DICT']['ham_directory']   

    # print('>> Reading emails from {0}'.format(spam_directory)) 

    for file_name in glob.glob(os.path.join(spam_directory, '*.txt')):
        with open(file_name, 'r', encoding = 'ISO-8859-1') as in_file:
            e_mails.append(in_file.read())
            labels.append(1)

    # print('>> Reading emails from {0}'.format(ham_directory)) 

    for file_name in glob.glob(os.path.join(ham_directory, '*.txt')):
        with open(file_name, 'r', encoding = 'ISO-8859-1') as in_file:
            e_mails.append(in_file.read())
            labels.append(0)
    
    return e_mails, labels

# ********************************
def clean_text(docs):
    all_names = set(names.words())
    lemmatizer = WordNetLemmatizer()

    cleaned_docs = []
    for doc in docs:
        cleaned_docs.append(' '.join([lemmatizer.lemmatize(word.lower())
                                        for word in doc.split()
                                        if word.isalpha()
                                        and word not in all_names]))
    return cleaned_docs

# ********************************
def get_clean_emails(e_mails):
    return clean_text(e_mails)

