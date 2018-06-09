#!/bin/bash

# Replace the <test option> with one of the following (depending on the test you want to run)
#
# TEST OPTIONS
# ============
# test_all : to run all tests
# test_config : to run configuration tests (code that are in config package)
# test_util : to run utility code tests (util package)
# test_model : to run machine learning model code tests (model package)
# test_model_evaluate : to run model evaluation and hyper parameter discovery code tests
# test_model_training : to run model training tests
# test_model_predict : to run predition tests
#
python manage.py <test option>
