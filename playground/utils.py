from ujson import dumps
from functools import partial

from yargy.normalization import get_normalized_text
from yargy.interpretation import InterpretationEngine

from natasha.grammars.person import PersonObject
from natasha.grammars.organisation import OrganisationObject
from natasha.grammars.location import LocationObject


json_dumps = partial(dumps, ensure_ascii=False)


def serialize_spans(results):
    for (grammar, tokens) in results:
        yield {
            'grammar': grammar.__class__.__name__,
            'rule': grammar.name,
            'tokens': [
                {
                    'value': t.value,
                    'position': t.position,
                    'forms': [
                        {
                            'normal_form': f['normal_form'],
                            'grammemes': f['grammemes'],
                        } for f in t.forms
                    ],
                } for t in tokens
            ],
            'normal_form': get_normalized_text(tokens),
        }


OBJECTS_MAPPING = {
    'person': PersonObject,
    'organisation': OrganisationObject,
    'location': LocationObject,
}


def serialize_object_attributes(obj, attributes):
    for attribute in attributes:
        tokens = getattr(obj, attribute)

        if not tokens:
            continue

        yield attribute, get_normalized_text(tokens) if tokens else None

    yield 'spans', [
        (t[0].position[0], t[-1].position[1]) for t in obj.spans
    ]


def serialize_person_object(obj):
    attributes = serialize_object_attributes(obj, {
        'firstname',
        'middlename',
        'lastname',
        'nickname',
        'descriptor',
        'descriptor_destination',
    })

    return {k: v for k, v in attributes}


def serialize_organisation_object(obj):
    attributes = serialize_object_attributes(obj, {
        'name',
        'descriptor',
    })

    return {k: v for k, v in attributes}


def serialize_location_object(obj):
    attributes = serialize_object_attributes(obj, {
        'name',
        'descriptor',
    })

    return {k: v for k, v in attributes}


OBJECT_SERIALIZERS = {
    'person': serialize_person_object,
    'organisation': serialize_organisation_object,
    'location': serialize_location_object,
}


def extract_objects(matches):
    for type, obj in OBJECTS_MAPPING.items():
        engine = InterpretationEngine(obj)
        for result in engine.extract(matches):
            yield (type, result)


def serialize_objects(objects):
    results = []
    for t, o in objects:
        if t not in results:
            results.append({
                'type': t,
                'fields': OBJECT_SERIALIZERS[t](o),
            })
    return results
