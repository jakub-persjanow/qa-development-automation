*** Settings ***
Resource    ../resources/loginPage/loginPage.robot
Resource    ../resources/pimPage/pimPage.robot
Resource    ../resources/setup/setupKeywordsOrange.robot
Library     ../resources/data_parser.py

*** Test Cases ***
TC-1 Login user
    Given Open Chrome Window And Navigate To
    When Navigate to login page and login user
    Then User is logged in 

TC-2 Get table data
    Given Open Chrome Window And Navigate To
    When Navigate to login page and login user
    Then Navigate to PIM page
    And Get data from table and parse

*** Keywords ***
Get data from table and parse
    ${data}=    Get data from table
    parse_data_to_dataframe     ${data}