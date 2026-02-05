import logging

logging.basicConfig(level=logging.INFO)

def test_logging():
    logging.info("This will show in logs1")
    logging.info("This will show in logs2")
    logging.info("This will show in logs3")
    logging.info("This will show in logs4")
    logging.info("This will show in logs5")
    logging.info("This will show in logs6")
    assert True
