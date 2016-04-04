'''
Allows to read .env files for a particular project.
'''
import logging

from os import path

logger = logging.getLogger(__name__)

my_user_id = None
outputs = []

def setup(bot):
    logger.info('setup read configuration plugin')
    global my_user_id
    slack_client = bot.slack_client
    my_user_id = slack_client.server.login_data['self']['id']

def process_message(data):
    # Ignore joins, leaves, typing notifications, etc... and messages from me
    if 'subtype' in data or data['user'] == my_user_id:
        return

    channel_id = data['channel']
    channel_tag = channel_id[0]
    if channel_tag == 'C': # 'C' indicates a message in a normal channel
        handle_channel_message(channel_id, data)
    elif channel_tag == 'D': # 'D' indicates a message in an IM channel
        handle_direct_message(channel_id, data)

def handle_direct_message(channel_id, data):
    text = data['text'].strip()
    if text == 'help':
        return send_help_text(channel_id)

    if text.startswith('read configuration'):
        _, _, project_name = text.split(' ')
        project_app_home_path = path.expanduser('~%s' % project_name)
        project_configuration_path = path.join(project_app_home_path, '.env')

        if not path.exists(project_configuration_path):
            return send(channel_id, 'there is no configuration file')

        message_fmt = '```%s\n```'

        with open(project_configuration_path) as f:
            return send(channel_id, message_fmt % f.read())

def handle_channel_message(channel_id, data):
    send(channel_id, "use DM")
    return

def send(channel_id, message):
    outputs.append([channel_id, message])

def send_help_text(channel_id):
    send(channel_id, HELP_TEXT)

HELP_TEXT = \
'''Here are the commands I understand:
```
read configuration <project name>   dump the .env of that project
```'''
