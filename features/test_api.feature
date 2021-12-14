Feature: Test API
    Background: Authentication
        Given I am an authenticated user
    Scenario Outline: An authenticated user can get email address of a Github acct.
    '''
    This is a test of the Github /users/{username} API endpoint.
    '''
        When I query the user data for <username>
        Then the email is <email>
        And the name is <name>
    Examples:
        | username       | email                | name                 |
        | fatalaijon     | fatalaijon@gmail.com | Jon Fatalai          |
        | parujr         | None                 | Paruj Ratanaworabhan |

    Scenario: An authenticated user can get repo name of a Github acct.
        When I query the repo data name guessing_game of Sahanon-P
        Then repo full_name is Sahanon-P/guessing_game  
