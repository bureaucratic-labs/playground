import pytest

from playground.app import make_app


@pytest.fixture
def cli(loop, test_client):
    app = make_app()
    return loop.run_until_complete(test_client(app))


@pytest.fixture
def war_and_peace_text():
    return '''
    Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина
    и приближенная императрицы Марии Феодоровны, встречая важного и чиновного
    князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла
    несколько дней, у нее был грипп, как она говорила (грипп был тогда
    новое слово, употреблявшееся только редкими)
    '''


async def test_version_endpoint(cli):
    response = await cli.get('/api/version')
    assert response.status == 200
    assert await response.json() == {
        'natasha': '0.8.0',
        'yargy': '0.9.0',
    }


async def test_extract_person_endpoint(cli, war_and_peace_text):
    response = await cli.post('/api/extract', data={
        'text': war_and_peace_text,
    })
    assert response.status == 200
    matches = await response.json()

    assert len(matches) == 4
    assert matches[0] == {
        'fact': {
            'first': 'анна',
            'last': 'шерер',
            'middle': 'павловна',
            'nick': None
        },
        'span': [45, 64],
        'type': 'Name'
    }
    assert matches[1] == {
        'fact': {
            'first': 'мария',
            'last': None,
            'middle': 'феодоровна',
            'nick': None
        },
        'span': [106, 122],
        'type': 'Name'
    }
    assert matches[2] == {
        'fact': {
            'first': 'василий',
            'last': None,
            'middle': None,
            'nick': None
        },
        'span': [163, 170],
        'type': 'Name'
    }
    assert matches[3] == {
        'fact': {
            'first': 'анна',
            'last': None,
            'middle': 'павловна',
            'nick': None
        },
        'span': [205, 218],
        'type': 'Name'
    }
