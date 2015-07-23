# RealMassive API Demo: Simple Inventory Management

This demo shows you how to get started managing your inventory with the RealMassive API. This demo shows you how to:
  * Login
  * Create users for your team
  * Create buildings
  * Create spaces
  * Upload media

## Getting Started
Before you can run the demo you need to complete the following steps:
  * **Create a Development account**: Please visit [https://rm-api-sandbox.appspot.com](https://rm-api-sandbox.appspot.com/) and create an account for yourself there.
  * **Obtain an API Token for your Development account**: Using the above account information, please visit [https://www.realmassive.com/developer-center](https://www.realmassive.com/developer-center/) and apply for a Development API Token. This API token will be valid for your demo account only on the RealMassive Development server (aka RM API Sandbox).

## Running
  * Clone this repo
  * cd SimpleInventoryDemo
  * Please fill in the API token and other constants for your project in ```user_constants.py```.
  * Run: ```python simple_inventory_demo.py```.

## Notes
  * This demo is written for Python 2.7.
  * See our accompanying [API documentation](docs.realmassive.apiary.io).
  * Sadly, we have a bug that requires the "time.sleeps(1)"s. This bug should be fixed by 08/01 at which point we can remove the sleep calls.
