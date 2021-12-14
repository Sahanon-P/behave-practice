from behave   import *
from hamcrest import assert_that, equal_to


def parse_boolean(text):
    if text.lower() == 'true':
        return True
    elif text.lower() == 'false':
        return False
    raise ValueError('Expect True or False, got {}'.format(text))


register_type(boolean=parse_boolean)

@given('I have boolean {x:boolean}')
def given_bool(context, x):
    context.result = x

@when('I put and condition with {y:boolean}')
def and_condition(context, y):
    context.result = context.result and y

@then('The result will be {expected:boolean}')
def show_result(context, expected):
    assert_that(expected, equal_to(context.result))