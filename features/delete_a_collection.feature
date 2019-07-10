Feature: Delete A Collection
  As a user
  I will check delete a collection successfully

  @id-5 @delete-a-collection-with-specific-id
  Scenario Outline: Delete a pre-created collection
    Given the user create new collection with data below
      | title   | description   | private   |
      | <title> | <description> | <private> |
    When the user delete the newly created collection
    Then the status of response should be "204"

    Examples:
      | title               | description                         | private |
      | my first collection | create new collection to save photo | False   |

