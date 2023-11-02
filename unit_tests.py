from functions import add


def test_add():
    '''
    Input: No Input
    Output: Assertion of test result
    Function to test the functionality of the add function
    '''
    # Define input variable
    x = 3
    y = 4

    # Define expected result
    expected_result = 7

    # Check function result with expected result
    assert add(x, y) == expected_result
