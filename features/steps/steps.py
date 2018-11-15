from behave import *
from twentyone import *
from selene import *

@given('a Google')
def step_impl(context):
    context.google = Google()

@when('open Google page')
def step_impl(context):
    context.google.open_site()

@when('set text in feald')
def step_impl(context):
    context.google.set_text()

@then('see the list result of search')
def step_impl(context):
    context.google.see_list()