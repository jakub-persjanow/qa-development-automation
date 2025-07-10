*** Settings ***
Resource    /Users/demiangela/Desktop/repoAuto/qa-development-automation/cookieManagement/resources/setup/setupKeywordsCookies.robot
Library     SeleniumLibrary

*** Variables ***

${MAIN_URL}    https://testpages.eviltester.com/styled/cookies/adminlogin.html
${SuperAdminButton}    //a[contains(text(), "Super Admin View")]
${AdminHeader}    //h1[contains(text(), "Admin View")]
${SuperAdminHeader}    //h1[contains(text(), "Super Admin View")]


*** Keywords ***
Navigate To adminPage
    [Arguments]     ${head}=${False}
    Open Chrome Window And Navigate To  
    ...     url=${MAIN_URL}     
    ...     head=${head}
Add Admin Role Cookie Value And Reload Page
    Add Cookie    loggedin    Admin
    Reload Page
    ${cookies}=  Get Cookies
    Log Many    ${cookies}    console=${True}
    Capture Page Screenshot
Delete Cookie Representing Role Value
    Delete Cookie    loggedin
    Reload Page
    ${cookies}=  Get Cookies
    Log Many    ${cookies}    console=${True} 
Add SuperAdmin Role Cookie Value And Reload Page
    Add Cookie    loggedin    SuperAdmin
    Reload Page
    ${cookies}=  Get Cookies
    Log Many    ${cookies}    console=${True}
    Capture Page Screenshot
Navigate to SuperAdmin page And Get Header
    Element Attribute Value Should Be    ${SuperAdminButton}    href    https://testpages.eviltester.com/styled/cookies/superadminview.html
    Click Element    ${SuperAdminButton}
Get SuperAdmin Header
    Wait Until Element Is Visible    ${SuperAdminHeader}
    Capture Page Screenshot
Get Admin Header
    Wait Until Element Is Visible    ${AdminHeader}
    Capture Page Screenshot