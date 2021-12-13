Feature: Test get user
    Scenario: An authenticated user can get email address of a Github acct.
    '''
    This is a test of the Github /users/{username} API endpoint.
    '''
        Given I am an authenticated user
        When I query the user data for "fatalaijon"
        Then the email is "fatalaijon@gmail.com"
        And the name is "Jon Fatalai"
