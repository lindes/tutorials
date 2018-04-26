# server.py -- a very simple flask app for vagrant provisioning demo

# normal flask stuff:
import flask
from flask import Flask

app = Flask(__name__)

# Stuff so we can see where we're running, to display that:
import socket, os, sys
from os import environ as env

# Very simple route to show that this server is running (and where):
@app.route('/')
def server_info():
    """Print some information about where and how this server is running.
We'll gather together a few bits of information, and then just print
them all, with some separator lines.

    """

    # a separator between several sections of output:
    section_separator = "-" * 70

    # First section: See if we can figure out if we're in a vagrant box
    # -- the file we're checking for is *probably* only installed within
    # a vagrant installation, because it's specifically meant to be used
    # there:
    if os.path.isfile('/sbin/mount.vboxsf'):
        vboxstatus = "which seems to be inside vagrant! Yay!"
    else:
        vboxstatus = "which doesn't seem to be within vagrant... did you mean it to be?"

    # include hostname and the above status:
    host_info    = " ".join(['Running on machine with hostname',
                        socket.gethostname(), '--', vboxstatus])

    # also include information about which version of python we're
    # running under:
    python_info  = sys.version

    # and finally, get information about where Vagrant is running from
    # (if applicable).  (Note: This environment variable is set up by
    # the provisioning in the Vagrantfile we use here; it's not
    # something that's normally available.)
    vagrant_dir = env.get('VAGRANT_DIR',
                          "[not in vagrant or unknown vagrant directory]")

    # Finally, we put it all together as a big string with newlines:
    plain_text = "\n".join([host_info, section_separator,
        "Python version information:", python_info, section_separator,
        "Vagrant directory:", vagrant_dir])

    # If we're running under flask, return this as a "text/plain" HTTP
    # response:
    if flask.has_request_context():
        return flask.Response(plain_text, mimetype='text/plain')
    else:
        # otherwise, just return the text, so we can test it from the
        # command line, via the following (__name__ == '__main__')
        # section.
        return plain_text

# Debug/test code:
if __name__ == '__main__':
    print "If you actually want to run the server, please make sure " + \
        "FLASK_APP is set, and run under 'flask run'."
    print
    print "But here's what 'GET /' would give:"
    print
    print server_info()
