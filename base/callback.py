# -*- coding: utf-8 -*-
from langchain.callbacks.base import BaseCallbackHandler


class MyCustomHandler(BaseCallbackHandler):

    def __init__(self, websocket, room):
        self.websocket = websocket
        self.room = room

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print("My custom handler, token: {}".format(token))
        self.websocket.send(token)
        self.websocket.emit('response', token, room=self.room)
