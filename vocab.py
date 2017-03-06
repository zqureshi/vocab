import fire
import json
import sys

from source import VocabularyCom
from airtable import Airtable


class CLI:
    class source:
        """Import word lists from various sources"""

        def vocabulary_com(self, list_url, pretty=False):
            result = VocabularyCom().collect(list_url)

            if pretty:
                print json.dumps(result, indent=4, sort_keys=True)
            else:
                json.dump(result, sys.stdout)

    class airtable:
        """Sync lists to Airtable"""

        def load(self, list_url, endpoint, key):
            words = VocabularyCom().collect(list_url)
            self._load(words, endpoint, key)

        def load_from_stdin(self, endpoint, key):
            words = json.load(sys.stdin)
            self._load(words, endpoint, key)

        def _load(self, words, endpoint, key):
            airtable = Airtable(endpoint, key)
            airtable.load(words)

            print 'Loaded %d terms to Airtable.' % len(words)


if __name__ == '__main__':
    fire.Fire(CLI)
