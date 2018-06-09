from flask import request
from flask_restplus import Resource

from spamfilter.main.util.dto import SpamFilterDto
from spamfilter.main.service.spam_or_ham import is_spam

api = SpamFilterDto.api
_spamfilter = SpamFilterDto.spamfilter

@api.route('/documentclass')
class check_document_class(Resource):
    @api.doc('Tells whether a document is Ham or Spam')
    # @api.marshal_list_with(_spamfilter, envelope = 'data')
    def post(self):
        """ Find whether the document is ham or spam """
        req = request.data
        # email = req['email']

        print(len(req))

        email_list = []
        email_list.append(req)

        # print(email_list)

        doc_type = is_spam(email_list)

        response_object = {
            'document_class' : doc_type[0]
        }

        print(response_object)

        return doc_type

