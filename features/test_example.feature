Feature: Test boolean

    Just test boolean
    Scenario: When I want to check for a boolean
        Given I have boolean True
        When I put and condition with False
        Then The result will be False
        