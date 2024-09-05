import logging
logging.basicConfig(filename='ddos_protection.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_alert(message):
    logging.info(message)
