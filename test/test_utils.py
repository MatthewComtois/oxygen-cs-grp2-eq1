from src.utils import *
import pytest

# ------test_get_env_var--------


def test_get_env_var_not_found_int():
    assert get_env_var("test", 200, False) is 200


def test_get_env_var_not_found_string():
    assert get_env_var("test", "test2", False) is "test2"


def test_get_env_var_found_string():
    assert get_env_var("test_string", "test2", False) == "testString"


def test_get_env_var_found_int():
    assert get_env_var("test_int", "test2", False) == "12"


def test_get_env_var_found_empty_true():
    assert get_env_var("test_empty", "test2", True) == ""


def test_get_env_var_found_empty_False():
    assert get_env_var("test_empty", "test2", False) == "test2"


# ------test_get_env_var_strict--------


def test_get_env_var_strict_not_found():
    with pytest.raises(
        Exception,
        match="La variable 'test' doit être définie comme variable d'environnement.",
    ):
        get_env_var_strict("test", True)


def test_get_env_var_strict_found_string():
    assert get_env_var_strict("test_string", True) == "testString"


def test_get_env_var_strict_found_int():
    assert get_env_var_strict("test_int", True) == "12"


def test_get_env_var_strict_found_empty_true():
    assert get_env_var_strict("test_empty", True) == ""


def test_get_env_var_strict_found_empty_False():
    with pytest.raises(
        Exception,
        match="La variable 'test_empty' doit être définie comme variable d'environnement.",
    ):
        get_env_var_strict("test_empty", False)
