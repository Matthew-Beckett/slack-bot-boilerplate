from flask import request, make_response, Blueprint
from pprint import pformat
from boilerplate.utils.slack import create_slackclient

import json
import logging
import os

logger = logging.getLogger('werkzeug')

index_blueprint = Blueprint('index', __name__)

slackclient = create_slackclient()

@index_blueprint.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        logger.info("Recieved GET on route /")
        return make_response("I'm up!", 200)
    if request.method == 'POST':
        data = json.loads(request.data.decode("utf-8"))
        logger.info(pformat(data))
        if 'challenge' in data:
            logger.info("Recieved Slack challenge response")
            return(data['challenge'])

        elif data['event']['type'] == 'app_mention':
            logger.info("Bot mention recieved, returning menu options.")
            try:
                with open('config/botOptions.json') as options_file:
                # Dictionary of menu options which will be sent as JSON
                    slackclient.chat_postMessage(
                    channel=data['event']['channel'],
                    text="Choose options:",
                    attachments=json.load(options_file)
                    )
                # Send an HTTP 200 response with empty body so Slack knows we're done here
                return make_response("", 200)
            
            except Exception as e:
                logger.error(e)
                return make_response("Internal Server Error", 500)

        else:
            logger.warning("An event type which cannot be handled was recieved")
            return make_response("Unknown event type", 500)

    else:
        make_response("Unsupported method" + request.method, 500)