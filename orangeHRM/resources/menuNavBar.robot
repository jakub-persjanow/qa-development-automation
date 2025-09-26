*** Settings ***
Library    SeleniumLibrary
*** Variables ***

${PIM_button}    //a[contains(@href,"PimModule")]
${PIM_header}    //h6[text()="PIM"]

*** Keywords ***
Navigate to PIM module 
    Click Link    ${PIM_button}
    Wait Until Element Is Visible    ${PIM_header}