Feature: Get A Collection
  As a user
  I will check the information of any collection is correct

  @id-3 @get-a-collection-with-specific-id
  Scenario: Get a collection information with specific ID
    When the user get information of collection "6289405"
    Then the status of response should be "200"
    And the information of collection "6289405" is shown as below
      | title        | total_photos | description                         | published_at              | updated_at                |
      | my first col | 2            | create new collection to save photo | 2019-07-01T23:35:40-04:00 | 2019-07-07T21:56:21-04:00 |







