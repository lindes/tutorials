# server.py -- a very simple flask app for vagrant provisioning demo

# normal flask stuff:
import flask
from flask import Flask

app = Flask(__name__)

# Stuff so we can see where we're running, to display that:
import socket, os

# Very simple route to show that this server is running (and where):
@app.route('/')
def hello_world():
    # See if we can figure out if we're in a vagrant box -- the file
    # we're checking for is *probably* only installed within a vagrant
    # installation, because it's specifically meant to be used there:
    if os.path.isfile('/sbin/mount.vboxsf'):
        vboxstatus = "which seems to be inside vagrant! Yay!"
    else:
        vboxstatus = "which doesn't seem to be within vagrant... did you mean it to be?"

    return 'Running on host ' + socket.gethostname() + ' -- ' + vboxstatus
