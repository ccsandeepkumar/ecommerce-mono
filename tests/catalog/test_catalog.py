import pytest
import logging

logging.basicConfig(level=logging.INFO)

@pytest.mark.testrail(1510)
def test_catalog():
    logging.info("Executing catalog test")
    logging.info("TestRail ID: 1510")
    assert True
