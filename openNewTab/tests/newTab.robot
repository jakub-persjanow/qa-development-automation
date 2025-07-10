*** Settings ***
Resource    ../resources/setup/setupKeywordsNewTab.robot

*** Test Cases ***
TC-1 Open New Tab By Pressing The Button
    When User Navigatest to New Tab App Page
    Then User Clicks Open New Tab Button
    And User Is Moved To The New Tab

*** Keywords ***
User Navigatest to New Tab App Page
User Clicks Open New Tab Button
User Is Moved To The New Tab