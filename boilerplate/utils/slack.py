
from timeit import default_timer as timer
from slack.web.classes import dialogs, dialog_elements
from slack.web.classes.objects import Option

import slack
import os
import json
import logging
import operator

logger = logging.getLogger('werkzeug')

def create_slackclient(slack_bot_token=None):
    if slack_bot_token == None:
        if 'SLACK_BOT_TOKEN' not in os.environ:
            raise Exception("Unable to obtain SLACK_BOT_TOKEN from environment")
        else:
            return slack.WebClient(os.environ.get('SLACK_BOT_TOKEN'))
    else:
        return slack.WebClient(slack_bot_token)
