import requests
from urllib.parse import urlencode


class TelegramBot(object):

    def __init__(self, token):
        self.token = token
        self.chatid = None

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
        return resp['result'][0]['message']['chat']['id']

    def sendmessage(self, message):
        if not self.chatid:
            self.chatid = self.getchatid()
        variables = {
            'chat_id': self.chatid,
            'text': message
        }
        resp = self.request('sendMessage', variables)
        return resp
