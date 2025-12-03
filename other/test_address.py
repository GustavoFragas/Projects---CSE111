from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():

    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("456 Elm St,   Los Angeles, CA 90001  ") == "Los Angeles"
    assert extract_city("789 Oak St,New York, NY 10001") == "New York"
    assert extract_city("  101 Pine St,   Miami, FL 33101") == "Miami"

def test_extract_state():

    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("456 Elm St,   Los Angeles, CA 90001") == "CA"
    assert extract_state("789 Oak St,New York, NY 10001") == "NY"
    assert extract_state("  101 Pine St,   Miami, FL 33101") == "FL"

def test_extract_zipcode():

    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("456 Elm St,   Los Angeles, CA 90001  ") == "90001"
    assert extract_zipcode("789 Oak St,New York, NY 10001") == "10001"
    assert extract_zipcode("  101 Pine St,   Miami, FL 33101") == "33101"

pytest.main(["-v", "--tb=line", "-rN", __file__])