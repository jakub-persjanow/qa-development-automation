*** Settings ***
Resource  ../Setup/keywordsButtons.robot
Library    SeleniumLibrary

*** Variables ***

*** Variables ***

${MAIN_URL}    https://testpages.eviltester.com/styled/dynamic-buttons-simple.html
${buttonStart}    //button[contains(text(), "start")]
${buttonOne}    //button[contains(text(), "One")]
${buttonTwo}    //button[contains(text(), "Two")]

*** Keywords ***

Navigate to buttonsPage
    [Arguments]     ${head}=${False}
    Open Chrome Window And Navigate To  
    ...     url=${MAIN_URL}     
    ...     head=${head}
Press Start Button
    Element Attribute Value Should Be    ${buttonStart}    id    button00
    Capture Page Screenshot
    Click Element    ${buttonStart}
Press One button
    Wait Until Element Is Visible    ${buttonOne}
    Capture Page Screenshot
    Click Element    ${buttonOne}
Validate if button Two Is Visible
    Wait Until Element Is Visible    ${buttonTwo}
    Capture Page Screenshot
