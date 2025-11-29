import logging

def setup_logger():
    logging.basicConfig(
        filename='search.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
