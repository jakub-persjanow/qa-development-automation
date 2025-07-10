*** Settings ***
Resource    ../resources/resourcesCookies.robot

*** Test Cases ***
TC-1 Open page and take Screenshot
    [Tags]    TC-1    adminPage    addRoleCookie
    When User Navigates to adminPage
    Then User Sets Role Cookie To Admin
    And User Deletes Role Cookie Value
    And User Sets Role Cookie To SuperAdmin


TC-2 Open page, get header
    [Tags]    TC-2    adminPage    addRoleCookie    getHeader
    When User Navigates to adminPage
    Then User Sets Role Cookie To Admin
    And User Gets Admin Header Value
    And User Deletes Role Cookie Value
    And User Sets Role Cookie To SuperAdmin
    And User Navigates To SuperAdmin Page
    And User Gets SuperAdmin Header

*** Keywords ***
User Navigates to adminPage
    Navigate To adminPage
User Sets Role Cookie To Admin
    Add Admin Role Cookie Value And Reload Page
User Deletes Role Cookie Value
    Delete Cookie Representing Role Value
User Sets Role Cookie To SuperAdmin
    Add SuperAdmin Role Cookie Value And Reload Page
User Gets Admin Header Value
    Get Admin Header
User Navigates To SuperAdmin Page
    Navigate to SuperAdmin page And Get Header
User Gets SuperAdmin Header
    Get SuperAdmin Header


