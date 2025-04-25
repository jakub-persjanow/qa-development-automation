*** Settings ***
Resource    ../resources/setup/SetupKeywords.robot
# Test Setup  Open Chrome Window And Navigate To    url=https://www.wp.pl/
Test Teardown   Close All Browsers
Force Tags  whole-suite


*** Test Cases ***
TC-1    
    [Tags]      wp-test
    [Setup]     Open Chrome Window And Navigate To    url=https://www.wp.pl/
    Wait Until Element Is Visible    //*[@id="root"]
    Capture Element Screenshot  //h3[contains(text(), "Cenimy Twoją prywatność")]
    Capture Page Screenshot

TC-2
    [Setup]     Open Chrome Window And Navigate To    url=https://www.onet.pl/
    [Tags]      run-together
    Wait Until Element Is Not Visible    //h3[contains(text(), "Cenimy Twoją prywatność")]
    Page Should Not Contain     Cenimy Twoją prywatność
    Capture Page Screenshot
    [Teardown]      Log    Browser not closing - TC3 is dependent
    
TC-3
    [Tags]      run-together
    Capture Page Screenshot
    Page Should Contain    Szanowna Użytkowniczko
