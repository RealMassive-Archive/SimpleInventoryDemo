"""
simple_inventory_demo.py -- Simple demo showing you how to manage your invetory
using the RealMassive API.

GitHub Project URL: https://github.com/inchoate/SimpleInventoryDemo
"""
import json
import requests
import os
import sys
import time

# BEGIN USER-DEFINED VARIABLES -- PLEASE UPDATE THESE
#
_MY_API_TOKEN = "ahBzfnJtLWFwaS1zYW5kYm94ciYLEgRVc2VyGICAgMCUo58KDAsSCEFwaVRva2VuGICAgICA14wKDA"
_MY_EMAIL = "jason.vertrees@realmassive.com"
_MY_PASSWORD = "a123123123"
#
# END USER-DEFINED VARIABLES -- PLEASE UPDATE THESE


# Constants
_BASE_URL = "https://rm-api-sandbox.appspot.com"
_BASE_API_URL = "/".join([_BASE_URL, "api/v1"])
_HEADERS = {"X-Client-Id": _MY_API_TOKEN}
_HERE = os.path.dirname(__file__)
_INPUT_FILES = {
    "users": "users.csv",
    "buildings": "buildings.csv",
    "spaces": "spaces.csv",
}

#
# Helper Functions: Usage & Testing
#
def _usage(msg=None):
    """
    Prints useful info for the user.
    """
    if not msg:
        print "Information here..."
    else:
        print msg
    sys.exit(1)
def _test_rm_up():
    """
    Tests to see if the sanbox is running.
    """
    r = requests.options(_BASE_URL)
    return r.status_code == 200
def _test_api_up():
    """
    Tests to see if the API is running.
    """
    r = requests.options(_BASE_API_URL, headers=_HEADERS)
    return r.status_code == 200
def _check():
    """
    Checks for proper environment setup.
    """
    if "X-Client-Id" not in _HEADERS:
        msg = "[ERROR]: 'X-Client-Id' used for API tokens not found in the rqeuest header.\n"
        msg += "[ERROR]: Please visit https://www.realmassive.com/developer-center/ to apply\n"
        msg += "[ERROR]: for an API token if you don't have one.\n"
        _usage(msg)

    if not _test_rm_up():
        msg = "[ERROR]: '{}'' was not responding.\n".format(_BASE_URL)
        msg += "[ERROR]: Please ensure your _BASE_URL is correct and try again.\n"
        _usage(msg)

    if not _test_api_up():
        msg = "[ERROR]: '{}'' was not responding.\n".format(_BASE_API_URL)
        msg += "[ERROR]: Please ensure your _BASE_API_URL is correct and try again.\n"
        _usage(msg)

    print "[INFO]: All tests passsed. Starting."
    return True

#
# Helper Functions: Getting Data
#
def _rget(query, sess):
    """
    restartable_get: a get that is smart enough to wait for rate limits.

    PARAMS
        query - (string) the query
        sess - request.Session

    RETURNS
        requests.Response - the original response
    """
    _backoff = 2.0

    while True:
        # try the queyr
        resp = sess.get(query, headers=_HEADERS)

        if resp.status_code != 429:
            # we're not throttled, so return response
            return resp

        # here we're throttled; so back off and retry
        time.sleep(_backoff)
        backoff = 2.0 * _backoff
        # while True's often require sanity checks: enforcing sanity
        if backoff > 600:
            print "Asked to sleep, like, forever. Bailing, something's really wrong."
            sys.exit()


