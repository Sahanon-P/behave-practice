import requests
from behave import *
from decouple import config
from hamcrest import assert_that, equal_to

def parse_string(text):
    if text == "None":
        return None
    return text

register_type(string = parse_string)

@given('I am an authenticated user')
def step_impl(context):
    context.TOKEN = config('ACCESS_TOKEN')

@when('I query the user data for {user}')
def step_impl(context, user):
    headers = {
        "Authorization": "token " + context.TOKEN
    }
    context.response = requests.get(f"https://api.github.com/users/{user}", headers=headers)

@then('the {key} is {value:string}')
def step_impl(context, key, value):
    result = context.response.json()[key]
    assert_that(value, equal_to(result))

@when('I query the repo data name {repo_name} of {user}')
def query_data(context, repo_name, user):
    headers = {
        "Authorization": "token " + context.TOKEN
    }
    context.response = requests.get(f"https://api.github.com/repos/{user}/{repo_name}", headers=headers)

@then('repo full_name is {expected}')
def check_result(context, expected):
    result = context.response.json()["full_name"]
    assert_that(result, equal_to(expected))