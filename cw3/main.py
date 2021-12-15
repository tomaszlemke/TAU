import requests
import json
import logging

# Creating logging file with test results
logging.basicConfig(filename='testing_results.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('REST API test')
info_counter = 0
error_counter = 0

# --------------------------------------------------
# Checking if API is found

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
# Testing if requesting film with fake id number will return anything

url = 'https://ghibliapi.herokuapp.com/films'
check = {'id': 'testtesttest'}
response = requests.get(url, check)

try:
    assert response.text == '[]'
    logger.info('Test 2 - correct')
    info_counter += 1
except AssertionError:
    logger.error('Test 2 - it should be empty^^"')
    error_counter += 1

# --------------------------------------------------
# Testing if invalid URL will give response code other than 200

url = 'https://ghibliapi.herokuapp.com/thisshouldgiveerror'
response = requests.request('GET', url)

try:
    assert response.status_code != 200
    logger.info('Test 3 - correct')
    info_counter += 1
except AssertionError:
    logger.error('Test 3 - it should not work - random URL ^^"')
    error_counter += 1

# --------------------------------------------------
# Testing if under specific path the defined keys and values can be found

url = 'https://ghibliapi.herokuapp.com/species/b5a92d0e-5fb4-43d4-ba60-c012135958e4'
check = {'classification': 'Spirit'}

response = requests.get(url, check)
a = json.loads(response.text)
for key, value in a.items():
    if key == 'classification':
        check_type = value


try:
    assert check.get('classification') == check_type
    logger.info('Test 4 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 4 - incorrect classification, should be "{check.get("classification")}" but got "{check_type}"')
    error_counter += 1

# --------------------------------------------------
# Testing if API will return specific film using 'name' criteria

url = 'https://ghibliapi.herokuapp.com/people'
check = {'name': 'Ashitaka'}

response = requests.get(url, check)
a = json.loads(response.text)

for key, value in a[0].items():
    if key == 'name':
        check_type = value

try:
    assert check.get('name') == check_type
    logger.info('Test 5 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 5 - name not found, should be "{check.get("name")}" but got "{check_type}"')
    error_counter += 1

# -----------------------------------------------------
# Testing if API will return film by providing film name and id

url = 'https://ghibliapi.herokuapp.com/films/'
film_id = '58611129-2dbc-4a81-a72f-77ddfc1b1b49'
original_title_romanised = 'Tonari no Totoro'
response = requests.request("GET", url + film_id)
a = json.loads(response.text)

for key, value in a.items():
    if key == 'original_title_romanised':
        query_text = value
    if key == 'id':
        query_id = value

try:
    assert original_title_romanised == query_text
    logger.info('Test 6 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 6 - got incorrect film\n'
                 f'Film id: {query_id}\n'
                 f'Original title romanised: {query_text}\n')
    error_counter += 1

# -----------------------------------------------------
# Testing if anything can be added to the list

data = {
    'title': "Toy Story 3",
    'running_time': "98"
}
response = requests.post('https://ghibliapi.herokuapp.com/films/', data=data)
a = json.loads(response.text)
try:
    assert response.status_code == 204
    logger.info('Test 7 - correct')
    info_counter += 1
except AssertionError:
    logger.error(f'Test 7 - post unsuccessful - does not accept POST, response message: {a.get("message")}')
    error_counter += 1

# -----------------------------------------------------
# Testing if limit function returns the correct number of results

url = 'https://ghibliapi.herokuapp.com/films'
check = {'limit': '2'}

response = requests.get(url, check)
a = json.loads(response.text)

result_counter = 0

for value in a:
    for k, v in value.items():
        if k == 'title':
            result_counter += 1


try:
    assert int(check.get('limit')) == result_counter
    logger.info('Test 8 - correct')
    info_counter += 1

except AssertionError:
    logger.error(f'Test 8 - Limit does not work, it should display only: {check.values()}')
    error_counter += 1