def _step1_create_user(first_name, last_name, email, password, phone, company, title):
    """
    Create a user given the user info.

    To create a user POST to https://rm-api-sandbox.appspot.com/auth/signup with the payload:
        {
            "company": "RealMassive",
            "email": "broker_email_here@realco.com",
            "first_name": "Chris",
            "last_name": "Broker",
            "password": "broker_pw_here",
            "phone": "555-555-5555",
            "title": "Broker"
        }

    PARAMS:
        email: (string) new user's email address
        password: (string) new user's password
        first_name: (string) new user's first name
        last_name: (string) new user's last name
        phone: (string) new user's contact number
        title: (string) new user's title

    RETURNS:
        User payload in JSON:

        {
            "auth_providers": [
                "email"
            ],
            "available_positions": [],
            "company": "",
            "company_role": "",
            "company_size": ""
            "created_at": "2015-07-20T16:53:19.849840+00:00",
            "edited_at": "2015-07-20T16:53:20.630020+00:00",
            "email": "broker_email_here@realco.com",
            "email_verified": true,
            "first_name": "Chris",
            "id": "5081532861513728",
            "is_premium": "",
            "key": "ahBzfnJtLWFwaS1zYW5kYm94chELEgRVc2VyGICAgImJtIMJDA",
            "last_login": "",
            "last_name": "Broker",
            "login_count": "",
            "organizations": [
                "ahBzfnJtLWFwaS1zYW5kYm94chkLEgxPcmdhbml6YXRpb24YgICAiYngygoM"
            ],
            "phone": "281-000-0000",
            "photo": "/static/img/default_profile.jpg",
            "secondary_email": "",
            "title": "Broker",
        }
    """
    _CREATE_USER_URL = "/".join([_BASE_URL, "auth/signup"])

    user_payload = {
        "company": company,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "title": title,
        # "photo": photo
    }

    response = requests.post(_CREATE_USER_URL, data=user_payload)

    if response.status_code != 200:
        print "[ERROR]: Could not create user."
        sys.exit(1)
    else:
        print "[INFO]: User {} exists. Once this user's email is confirmed, you can login as him/her.".format(
                email)


def _step2_confirm_email():
    """
    This is done in via the user's email client.
    """
    print "[INFO]: Currently, this step must be completed through the user's email client."


def _step3_login_as_user(email, password):
    """
    Login as the user to customize his/her profile.

    RETURNS
        (requests.session) to store user session info for subsequent calls.

    NOTES:
        * API_TOKEN required for this call. Passed in headers.
    """
    _LOGIN_URL = "/".join([_BASE_URL, "/api/v1/auth"])
    login_payload = {
            "email": email,
            "password": password,
    }

    session = requests.Session()

    response = session.post(_LOGIN_URL, data=login_payload, headers=_HEADERS)

    if response.status_code == 200:
        print "[INFO]: Logged in as {}.".format(email)
        print "[INFO]: Server responded: {}.".format(response.content)
        return session, json.loads(response.content)["user_info"]
    else:
        print "[ERROR]: Could not login as user. Response from server: {}".format(response.content)
        sys.exit(1)

def _step4_assign_user_photo(sess, user, photo_url, category):
    """
    This will assign the user's profile photo.
    """
    _USER_URL = "/".join([_BASE_API_URL, "users/{}".format(user.get("key"))])

    # GET returns the true model
    response = sess.get(url=_USER_URL, headers=_HEADERS)
    if response.status_code != 200:
        print "[ERROR]: Could not assign user photo. Response from server: {}".format(response.content)
        import pdb; pdb.set_trace()
        sys.exit(1)

    user = json.loads(response.content)

    del user["is_premium"]  # read only
    del user["email_verified"]  # read only
    user.update({"photo": photo_url})

    response = sess.put(url=_USER_URL,
                        data=json.dumps(user),
                        headers=_HEADERS)

    if response.status_code == 200:
        print "[INFO]: Photo assigned to user {}".format(user.get("email"))
    else:
        print "[ERROR]: Could not assign user photo. Response from server: {}".format(response.content)
        sys.exit(1)




if __name__ == '__main__':
    if not _check():
        _usage()

    _EMAIL = "jason.vertrees+api9@realmassive.com"

    _step1_create_user(first_name="JasonTEST",
                       last_name="VertreesTEST",
                       email=_EMAIL,
                       password="a123123123",
                       phone="1-800-888-8888",
                       company="RealMassvie+TEST",
                       title="CTO+TEST",)

    _step2_confirm_email()

    sess, user = _step3_login_as_user(_EMAIL,
                                "a123123123")

    print "===> Logged in {} {} ({})".format(user.get("first_name"), user.get("last_name"), user.get("email"))

    # _step3_upload_user_photo(sess,
    #                          user=user,
    #                          photo_file="/path/to/file",
    #                          category="profile_upload")

    _step4_assign_user_photo(sess,
                             user=user,
                             photo_url="https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/7/005/065/326/202211e.jpg", # NOQA
                             category="profile_upload")
    # PUT w/User and photo URL


# TODO: Document /auth/signup. Passing this data as "application/x-www-form-urlencoded":
#
# first_name=Jason&last_name=Vertrees&company=RealMassive&title=CTO&email=jason.vertrees%2Bapi5%40realmassive.com&password=a123123123
#
# successfully returns this:
#
# {
#   "register_success": true
# }










