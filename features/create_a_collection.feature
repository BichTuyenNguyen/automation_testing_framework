Feature: Create A Collection
  As a user
  I will check to create the collection with required field

  @id-4 @create-a-collection-with-required-field
  Scenario Outline: Create a collection with required field
    When the user send a post request to create a collection with below params
      | title   | description   | private   |
      | <title> | <description> | <private> |
    Then the status of response should be "201"
    And the information of new created collection is the same as input data


    Examples:
      | title               | description                         | private |
      | my first collection | create new collection to save photo | False   |




