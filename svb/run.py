#!/usr/bin/python3

from bottle import route, run, request, response, HTTPError, error, install, view, static_file
import string
import urllib3, logging
import sys
import os
import json
import random

class out:

    INFO, WARN, ERROR = ((32, "INFO"), (33, "WARN"), (31, "ERROR"))

    @staticmethod
    def _output(message, type):
        sys.stdout.write("[\033[1;%im%s\033[0;0m] " % type + "%s\n" % message)

    @staticmethod
    def info(message):
        out._output(message, out.INFO)

    @staticmethod
    def warn(message):
        out._output(message, out.WARN)

    @staticmethod
    def error(message):
        out._output(message, out.ERROR)
        sys.exit(1)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')


@route("/", method="GET")
@view("index.tpl")
def index() :
    url = request.headers['HOST']
    BADGE = getBadge()
    MY_NODE_NAME = os.environ.get('MY_NODE_NAME') # None
    MY_POD_NAME = os.environ.get('MY_POD_NAME') # None
    MY_POD_NAMESPACE = os.environ.get('MY_POD_NAMESPACE') # None
    MY_POD_IP = os.environ.get('MY_POD_IP') # None
    MY_CONTAINER_ID = os.environ.get('HOSTNAME') # None
    try:

        response.status = 200

    except Exception as e:
        response.status = 500
        return {"status": "error", "error": str(e)}
    
    return {"BADGE": BADGE, "url": url, "MY_NODE_NAME": MY_NODE_NAME, "MY_POD_NAME": MY_POD_NAME, "MY_CONTAINER_ID": MY_CONTAINER_ID, "MY_POD_NAMESPACE": MY_POD_NAMESPACE, "MY_POD_IP": MY_POD_IP}


def getBadge():
    ret = []
    try:
        badges = ['adventure.png', 'community.png', 'excellence.png', 'leadership.png', 'rock_solid.png', 'singularity.png']

        ret = random.choice(badges)

    except Exception as e:
        raise Exception("Something Bad append generateAccessKey - %s" % e)
    return ret



def main():
    out.info("Starting SVB")

    try:
        with open("svb.conf") as f:
            c = json.load(f)
    except IOError:
        out.error("Could not read svb.conf file (missing? permission?)")
    except ValueError:
        out.error("Could not parse svb.conf file (not valid json?)")

    try:
        global port
        port = c["http"]["port"]
    except Exception as e:
        out.error("Could not find %s on svb.conf (missing? out of scope ?)" % e)

    try:
        host = c["http"]["host"]
    except Exception as e:
        out.error("Could not find %s on svb.conf (missing? out of scope ?)" % e)

    try:
        global version
        version = c["server"]["version"]
    except Exception as e:
        out.error("Could not find %s on svb.conf (missing? out of scope ?)" % e)


    out.info("Configuration file loaded")

    out.info("Starting http server")

    logging.getLogger("wsgi").addHandler(logging.NullHandler())
    run(
        host=host,
        port=port,
        quiet=True,
        server="paste",
        use_threadpool=True,
        threadpool_workers=15,
        request_queue_size=5,
    )


if __name__ == "__main__":
    main()