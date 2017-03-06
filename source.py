import logging
import requests

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def fetch_page(url):
    """Given a URL returns a BeautifulSoup object of its contents"""
    logger.debug('fetching page ' + url)

    request = requests.get(url)
    if request.status_code != 200:
        raise Exception('Error %d while fetching page' % request.status_code)

    return BeautifulSoup(request.text, 'html.parser')


class VocabularyCom:
    def collect(self, url):
        """Given a URL for a vocabulary.com list returns all words and their descriptions"""
        logger.info('fetching list from ' + url)

        word_list = fetch_page(url)
        result = []

        for tag in word_list.find_all('li', class_='entry learnable'):
            logger.info('looking up ' + tag.a.text)

            word_description = fetch_page('https://www.vocabulary.com' + tag.a['href'])

            blurb = word_description.find('div', class_='section blurb')
            definition = word_description.find('div', class_='ordinal first')

            result.append({
                'word': tag.a.text,
                'type': definition.a['title'],
                'description': tag.div.text,
                'short': blurb.find('p', class_='short').text,
                'long': blurb.find('p', class_='long').text,
                'frequency': tag['freq'],
            })

        return result
