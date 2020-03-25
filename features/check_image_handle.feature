Feature: Check Image Handing
  As a user
  I log in to Unsplash site
  I check that the image's camera model and focal length are correct
  I check that all related tags of a image are correct
  I check that the image is downloaded and exist in system

  @id-3 @check-image @check-image-information
  Scenario Outline: Check that the image's camera model and focal length are correct
    Given the user logs in successfully with <username>
    When the user opens an image with ID using this <url>
    And the user clicks on Info button
    Then the user should see the image's info as below
      | camera_model | focal_length |
      | Canon EOS 6D | 24.0mm       |

    Examples:
      | username | url                                     |
      | tuyen    | https://unsplash.com/photos/2TLREZi7BUg |


  @id-4 @check-image @check-image-related-tags
  Scenario Outline: Check that all related tags of a image are correct
    Given the user logs in successfully with <username>
    When the user opens an image with ID using this <url>
    Then the user should see all related tags of the image

    Examples:
      | username | url                                     |
      | tuyen    | https://unsplash.com/photos/E6PWA9GvIBU |


  @id-6 @check-image @check-image-downloadable
  Scenario Outline: Check that the image is downloaded and exist in system
    Given the user logs in successfully with <username>
    When the user opens an image with ID using this <url>
    And the user downloads image
    Then the user notices that the image is downloadable and the correct image has been saved

    Examples:
      | username | url                                     |
      | tuyen    | https://unsplash.com/photos/2TLREZi7BUg |


  @id-7 @check-image @check-image-downloadable-with-hashcode
  Scenario Outline: Check that the image is downloaded and exist in system
    Given the user logs in successfully with <username>
    When the user opens an image with ID using this <url>
    And the user downloads image using API
    Then the user notices that the hashcode of image is the same with <expected_hashcode>

    Examples:
      | username | url                                     | expected_hashcode                |
      | tuyen    | https://unsplash.com/photos/2TLREZi7BUg | 5fa251cfe7cd7c4c99529bb74f2f3d51 |



