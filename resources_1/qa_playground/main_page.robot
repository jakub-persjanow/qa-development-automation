*** Settings ***
Resource    ../setup/SetupKeywords.robot
Library     SeleniumLibrary

*** Variables ***
${MAIN_URL}     https://qaplayground.dev
${MINI_APPS_BUTTON}     //a[contains(text(), "Mini Web Apps")]
${DYNAMIC_TABLE_APP}    //a[contains(@href, "dynamic-table")]
${NEW_TAB_APP}          //a[contains(@href, "new-tab")]

*** Keywords ***
Navigate To QA Playground
    [Arguments]     ${head}=${False}
    Open Chrome Window And Navigate To  
    ...     url=${MAIN_URL}     
    ...     head=${head}

Navigate To Mini Apps
    Wait Until Element Is Visible    ${MINI_APPS_BUTTON} 
    Click Element    ${MINI_APPS_BUTTON} 

Navigate To Dynamic Table App
    Wait Until Element Is Visible    ${DYNAMIC_TABLE_APP} 
    Click Element    ${DYNAMIC_TABLE_APP} 

Navigate To New Tab App
    Wait Until Element Is Visible    ${NEW_TAB_APP} 
    Click Element    ${NEW_TAB_APP} 