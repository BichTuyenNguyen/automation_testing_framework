from behave import *
from config.env_setup import EnvSetup
from pageobjects import constants
from pageobjects.login_page import LoginPage
import json


@step('the user goes to login page')
def navigate_login(context):
    LoginPage(context.driver).navigate(constants.LOGIN_PAGE["NAVIGATE_LOGIN"].format(site=EnvSetup.SITE))


@step("the user enters his email {email}")
def enter_user_email(context, email):
    LoginPage(context.driver).input_user_email(constants.LOGIN_PAGE["USER_EMAIL"], email)


@step("the user enters his password {password}")
def enter_user_password(context, password):
    LoginPage(context.driver).input_user_password(constants.LOGIN_PAGE["USER_PASSWORD"], password)


@step("the user clicks the commit button")
def click_commit_button(context):
    LoginPage(context.driver).go_to_login_page(constants.LOGIN_PAGE["LOGIN_COMMIT_BUTTON"])


@given("the user logs in successfully with {username}")
def login(context, username):
    email = ""
    password = ""
    try:
        with open("./config/sample_user.json") as read:
            read_file = json.load(read)
            email = read_file[username]["email"]
            password = read_file[username]["password"]
            context.username = read_file[username]["username"]
    except FileNotFoundError:
        print("File path does not exist.")

    context.execute_steps('''
        Given the user goes to login page
        and the user enters his email {email}
        and the user enters his password {password}
        and the user clicks the commit button
        '''.format(email=email, password=password))

