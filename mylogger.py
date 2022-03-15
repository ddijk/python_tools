from logging import getLogger
import logging
import sys
import os

mylevel=os.environ.get('OLL', 'INFO')

#print(f'mylevel={mylevel}')

#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s')

logger = getLogger(__name__)

if mylevel == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger.info('regel op level "info"')
logger.debug('regel op level "debug"')
#logger.warning('Watch out!') 
#print('the end', sys.stdout)
sys.stdout.write('the end')
