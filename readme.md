# Unsplash Selenium

This is a program that supports automatic testing of unsplash API.

## Introducing
**Library:** Selenium 3.141.0

**Programing language:** Python 3.7

**Automation Framework:** Behave

## Application for the testing:

**Application:** https://unsplash.com

**API documentation:** https://unsplash.com/documentation

## Test scenario list:

1. Check the user's full name after login to the application

2. Check that the user's location is correct after updated

3. Check that the image's camera model and focal length are correct

4. Check that all related tags of a collection are correct

5. Check that the user can create a new collection and add a photo into it.

6.  Check that the image is downloadable and the correct image has been saved when the user clicks on Download button

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

URL clone: **https://gitlab.com/duynguyenx/de21.git**

### Prerequisites
What you need to prepare as:

1. Operating system: Window 10

2. IDE Pycharm:

**https://www.jetbrains.com/pycharm/download/**

3. Python:

**https://www.python.org/downloads/**

### Installing

Open command line in  project's location and follow examples below.

Setup pip:
```
 > python -m pip install -U pip
```

Setup virtualenv environment:
```
 > pip install virtualenv
 > virtualenv venv
 > venv\Script\activate
```

Install packages:

```
 > pip install -r requirements.txt
```

## Running the tests

Run all behave:

```
@behave
```

Run any behave by tag:

```
@behave -k -t [tag]
```
    _Example_: @behave -k -t id-1

After running the scenario, you will see if the test result is successful or not.

## Report using Junit Behave 

**behave** provides reporting results of a test run by Junit

You can open **junit-reports** folder and open any html report file with browser to show the report.

Or you follow step by step below to generate a new Junit report on command line:

Open project folder and activate your environment:

```
 > venv\Script\activate
```

Generate junit behave report (Default all XML reports will save at reports/):

```
 > behave --junit
```

Parse XML file to HTML file:

```
 > python -m junit2htmlreport [JUNIT_XML_FILE] [JUNIT_HTML_FILE]
```
    _Example_: python -m junit2htmlreport reports/TESTS-check_collection_handle.xml junit-reports/TESTS-check_collection_handle.html

Finally, open html report file with any browser.

## Report using Allure Behave 

You can open **allure-report/index.html** and open with any browser to show the report.

Or you follow step by step below to generate a new Allure report on command line:

Specify the formatter directly in the command line:

```
 >  behave -f allure_behave.formatter:AllureFormatter -o allure-results 
```

Open the allure report:

```
 >  allure serve 
```

Generate the allure report:

```
 >  allure generate
```