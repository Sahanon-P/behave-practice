import requests
from behave import *
from decouple import config
from hamcrest import assert_that, equal_to

@given('I am an authenticated user')
def step_impl(context):
    context.TOKEN = config('ACCESS_TOKEN')

@when('I query the user data for "{user}"')
def step_impl(context, user):
    headers = {
        "Authorization": "token " + context.TOKEN
    }
    context.response = requests.get(f"https://api.github.com/users/{user}", headers=headers)

@then('the "{key}" is "{value}"')
def step_impl(context, key, value):
    result = context.response.json()[key]
    assert_that(check_empty(value), equal_to(result))

def check_empty(value):
    if value == "None":
        return None
    return value