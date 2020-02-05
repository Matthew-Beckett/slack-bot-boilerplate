from flask import request, make_response, Blueprint
from boilerplate.utils.slack import create_slackclient
from pprint import pformat

import json
import logging
import os
import time
import threading

logger = logging.getLogger('werkzeug')

slack_message_actions_blueprint = Blueprint('slack_message_actions', __name__)

slackclient = create_slackclient()

@slack_message_actions_blueprint.route('/message_actions', methods=['POST'])
def message_actions_route():
    data = json.loads(request.form["payload"])
    logger.info(pformat(data))

    if data['callback_id'] == 'menu_options_2319':

        if data['actions'][0]['value'] == 'list':
            logger.info("Recieved request to 'list' from user " + data['user']['name'])
            slackclient.chat_update(
                channel=data['channel']['id'],
                ts=data['message_ts'],
                text="This method is not implemented yet.",
                attachments=[]
            )
            return make_response("", 200)

        if data['actions'][0]['value'] == 'move':
            logger.info("Recieved request to 'move' from user " + data['user']['name'])
            slackclient.chat_update(
                channel=data['channel']['id'],
                ts=data['message_ts'],
                text="This method is not implemented yet.",
                attachments=[]
            )
            return make_response("", 200)

    elif data['callback_id'] == 'move_targets':
        if data['type'] == 'dialog_cancellation':
            slackclient.chat_postMessage(
                channel=data['channel']['id'],
                text="Request cancelled by " + data['user']['name'],
                attachments=[]
            )
            return make_response("", 200)

        elif data['type'] == 'dialog_submission':
            slackclient.chat_postMessage(
                channel=data['channel']['id'],
                text="This is not implemented yet.",
                attachments=[]
            )
            return make_response("", 200)

        else:
            return make_response("Unexpected callback type", 500)

def self_destruct_message(ts: str, channel_id:str, delay: int):
    time.sleep(delay)
    slackclient.chat_delete(
                channel=channel_id,
                ts=ts
            )
