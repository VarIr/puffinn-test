import pytest
from puffinn_test_package.subpackage1.import_puffinn import print_version, create_index


def test_import_puffinn():
    with pytest.raises(AttributeError):
        print_version()


def test_create_index():
    assert create_index()
