"""
space.py -- functions for operating on spaces.

A "Space" is a leasable unit that resides in "Building".
"""
import json
import sys

import constants


def create_space(sess, current_space, current_building):
    """
    Makes a space in the building for the current user.

    HOW:
        POST the Space payload
        JSON encoded
        TO /api/v1/spaces

    NOTES:
        To properly create a Space within a Building you need to pass the
        "building_key" as part of the JSON payload.
    """
    create_space_url = "/".join([constants.BASE_API_URL, "spaces"])
    # Update the space description to add a pointer to the building.
    # This is how we track which space belongs in which building.
    current_space.update({"building_key": current_building.get("key")})

    response = sess.post(create_space_url,
                         data=json.dumps(current_space),
                         headers=constants.HEADERS)

    if response.status_code != 200:
        print "[ERROR]: There was an error creating the sample space."
        print "[ERROR]: Server response: {}".format(response.content)
        sys.exit(1)

    resp_data = json.loads(response.content)
    return resp_data


def add_contact_to_space(sess, current_space, current_user):
    """
    Adds a user as a contact to this space.

    HOW:
        POST the user payload
        JSON encoded
        TO /api/v1/spaces/<keystring>/contacts
    """
    add_contact_url = "/".join([
        constants.BASE_API_URL,
        "spaces",
        current_space.get("key"),
        "contacts"])

    user_payload = {
        "user": current_user.get("key")
    }

    response = sess.post(
        add_contact_url,
        data=json.dumps(user_payload),
        headers=constants.HEADERS)

    if response.status_code != 200:
        print "[ERROR]: There was an error adding another contact to a space."
        print "[ERROR]: Server response: {}".format(response.content)
        sys.exit(1)
