import requests
import json
import logging


logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('REST API test')
info_counter = 0
error_counter = 0

# --------------------------------------------------
url = 'https://ghibliapi.herokuapp.com/films'
response = requests.request('GET', url)

try:
    assert response.status_code == 200
    logger.info('Test 1 - correct')
    info_counter += 1
except AssertionError:
    logger.error('Test 1 - could not get requested URL')
    error_counter += 1


# --------------------------------------------------
url = 'https://ghibliapi.herokuapp.com/thisshouldgiveerror'
response = requests.request('GET', url)

try:
    assert response.status_code != 200
    logger.info('Test 2 - correct')
    info_counter += 1
except AssertionError:
    logger.error('Test 2 - it shound not work - random URL ^^"')
    error_counter += 1

# --------------------------------------------------

url = 'https://ghibliapi.herokuapp.com/species/b5a92d0e-5fb4-43d4-ba60-c012135958e4'
check = {'classification': 'Spirit'}

response = requests.get(url, check)
a = json.loads(response.text)
for key, value in a.items():
    if key == 'classification':
        check_type = value


try:
    assert check.get('classification') == check_type
    logger.info('Test 3 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 3 - incorrect classification, should be "{check.get("classification")}" but got "{check_type}"')
    error_counter += 1

# --------------------------------------------------

url = 'https://ghibliapi.herokuapp.com/people'
check = {'name': 'Ashitaka'}

response = requests.get(url, check)
a = json.loads(response.text)

for key, value in a[0].items():
    if key == 'name':
        check_type = value

try:
    assert check.get('name') == check_type
    logger.info('Test 4 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 4 - name not found, should be "{check.get("name")}" but got "{check_type}"')
    error_counter += 1

# -----------------------------------------------------

