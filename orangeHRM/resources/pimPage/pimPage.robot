*** Settings ***
Resource    ../setup/setupKeywordsOrange.robot
Library    SeleniumLibrary
Library    Collections

*** Variables ***

${Table_Body}    //div[contains(@class,'oxd-table-body')]
${Table_row}    //div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')]
${Row_cell}    .//div[contains(@class,'oxd-table-cell oxd-padding-cell')]

*** Keywords ***

Get data from table
    Wait Until Element Is Visible    ${Table_Body}
    ${rows}=    Get WebElements    ${Table_row}
    ${count}=    Get Length          ${rows}
    ${end}=    Evaluate            ${count} + 1
    ${table_data}=    Create List

    FOR    ${i}    IN RANGE    1    ${end}
        ${id}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][2]
        ${first_middle}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][3]
        ${last_name}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][4]
        ${job_title}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][5]
        ${employment_status}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][6]
        ${sub_unit}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][7]
        ${supervisor}=    Get Text    xpath=(//div[contains(@class,'oxd-table-row oxd-table-row--with-border oxd-table-row--clickable')])[${i}]//div[contains(@class,'oxd-table-cell')][8]

        ${row_dict}=    Create Dictionary
        ...    ID=${id}
        ...    First (& Middle) Name=${first_middle}
        ...    Last Name=${last_name}
        ...    Job Title=${job_title}
        ...    Employment Status=${employment_status}
        ...    Sub Unit=${sub_unit}
        ...    Supervisor=${supervisor}

        Append To List    ${table_data}    ${row_dict}
    END

    Log    ${table_data}
    RETURN  ${table_data}
    