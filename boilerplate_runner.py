from flask import Flask
from boilerplate.routes.index import index_blueprint
from boilerplate.routes.slack import slack_message_actions_blueprint

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('werkzeug')

app = Flask(__name__)
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(slack_message_actions_blueprint, url_prefix='/slack')

if __name__ == "__main__":
    logger.info("Staring boilerplate...")
    app.run()