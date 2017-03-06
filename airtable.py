import logging
import requests

logger = logging.getLogger(__name__)


class Airtable:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key
        self.headers = {
            'Authorization': 'Bearer ' + key,
        }

    def load(self, words):
        """Given word descriptions collected from a source, load it into a Base"""
        for word in words:
            logger.info('saving ' + word['word'])

            payload = {
                'fields': {
                    'Word': word['word'],
                    'Type': word['type'],
                    'Frequency': float(word['frequency']),
                    'Description': word['description'],
                    'Short': word['short'],
                    'Long': word['long']
                }
            }

            request = requests.post(self.endpoint, headers=self.headers, json=payload)

            if request.status_code != 200:
                raise Exception('Error %d while saving %s' % (request.status_code, word['word']))
