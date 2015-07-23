import requests
import sys

from constants import (
    BASE_API_URL, BASE_URL, HEADERS
)


# Helper Functions: Usage & Testing
def usage(msg=None):
    """
    Prints useful info for the user.
    """
    if not msg:
        print "Information here..."
    else:
        print msg
    sys.exit(1)


def test_rm_up():
    """
    Tests to see if the sanbox is running.
    """
    r = requests.options(BASE_URL)
    return r.status_code == 200


def test_api_up():
    """
    Tests to see if the API is running.
    """
    r = requests.options(BASE_API_URL, headers=HEADERS)
    return r.status_code == 200


def check():
    """
    Checks for proper environment setup.
    """
    if "X-Client-Id" not in HEADERS:
        msg = "[ERROR]: 'X-Client-Id' used for API tokens not found in the rqeuest header.\n"
        msg += "[ERROR]: Please visit https://www.realmassive.com/developer-center/ to apply\n"
        msg += "[ERROR]: for an API token if you don't have one.\n"
        usage(msg)

    if not test_rm_up():
        msg = "[ERROR]: '{}'' was not responding.\n".format(BASE_URL)
        msg += "[ERROR]: Please ensure your BASE_URL is correct and try again.\n"
        usage(msg)

    if not test_api_up():
        msg = "[ERROR]: '{}'' was not responding.\n".format(BASE_API_URL)
        msg += "[ERROR]: Please ensure your BASE_API_URL is correct and try again.\n"
        usage(msg)

    print "[INFO]: All tests passsed. Starting."
    return True
