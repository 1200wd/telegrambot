import requests
from urllib.parse import urlencode


class TelegramBot(object):

    def __init__(self, token, chat_id=None):
        self.token = token
        self.chatid = chat_id

    def request(self, method, variables=None):
        url = 'https://api.telegram.org/bot%s/' % self.token
        url += method
        if variables is None:
            variables = {}
        if variables:
            url_vars = '?' + urlencode(variables)
            url += url_vars

        resp = requests.get(url)
        if resp.status_code != 200:
            print("Warning %d: %s" % (resp.status_code, resp.reason))
        return resp.json()

    def getchatid(self):
        resp = self.request('getUpdates')
        if not resp['result']:
            raise ValueError('Chat ID not found, please provide a Chat ID or send a message to the chat')
        chatid = resp['result'][0]['message']['chat']['id']
        try:
            open('.chatid', 'w').write(str(chatid))
        except Exception:
            pass
        return chatid

    def sendmessage(self, message):
        if not self.chatid:
            self.chatid = self.getchatid()
        variables = {
            'chat_id': self.chatid,
            'text': message
        }
        resp = self.request('sendMessage', variables)
        return resp
