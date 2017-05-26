from ujson import dumps
from functools import partial

from yargy.utils import get_tokens_position
from yargy.normalization import get_normalized_text
from yargy.interpretation import InterpretationEngine

from natasha.grammars.person import PersonObject
from natasha.grammars.organisation import OrganisationObject
from natasha.grammars.location import LocationObject, AddressObject


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
    'address': AddressObject,
}


def serialize_object_attributes(obj, attributes):
    for attribute in attributes:
        tokens = getattr(obj, attribute)

        if not tokens:
            continue

        yield attribute, get_normalized_text(tokens) if tokens else None

    yield 'spans', [
        {
            'position': get_tokens_position(t),
            'normalized': get_normalized_text(t),
        } for t in obj.spans
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


def serialize_address_object(obj):
    attributes = serialize_object_attributes(obj, {
        'street_descriptor',
        'street_name',
        'house_number',
        'house_letter',
        'house_corpus',
        'house_building',
    })
    return {k: v for k, v in attributes}


OBJECT_SERIALIZERS = {
    'person': serialize_person_object,
    'organisation': serialize_organisation_object,
    'location': serialize_location_object,
    'address': serialize_address_object,
}


def extract_objects(matches):
    for type, obj in OBJECTS_MAPPING.items():
        engine = InterpretationEngine(obj)
        for result in engine.extract(matches):
            yield (type, result)


def solve_coreference(objects):
    results = []
    for a in objects:
        if not any(a == b for b in results):
            results.append(a)
        else:
            for i, b in enumerate(results):
                if a == b:
                    item = b[1].merge(a[1])
                    results[i] = (
                        b[0],
                        item,
                    )
    return results


def serialize_objects(objects):
    objects = solve_coreference(objects)
    results = []
    for t, o in objects:
        fields = OBJECT_SERIALIZERS[t](o)
        spans = fields.pop('spans')
        item = {
            'type': t,
            'fields': fields,
            'spans': spans,
        }
        results.append(item)
    return results
