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
        'natasha': '0.7.0',
        'yargy': '0.8.0',
    }


async def test_extract_endpoint(cli, war_and_peace_text):
    response = await cli.post('/api/extract', data={
        'text': war_and_peace_text,
    })
    assert response.status == 200
    response = await response.json()

    objects = response['objects']

    assert len(objects) == 3
    assert objects[0] == {
        'fields': {
            'firstname': 'Анна',
            'middlename': 'Павловна',
            'lastname': 'Шерер',
        },
        'spans': [
            {
                'normalized': 'Анна Павловна Шерер',
                'position': [45, 64],
            },
            {
                'normalized': 'Анна Павловна',
                'position': [205, 218],
            }
        ],
        'type': 'person',
    }
    assert objects[1] == {
        'fields': {
            'firstname': 'Мария',
            'middlename': 'Феодоровна',
        },
        'spans': [
            {
                'normalized': 'Мария Феодоровна',
                'position': [106, 122],
            },
        ],
        'type': 'person',
    }

    assert objects[2] == {
        'fields': {
            'firstname': 'Василий',
        },
        'spans': [
            {
                'normalized': 'Василий',
                'position': [163, 170],
            },
        ],
        'type': 'person',
    }