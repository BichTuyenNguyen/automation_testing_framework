Feature: Like A Photo
  As a user
  I will check liking a photo Likes field will be increased

  @id-2 @like-a-photo-with-specific-id
  Scenario: Like a photo with specific ID
    When the user like a photo "z0L0mo__9bg"
    Then the status of response should be "201"
    And the Likes field of photo "z0L0mo__9bg" is increased!

