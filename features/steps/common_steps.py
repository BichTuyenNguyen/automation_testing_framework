from behave import then
from hamcrest import assert_that


@then('the status of response should be "{status}"')
def check_response_status(context, status):
    expected_result = status
    actual_result = context.response.status_code
    assert_that(actual_result, expected_result, "Assert the status response")
