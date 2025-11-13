import pytest
from names import make_full_name, extract_family_name, extract_given_name

def test_make_full_name():

    assert make_full_name("Marie", "Toussaint") ==  "Toussaint; Marie"
    assert make_full_name("John", "O'Connor") ==  "O'Connor; John"
    assert make_full_name("Connor-Michael", "Lee") ==  "Lee; Connor-Michael"

def test_extract_family_name():

    assert extract_family_name("Marie; Toussaint") ==  "Marie"
    assert extract_family_name("John; O'Connor") ==  "John"
    assert extract_family_name("Connor-Michael; Lee") ==  "Connor-Michael"

def test_extract_given_name():

    assert extract_given_name("Marie; Toussaint") ==  "Toussaint"
    assert extract_given_name("John; O'Connor") ==  "O'Connor"  
    assert extract_given_name("Connor-Michael; Lee") ==  "Lee"

pytest.main(["-v", "--tb=line", "-rN", __file__])