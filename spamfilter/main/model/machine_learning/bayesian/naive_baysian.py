from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
    
import numpy as np
import glob
import pickle
import json

'''
    eval_model

    params: 

    Function to evaluate the naive bayes model performance
'''
def eval_model(cleaned_emails, labels):
    
    k = 10
    k_fold = StratifiedKFold(n_splits=k)

    # convert to numpy array for more efficient slicing
    cleaned_emails_np = np.array(cleaned_emails)
    labels_np = np.array(labels)

    max_features_option = [2000, 4000, 8000]
    smoothing_factor_option = [0.5, 1.0, 1.5, 2.0]
    fit_prior_option = [True, False]
    auc_record = {}

    for train_indices, test_indices in k_fold.split(cleaned_emails, labels):
        X_train, X_test = cleaned_emails_np[train_indices], cleaned_emails_np[test_indices]
        Y_train, Y_test = labels_np[train_indices], labels_np[test_indices]

        for max_features in max_features_option:

            if max_features not in auc_record:
                auc_record[max_features] = {}

            # cv = CountVectorizer(stop_words="english", max_features=max_features)
            cv = TfidfVectorizer(stop_words="english", max_features=max_features)

            term_docs_train = cv.fit_transform(X_train)
            term_docs_test = cv.transform(X_test)

            for smoothing_factor in smoothing_factor_option:

                if smoothing_factor not in auc_record[max_features]:
                    auc_record[max_features][smoothing_factor] = {}

                for fit_prior in fit_prior_option:
                    clf = MultinomialNB(alpha=smoothing_factor, fit_prior=fit_prior)

                    clf.fit(term_docs_train, Y_train)

                    prediction_prob = clf.predict_proba(term_docs_test)

                    pos_prob = prediction_prob[:, 1]

                    auc = roc_auc_score(Y_test, pos_prob)

                    temp_auc = auc + auc_record[max_features][smoothing_factor].get(fit_prior, 0.0)
                    
                    auc_record[max_features][smoothing_factor][fit_prior] = temp_auc

    report_dict = {}
    report_col_dict = {}
    report_row_list = []

    # print('max features  smoothing  fit prior  auc')
    for max_features, max_feature_record in auc_record.items():
        for smoothing, smoothing_record in max_feature_record.items():
            for fit_prior, auc in smoothing_record.items():

                report_col_dict['max_features'] = max_features
                report_col_dict['smoothing'] = smoothing
                report_col_dict['fit_prior'] = fit_prior
                report_col_dict['auc'] = auc / k

                report_row_list.append(report_col_dict)

                # print('       {0}      {1}      {2}    {3:.4f}'.format(max_features, smoothing, fit_prior, auc/k))
    report_dict['model_eval_report'] = report_row_list

    return report_dict

''' train_model

    Function to train the naive bayes model
'''
def train_model(cleaned_emails, labels, model_hyper_param_dict, model_file, vectorizer_file):

    # Create term vector
    vectorizer = TfidfVectorizer(stop_words="english", 
            max_features = model_hyper_param_dict['max_features'])
    
    # Fit the training data in the vectorizer
    term_docs_train = vectorizer.fit_transform(cleaned_emails)
    
    classifier = MultinomialNB(alpha = model_hyper_param_dict['smoothing_factor'], 
            fit_prior=model_hyper_param_dict['fit_prior'])
    
    # Now for the classifier
    classifier.fit(term_docs_train, labels)
    
    # Save the model and the vectorizer
    
    with open(model_file, 'wb') as fp:
        pickle.dump(classifier, fp, protocol = pickle.HIGHEST_PROTOCOL)

    with open(vectorizer_file, 'wb') as fp:
        pickle.dump(vectorizer, fp, protocol = pickle.HIGHEST_PROTOCOL)

'''
    predict

    Function to predict an email using the trained naive bayesian model
'''
def predict(email, model_file, vectorizer_file):

    with open(model_file, 'rb') as fp:
        classifier = pickle.load(fp)

    with open(vectorizer_file, 'rb') as fp:
        vectorizer = pickle.load(fp)

    # cleaned_emails = get_clean_emails(email)
    
    vectorized_email = vectorizer.transform(email)
    prediction = classifier.predict(vectorized_email)
    predict_proba = classifier.predict_proba(vectorized_email)[:,1]
    
    return_value = {
        'prediction' : prediction,
        'prediction_probability': predict_proba
    }
    
    return return_value

