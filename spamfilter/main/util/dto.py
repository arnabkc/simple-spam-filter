from flask_restplus import Namespace, fields

class SpamFilterDto:
    api = Namespace('spamfilter', description = 'spamfilter related operations')
    
    spamfilter = api.model('spamfilter', {
        'document_class' : fields.String(required = True, description = 'States whether a document is ham or spam')
    })

