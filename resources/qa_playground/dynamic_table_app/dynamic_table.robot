*** Settings ***
Library     SeleniumLibrary
Resource    ./dynamic_table_xpaths.robot


*** Keywords ***
Dynamic Table Header Is Visible And Contains Proper Columns
    Wait Until Element Is Visible   ${DYNAMIC_TABLE_HEADER} 


Dynamic Table Row Contains Superhero
    [Arguments]     ${superhero_name}   ${email}    ${status}   ${real_name}
    ${xpath}=   Dynamic Table Row XPath     
    ...     superhero_name=${superhero_name} 
    ...     email=${email}
    ...     status=${status}
    ...     real_name=${real_name}
    Wait Until Element Is Visible    ${xpath}
    Capture Element Screenshot      ${xpath}

Dynamic Table Contains Number Of Rows
    [Arguments]    ${expected_number}
    ${rows}=  Get WebElements    ${DYNAMIC_TABLE_ROW}
    # ${lenght}=  Get Length    ${rows}
    # Should Be Equal As Integers  ${lenght}  ${expected_number}
    Length Should Be  ${rows}    ${expected_number}
    Capture Page Screenshot