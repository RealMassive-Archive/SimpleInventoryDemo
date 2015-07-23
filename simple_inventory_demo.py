"""
simple_inventory_demo.py -- creates and populates a small organization.

This is a simple demo that shows you how to manage your invetory using the
RealMassive API. It starts by creating a user. Then, it creates buildings
and spaces for that user. It also uploads media for these buildings and
spaces.

GitHub Repo: https://github.com/inchoate/SimpleInventoryDemo
"""
import time

import building
import constants
import media
import organization
import space
import tests
import user


if __name__ == '__main__':
    if not tests.check():
        tests.usage()

    # Step 1. Create a User (see user.py::create_user)
    user.create_user(constants.EXAMPLE_USER)

    # Step 2. Login as the user (see user.py::login_user)
    current_sess, current_user = user.login_user(constants.EMAIL,
                                                 constants.PASSWORD)
    time.sleep(1)

    # Step 3. Optional, but strongly suggested, give the user a photo.
    #         (see user.py::assign_user_photo)
    user.assign_user_photo(
        current_sess,
        user=current_user,
        photo_url="http://real.ma/1ehANvQ")

    # Step 4. Create a Building
    BUILDING_INFO = building.create_building(current_sess,
                                             constants.EXAMPLE_BUILDING,
                                             current_user)
    time.sleep(1)

    # Step 7. Upload media and attach it to the Building
    media.assign_media(current_sess,
                       BUILDING_INFO,
                       "buildings",
                       constants.SPACE_IMG_PATH)
    time.sleep(1)

    # Step 5. Create a Space in this Building
    SPACE_INFO = space.create_space(current_sess,
                                    constants.EXAMPLE_SPACE,
                                    BUILDING_INFO)
    time.sleep(1)

    # Step 6. Optional, invite a user to join your organization
    # so you can add him/her as a contact on a listing.
    additional_user = "jason.vertrees+api7@realmassive.com"
    organization.add_user_to_org(current_sess,
                                 additional_user,
                                 current_user.get("organizations")[0])
    time.sleep(1)

    # Step 6. Optional, add another contact to this Space.
    # NOTE: User must be a RealMassive user.
    space.add_contact_to_space(current_sess,
                               SPACE_INFO,
                               current_user)
    time.sleep(1)

    # Step 7. Upload media and attach it to the space
    media.assign_media(current_sess,
                       SPACE_INFO,
                       "spaces",
                       constants.BUILDING_IMG_PATH)
