from pkg_resources import resource_filename
import random, gzip, glob

collection_names = ['chuck', 'pyjokes_en', 'unsorted']
cache = {}

def _load_file(collection_name):
    with gzip.open(resource_filename('oneliners', 'data/' + collection_name + '.txt.gz')) as f:
        result = f.read().decode('utf8').split('\n')
    return result

def get_collection(name=None):
    if name not in cache:
        if name is None:
            result = []
            for c in collection_names:
                result.extend(get_collection(c))
            cache[name] = result
        else:
            cache[name] = _load_file(name)
    return cache[name]

def get_random(collection_name=None):
    '''Generate a random joke from a given collection (see "oneliners.collection_names" for a list of options).
       When collection_name=None, generates a random joke from all available collections.'''
    return random.choice(get_collection(collection_name))