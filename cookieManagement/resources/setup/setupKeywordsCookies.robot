*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Open Chrome Window And Navigate To
    [Arguments]     ${url}      ${head}=${False}

    IF    ${head}
        ${browser}=     Set Variable    Chrome
    ELSE
        ${browser}=     Set Variable    headlesschrome
    END

    Open Browser    ${url}      browser=${browser}