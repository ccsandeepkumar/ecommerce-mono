import pytest
import logging

logging.basicConfig(level=logging.INFO)

@pytest.mark.testrail(1512)
def test_payment():
    logging.info("Executing payment test")
    logging.info("TestRail ID: 1512")
    assert True
