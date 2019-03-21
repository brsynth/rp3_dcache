import pytest
from dcache.Utils import default_config

def test_config_1():    
    cfg = default_config()
    assert cfg['db']

def test_as_document():
    pass
