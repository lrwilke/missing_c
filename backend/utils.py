import os

script_dir = os.path.dirname(__file__)
rel_path = "resources/engmix.txt"


def get_words():
    # source: http://www.gwicks.net/dictionaries.htm
    with open(os.path.join(script_dir, rel_path)) as f:
        words = f.read().splitlines()
    # don't return short words -> larger makes it easier to guess
    return [w for w in words if len(w) >= 4]
