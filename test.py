import sys
import nose

assert_equals = nose.tools.assert_equals


def test_py_version_26():

    assert_equals(sys.version_info[0], 2)
    assert_equals(sys.version_info[1], 6)


def test_py_version_27():

    assert_equals(sys.version_info[0], 2)
    assert_equals(sys.version_info[1], 7)

