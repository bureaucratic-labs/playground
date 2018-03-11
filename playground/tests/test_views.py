import pytest

from playground.app import make_app


@pytest.fixture
def cli(loop, test_client):
    app = make_app()
    return loop.run_until_complete(test_client(app))


WAR_AND_PEACE_TEXT = '''
    Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина
    и приближенная императрицы Марии Феодоровны, встречая важного и чиновного
    князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла
    несколько дней, у нее был грипп, как она говорила (грипп был тогда
    новое слово, употреблявшееся только редкими)
'''

ADDRESS_TEXT = '''
    В городе-герое Ленинграде, на Малой Конюшенной улице, дом 3
'''


async def test_version_endpoint(cli):
    response = await cli.get('/api/version')
    assert response.status == 200
    assert (await response.json()).keys() == {'natasha', 'yargy', 'pymorphy'}


async def test_extract_person_endpoint(cli):
    response = await cli.post('/api/extract', data=WAR_AND_PEACE_TEXT)
    assert response.status == 200
    matches = await response.json()

    assert matches == [
        {
            'fact': {
                'month': 7,
                'year': 1805
            },
            'span': [20, 34],
            'type': 'Date'
        },
        {
            'fact': {
                'first': 'анна',
                'last': 'шерер',
                'middle': 'павловна',
            },
            'span': [45, 64],
            'type': 'Name'
        },
        {
            'fact': {
                'first': 'мария',
                'middle': 'феодоровна',
            },
            'span': [106, 122],
            'type': 'Name'
        },
        {
            'fact': {
                'first': 'василий',
            },
            'span': [163, 170],
            'type': 'Name'
        },
        {
            'fact': {
                'first': 'анна',
                'middle': 'павловна',
            },
            'span': [205, 218],
            'type': 'Name'
        }
    ]

async def test_extract_location_and_address_endpoint(cli):
    response = await cli.post('/api/extract', data=ADDRESS_TEXT)
    assert response.status == 200
    matches = await response.json()

    assert matches == [
        {
            'fact': {
                'parts': [
                    {'name': 'Малой Конюшенной', 'type': 'улица'},
                    {'number': '3', 'type': 'дом'}
                ]
            },
            'span': [35, 64],
            'type': 'Address',
        }
    ]

async def test_send_and_get_issues(cli):
    response = await cli.post('/api/issues', data=WAR_AND_PEACE_TEXT)
    assert response.status == 200
    assert (await response.json()) == {
        'status': True
    }

    response = await cli.get('/api/issues')
    assert response.status == 200
    assert (await response.json())[0]['text'] == WAR_AND_PEACE_TEXT
