from datetime import datetime

from pytest import raises

from beacon_proj.main import add_timestring


# Basic case just adding one hour
def test_add_timestring():
    assert add_timestring("00:00:00", "01:00:00") == "01:00:00"


def test_add_timestring_with_minutes_case():
    assert add_timestring("00:31:00", "00:31:00") == "01:02:00"


# This has to raise an error
def test_add_timestring_with_letters():
    with raises(Exception) as e:
        add_timestring("as:00:00", "01:00:00")
        assert "as:00:00" in str(e.value)
