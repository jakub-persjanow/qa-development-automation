*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${URL}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Keywords ***
Open Chrome Window And Navigate To
    [Arguments]     ${url}=${URL}      ${head}=${False}

    IF    ${head}
        ${browser}=     Set Variable    Chrome
    ELSE
        ${browser}=     Set Variable    headlesschrome
    END

    Open Browser    ${url}      browser=${browser}
    Set Window Size    1440    720