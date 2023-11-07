import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
##logging.disable(logging.CRITICAL)
def faction(n):
    logging.debug('start of faction(%s)'%n)
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug('i is'+str(i))
    logging.debug('end of faction')
    return total
print(faction(5))