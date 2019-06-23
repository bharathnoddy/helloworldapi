
from username import app
import configparser
import logging

logging.basicConfig(filename='/var/log/helloworld.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('config.ini')

host = config['DEFAULT']['host']
port = config['DEFAULT']['port']

app.run(host=host, port=port, debug=True)
