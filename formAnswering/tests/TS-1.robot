*** Settings ***
Library     ../resources/FormKeywords.py
Library     SeleniumLibrary

*** Test Cases ***
TC-1
    When User Navigates To Form
    Then User Can See Form Inputs

*** Keywords ***
User Navigates To Form
    [Arguments]     ${url}=https://docs.google.com/forms/d/e/1FAIpQLSdQf7tWySiRVt9G7DYKHLK9sgfO9CZp7pUNv58ECqvJmCuMQw/viewform
    Open Chrome Window And Navigate To      ${url}

User Can See Form Inputs
    ${form}=    get_form_object     header_text=Test Form   name_header_text=Name        email_header_text=Email
    Wait Until Element Is Visible   ${form.header}
    Wait Until Element Is Visible   ${form.name}
    Wait Until Element Is Visible   ${form.email}
    Capture Page Screenshot
    Set Test Variable    ${TEST_FORM}   ${form}

Open Chrome Window And Navigate To
    [Arguments]     ${url}      ${head}=${False}

    IF    ${head}
        ${browser}=     Set Variable    Chrome
    ELSE
        ${browser}=     Set Variable    headlesschrome
    END

    Open Browser    ${url}      browser=${browser}