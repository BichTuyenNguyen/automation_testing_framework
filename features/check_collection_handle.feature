Feature: Check User Adds A Photo To Collection
  As a user
  I will create a new collection and add a photo to it

  @id-5 @check-add-photo-to-collection
  Scenario Outline: Check that the user can create a new collection and add a photo into it
    Given the user logs in successfully with <username>
    And the user creates a new collection using API with below params
      | title   | description   | private   |
      | <title> | <description> | <private> |
    And the user add a photo with <photo_id> into the added collection using API
    When the user clicks on the added photo to the collection
    Then the user notices that the ID of photo in URL is correct

    Examples:
      | username | title   | description      | private | photo_id    |
      | tuyen    | 2172019 | testing selenium | False   | 2TLREZi7BUg |


