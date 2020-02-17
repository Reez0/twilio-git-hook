# twilio-git-hook
A python git hook to send a message over WhatsApp whenever you do a git push

1. In your .git directory change pre-push.sample to pre-push
2. Your pre-push should be something like this on Windows. Not sure about Linux.

`#!/bin/sh`

`C:/Users/<Your user>/AppData/Local/Programs/Python/Python38/python C:/path/to/your/repo/.git/hooks/pre-push.py`

`exit 0`

3. Change the Python path to whatever Python version you use.
4. run `pip install twilio`. Do not use a virtual env.
5. Change team members, account SID, auth token and Twilio number to the information provided to you by Twilio.
