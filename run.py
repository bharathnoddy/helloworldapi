
from username import app
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

host = config['DEFAULT']['host']
port = config['DEFAULT']['port']

app.run(host=host, port=port, debug=True)
