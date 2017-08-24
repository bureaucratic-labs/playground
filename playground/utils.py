
from json import dumps
from functools import partial


json_dumps = partial(dumps, ensure_ascii=False)
