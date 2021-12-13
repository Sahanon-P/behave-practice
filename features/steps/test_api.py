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

@then('the email is "{email}"')
def step_impl(context, email):
    result = context.response.json()['email']
    assert_that(check_empty(email), equal_to(result))

@then('the name is "{name}"')
def step_impl(context, name):
    result = context.response.json()['name']
    assert_that(name, equal_to(result))

def check_empty(value):
    if value == "None":
        return None
    return value