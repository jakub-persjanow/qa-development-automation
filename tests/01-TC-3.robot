*** Settings ***
Resource    ../resources/setup/SetupKeywords.robot
# Test Setup  Open Chrome Window And Navigate To    url=https://qaplayground.dev/apps/dynamic-table/
Test Teardown   Close All Browsers
Force Tags  whole-suite


*** Test Cases ***
TC-1    
    [Tags]      qaplayground-test
    [Setup]     Open Chrome Window And Navigate To    url=https://qaplayground.dev/apps/dynamic-table/
    Wait Until Element Is Visible    //*
    Capture Element Screenshot  //h1/span[contains(text(), "QA Playground")]
    ${text}    Get Text    xpath=//table/tbody/tr[1]
    Log    The name of the first superhero is: ${text}
    Capture Page Screenshot

TC-2
    [Setup]     Open Chrome Window And Navigate To    url=https://qaplayground.dev/apps/dynamic-table/
    [Tags]      run-together
    Wait Until Element Is Visible    //h1/span[contains(text(), "QA Playground")]
    Page Should Contain     QA Playground
    Capture Page Screenshot
    [Teardown]      Log    Browser not closing - TC3 is dependent
    
TC-3
    [Tags]      run-together
    Capture Element Screenshot    //div[contains(text(), "Iron Man")]
    Capture Page Screenshot
    
