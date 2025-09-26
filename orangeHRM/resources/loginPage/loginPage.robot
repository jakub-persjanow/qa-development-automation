*** Settings ***
Resource    ../setup/setupKeywordsOrange.robot
Library    SeleniumLibrary

*** Variables ***

${User_name_input}    //input[contains(@name,'username')]
${Password_input}    //input[contains(@name,'password')]
${Login_button}    //button[contains(@type,'submit')]
${User_pill}    //p[contains(text(),'manda user')]
${PIM_page_button}    //a[contains(@href, "/web/index.php/pim/viewPimModule")]

*** Keywords ***

Navigate to login page and login user
    Wait Until Element Is Visible    ${User_name_input}
    Wait Until Element Is Visible    ${Password_input}
    Wait Until Element Is Visible    ${Login_button}
    Input Text    ${User_name_input}     Admin
    Input Text    ${Password_input}    admin123
    Click Button    ${Login_button}
User is logged in
    Wait Until Element Is Visible    ${User_pill}
    Capture Page Screenshot
Navigate to PIM page
    Wait Until Element Is Visible    ${PIM_page_button}
    Click Element    ${PIM_page_button}
    
