from behave   import given, when, then
from hamcrest import assert_that, equal_to

@given('I have a calculator')
def given_calculator(context):
    pass

@when('I mutiply {x:d} and {y:d}')
def multiply(context, x, y):
    context.result = x*y

@then('the calculator returns {expected:d}')
def result(context, expected):
    assert_that(context.result, equal_to(expected))