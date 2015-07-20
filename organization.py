"""
organization.py -- allows you to add other users to your organization.
"""
import json
import sys

import constants


def add_user_to_org(sess, user, org):
    """
    Add user to a given org.

    HOW:
        POST the user payload
        JSON encoded
        TO /api/v1/organizations/<keystring>/invitations

    NOTE:
        If the user is already in this organization we strangely return a
        status code of 500 and a warning in the response body. We'll fix
        this soon.
    """
    add_user_to_org_url = "/".join([constants.BASE_API_URL,
                                    "organizations",
                                    org,
                                    "invitations"])
    payload = {"email": user}

    response = sess.post(add_user_to_org_url,
                         data=json.dumps(payload),
                         headers=constants.HEADERS)

    if response.status_code == 500:
        reason = json.loads(response.content).get("error")
        if reason == "User already belongs to this organization.":
            print "[WARN]: User is already in the organization."
        return
    elif response.status_code != 200:
        print "[ERROR]: There was an error adding user to organization."
        print "[ERROR]: Server response: {}".format(response.content)
        sys.exit(1)
