*** Settings ***
Resource    ../resources/setup/SetupKeywords.robot
Force Tags  copy


*** Test Cases ***
TC-1-COPY    
    [Setup]     Open Chrome Window And Navigate To    url=https://www.wp.pl/
    Wait Until Element Is Visible    //*[@id="root"]
    Capture Element Screenshot  //h3[contains(text(), "Cenimy Twoją prywatność")]
    Capture Page Screenshot