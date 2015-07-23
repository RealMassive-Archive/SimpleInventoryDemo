"""
This module holds functions for users, most notably
  * creating users
  * logging in as a user (and persisting state with sessions)
"""
import json
import requests
import sys

from constants import BASE_API_URL, BASE_URL, HEADERS


def create_user(user_info):
    """
    Create a user from the provided parameters.

    HOW:
        POST the user payload (see code below)
        FORM ENCODED (key/value) not JSON
        TO /auth/signup

    NOTES:
        HEADERS are not required for this route.

    FUNCTION PARAMS:
        first_name: (string) new user's first name
        last_name: (string) new user's last name
        email: (string) new user's email address
        password: (string) new user's password
        phone: (string) new user's contact number
        company: (string) your company's name
        title: (string) new user's title

    FUNCTION RETURNS:
        User payload in JSON. We suggest you store the email or key to this user
        to use in future calls.
    """
    create_user_url = "/".join([BASE_URL, "auth/signup"])
    user_payload = {
        "company": user_info.get("company"),
        "first_name": user_info.get("first_name"),
        "last_name": user_info.get("last_name"),
        "email": user_info.get("email"),
        "password": user_info.get("password"),
        "phone": user_info.get("phone"),
        "title": user_info.get("title"),
        "organization_name": user_info.get("company")
    }

    response = requests.post(create_user_url, data=user_payload)

    if response.status_code != 200:
        print "[ERROR]: Could not create user."
        sys.exit(1)


def login_user(email, password):
    """
    Login as the user to customize his/her profile.

    HOW:
        POST 'email' and 'password'
        FORM ENCODED (key/value) not JSON
        TO /api/v1/auth

    NOTES:
        HEADERS are required. Pass your API token as X-Client-Id.
        Once logged in, we suggest you establish a cookie-based session for
          making calls on behalf of this user. See 'session' in the code.

    FUNCTION RETURNS
        (requests.session) to store user session info for subsequent calls.
    """
    login_url = "/".join([BASE_API_URL, "auth"])
    login_payload = {
        "email": email,
        "password": password,
    }
    # This session holds the user's authentication and persists.
    session = requests.Session()

    response = session.post(login_url,
                            data=login_payload,
                            headers=HEADERS)

    if response.status_code == 200:
        return session, json.loads(response.content)["user_info"]
    else:
        print "[ERROR]: Could not login as user. Response from server:"
        print " {}".format(response.content)
        sys.exit(1)


def assign_user_photo(sess, user, photo_url):
    """
    This will assign the user's profile photo.

    HOW:
        1. GET the user entity you want to update
           AT /api/v1/users/<keystring>

        2. Update that entity's "photo" field with a valid image URL.

        3. PUT the user payload
           JSON encoded
           TO /api/v1/users/<keystring>

    NOTES:
        When you get the user it returns two non-editable fields:
            (1) is_premium
            (2) email_verified
        You need to remove these fields before updating the user. If you don't
        the server will reject your request.
    """
    user_url = "/".join([BASE_API_URL, "users/{}".format(user.get("key"))])

    # GET returns the true User model
    response = sess.get(url=user_url, headers=HEADERS)

    if response.status_code != 200:
        print "[ERROR]: Could not assign user photo. Response from server: {}".format(response.content)
        sys.exit(1)

    user = json.loads(response.content)

    del user["is_premium"]  # read only
    del user["email_verified"]  # read only
    user.update({"photo": photo_url})

    response = sess.put(url=user_url,
                        data=json.dumps(user),
                        headers=HEADERS)

    if response.status_code != 200:
        print "[ERROR]: Could not assign user photo. Response from server: {}".format(response.content)
        sys.exit(1)
