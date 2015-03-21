from __future__ import unicode_literals

import os
import time
import random
import pkgutil

root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))


def load_fixtures(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([os.path.join(root_dir, dirname)]):
        full_package_name = '%s.%s' % (dirname, package_name)
        name, module = package_name, importer.find_module(package_name).load_module(full_package_name)
        yield name, getattr(module, 'export')

adjetives = dict(load_fixtures('adjetives'))
nouns = dict(load_fixtures('nouns'))


def get_random_name():
    random.seed(time.time())
    adjetive = random.choice(adjetives['common'])
    noun = random.choice(nouns['science'])
    return '{0} {1}'.format(adjetive, noun)
