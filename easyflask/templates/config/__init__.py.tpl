#coding: utf-8

__all__ = ['load_config']

import os
import inspect
import importlib

_config = None

def load_config():
    global _config
    if _config is not None:
        return _config
    import config.default
    fields = {{k: v for k, v in inspect.getmembers(default.Config) if k.isupper()}}
    if 'ENV' in os.environ:
        try:
            m = importlib.import_module('config.' + os.environ['ENV'])
            new_fields = {{k: v for k, v in inspect.getmembers(m.Config) if k.isupper()}}
            fields.update(new_fields)
        except ImportError:
            pass
    _config = type('Config', (object,), fields)
    return _config
