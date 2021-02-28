import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO, filename='logs.txt')

logger = logging.getLogger('test_logger')

logger.info('This wont show')
logger.error('This will show ')