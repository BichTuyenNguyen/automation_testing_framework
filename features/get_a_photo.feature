Feature: Get A Photo
  As a user
  I will check the information of any photo is correct

  @id-1 @get-photo-with-specific-ID
  Scenario: Get a photo information with specific ID
    When the user get information of photo "nXN1MorbCRY"
    Then the status of response should be "200"
    And  the information of photo "nXN1MorbCRY" is shown as below
      | width | height | description | focal_length | iso |
      | 4480  | 5600   | None        | 24.0         | 100 |





