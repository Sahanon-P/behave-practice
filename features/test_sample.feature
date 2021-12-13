# file:features/tutorial10_step_usertype.feature
Feature: User-Defined Datatype as Step Parameter (tutorial10)

  As a test writer
  I want that a step parameter is converted into a specific datatype
  to simplify the programming of the step definition body.

  Scenario: Calculator
    Given I have a calculator
    When I mutiply "2" and "3"
    Then the calculator returns "6"
