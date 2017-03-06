# ✒︎ vocab
Import vocabulary lists to Airtable and generate flash cards.

## ❯ Requirements
- python2
- [pipenv](https://github.com/kennethreitz/pipenv)

## ❯ Usage
```bash
# Install dependencies and activate virtualenv
$ pipenv install && pipenv shell --compat

# Load some poetry terms to Airtable
$ python vocab.py airtable load 'https://www.vocabulary.com/lists/479437' <airtable-base-endpoint> <airtable-api-key>
```
