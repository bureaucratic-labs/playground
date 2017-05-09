from ujson import dumps
from functools import partial

from yargy.normalization import get_normalized_text


json_dumps = partial(dumps, ensure_ascii=False)


def serialize_entities(results):
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
