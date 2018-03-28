import yaml
import os
settings = os.path.join(os.path.dirname(__file__), "settings.yaml")


def _load_config():
    with open(settings, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg

config = _load_config()
