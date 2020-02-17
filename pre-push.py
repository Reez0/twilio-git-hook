import os
import sys
from pathlib import Path
import getpass
import subprocess
from twilio.rest import Client

full_path = os.getcwd()
project = full_path.split(os.sep)[-1]
user = getpass.getuser()
commit_message = str(subprocess.check_output(['git','log','-1', '--pretty=%B'],
                     encoding='utf-8')).replace('\n', ' ').replace('\r', '').strip()

team_members = [{'name':'Team Member 1','number':'+xxxxxxxxxxx'},{'name':'Team Member 2','number':'+xxxxxxxxxxx'}]

whatsapp_message = f'''{user} just pushed some code to the {project} project with a commit message of
'{commit_message}' '''

account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

for team_member in team_members:
    message = client.messages.create(
                                body= f"Hi, {team_member['name']}. \n"+whatsapp_message,
                                from_='whatsapp:<Twilio Whatsapp Number>',
                                to=f"whatsapp:{team_member['number']}"
                            )