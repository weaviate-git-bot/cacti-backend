import logging
from websocket_server import WebsocketServer
import chat

client_id_to_chat = {}

def new_client(client, server):
    client_id_to_chat[client['id']] = chat.new_chat()

def client_left(client, server):
    client_id_to_chat.pop(client['id'])

def message_received(client, server, message):
    client_chat = client_id_to_chat[client['id']]
    r = client_chat.chat(message)
    server.send_message(client, r)


server = WebsocketServer(host='127.0.0.1', port=9999, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.set_fn_client_left(client_left)
server.run_forever()
