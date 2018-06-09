from spamfilter.main.model.machine_learning.bayesian.naive_baysian import predict

from manage import app

def is_spam(email_list):
    model_file = app.config['CONFIG_DICT']['model_file']
    vectorizer_file = app.config['CONFIG_DICT']['vectorizer_file']

    predicted_value = predict(email_list, model_file, vectorizer_file)

    ham_spam = ['Ham', 'Spam']

    predicted_list = predicted_value['prediction']

    predicted_labels = []

    for predicted_label in predicted_list:
        predicted_labels.append(ham_spam[predicted_label])

    return predicted_labels, 201
