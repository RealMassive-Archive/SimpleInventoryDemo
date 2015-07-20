import json
import sys

import constants


def create_building(sess, building_info, user_info):
    """
    Creates a building given the building data.

    HOW:
        1. POST the building payload
           JSON encoded
           TO /api/v1/buildings

    NOTES:
        Buildings can be created in two statuses: "Claimed" and "Unclaimed."
        A claimed building is managed by your organization. When POSTing the
        building information, add "manager" which is your organization's key.
        If the key if left out, the Building will be unclaimed. Anyone can
        then come claim this building.
    """
    create_building_url = "/".join([constants.BASE_API_URL, "buildings"])
    building_payload = building_info

    org_key = user_info.get("organizations")[0]
    # this "claims" the building by this organization
    building_payload.update({"manager": org_key})

    response = sess.post(create_building_url,
                         data=json.dumps(building_payload),
                         headers=constants.HEADERS)

    if response.status_code != 200:
        print "[ERROR]: There was an error creating the sample building."
        print "[ERROR]: Server response: {}".format(response.content)
        sys.exit(1)

    resp_data = json.loads(response.content)
    return resp_data
