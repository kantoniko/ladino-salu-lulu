import os
from yaml import safe_load

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(root, 'book.yaml')) as fh:
    data = safe_load(fh)

