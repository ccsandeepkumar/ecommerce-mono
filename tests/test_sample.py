import logging

logging.basicConfig(level=logging.INFO)

def test_logging():
    logging.info("This will show in logs")
    assert True
