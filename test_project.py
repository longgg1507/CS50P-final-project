import pytest
import project

def test_key():
    assert project.get_key() == "d448b1fa8523f6b180b551e64a4edc06"
    
def test_location_format():
    assert type(project.get_location()) == str

def test_time_converter():
    assert project.convert_to_time("6:30") == "day_time"
    assert project.convert_to_time("18:06") == "day_time"
    assert project.convert_to_time("19:22") == "night_time"