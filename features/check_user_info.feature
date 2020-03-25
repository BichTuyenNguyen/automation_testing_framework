Feature: Check User Information
  As a user
  I log in to Unsplash site
  I check my user's full name is correct
  I update my location to Vietnam


  @id-1 @check-user @check-user-name
  Scenario Outline: Check the user's full name after login to the application
    Given the user logs in successfully with <username>
    When the user goes to Collection page
    Then the user able to see <full_name> is displayed

    Examples:
      | username | full_name    |
      | tuyen    | Tuyen Nguyen |


  @id-2 @check-user @check-user-location
  Scenario Outline: Check that the user's location is correct after updated
    Given the user logs in successfully with <username>
    Given the user goes to Edit Profile page
    When the user enters <location> in the location input
    And the user clicks on the Update account button
    Then the user should see the updated location is <location>

    Examples:
      | username | location |
      | tuyen    | Vietnam  |