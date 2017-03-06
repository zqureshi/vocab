import fire
import json
import sys

from source import VocabularyCom

class CLI:
    class source:
        """Import word lists from various sources"""

        def vocabulary_com(self, list_url, pretty=False):
            result = VocabularyCom().collect(list_url)

            if pretty:
                print json.dumps(result, indent=4, sort_keys=True)
            else:
                json.dump(result, sys.stdout)


if __name__ == '__main__':
    fire.Fire(CLI)
