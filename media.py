"""
media.py -- media handling for marketing spaces and buildings.

This file is used to upload media (images/pdfs) to Spaces and Buildings
for their marketing presentation.

To upload an image for a Space or a Building follow these steps:
  * Upload the image to our server by POSTing to /upload
  * Take that response payload, add the target key and POST that to
      /api/v1/spaces/<keystring>/attachments
  * Make sure the attachments call's header specifies Content-Type
      as application/json.
"""
import json
import sys

import constants


def assign_media(sess, target, target_type, img_path):
    """
    Uploads and sets a picture for this target. The target is a Building or
    Space.

    HOW:
    1. POST the image (upload it)
       TO /upload

    2. Store the response from the server.

    3. Add "target" to the response. Target is a keystring that points to the
       Building or Space to which you want to assign this media.

    4. POST the modified response
       JSON encoded
       TO /api/buildings/<keystring>/attachments for a Building
         or
       TO /api/spaces/<keystring>/attachments for a Space.

    PARAMS
        target : (string, key) target space or building key
        target_type : (string, "spaces" or "buildings")
        img_path : (string) path to file to upload
    """
    media_upload_url = "/".join([constants.BASE_URL, "upload"])
    media_assign_url = "/".join([constants.BASE_API_URL,
                                 target_type,
                                 target.get("key"),
                                 "attachments"])
    response = None

    # open the file and upload it
    with open(img_path, 'rb') as img_file:
        img_payload = {"file": img_file}
        response = sess.post(
            media_upload_url,
            files=img_payload,
            headers=constants.HEADERS,
            verify=False)

        if response.status_code != 200:
            print "[ERROR]: There was an error uploading media."
            print "[ERROR]: Server response: {}".format(response.content)
            sys.exit(1)

    resp_data = json.loads(response.content)
    resp_data["target"] = target.get("key")

    media_headers = constants.HEADERS.copy()
    media_headers.update({"Content-Type": "application/json"})

    response = sess.post(media_assign_url,
                         data=json.dumps(resp_data),
                         headers=media_headers)
