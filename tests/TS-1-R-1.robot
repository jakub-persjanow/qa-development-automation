*** Settings ***
Resource    ../resources/resources1.robot

*** Test Cases ***
TC-1 Validate Dynamic Table Mini App Header
    [Tags]  TC-1    dynamic_table_app
    When User Navigates To Dynamic Table Mini App
    Then User Can See Dynamic Table Header With Proper Columns

TC-2 Validate Dynamic Table Mini App Row - Ant-Man
    [Tags]  TC-2    dynamic_table_app   ant_man
    When User Navigates To Dynamic Table Mini App
    Then User Can See Ant-Man In The Table

TC-3 Validate Dynamic Table Mini App Row - All rows
    [Tags]  TC-3    dynamic_table_app all_rows
    When User Navigates To Dynamic Table Mini App
    Then User Can See All The Rows In The Table
    And User Can See Correct Amount Of Heroes

*** Keywords ***
User Navigates To Dynamic Table Mini App
    Navigate To QA Playground
    Navigate To Mini Apps
    Navigate To Dynamic Table App

User Can See Dynamic Table Header With Proper Columns
    Dynamic Table Header Is Visible And Contains Proper Columns
    Capture Element Screenshot    ${DYNAMIC_TABLE_HEADER}

User Can See Ant-Man In The Table
    Dynamic Table Row Contains Superhero
    ...     superhero_name=Ant-Man 
    ...     email=ant-man@avengers.com
    ...     status=Active
    ...     real_name=Eric O'Grady

User Can See All The Rows In The Table
    FOR    ${dict}    IN    @{LIST_OF_SUPERHEROS}
        Log Dictionary    ${dict}
        Dynamic Table Row Contains Superhero
            ...     superhero_name=${dict["superhero_name"]}
            ...     email=${dict["email"]}
            ...     status=${dict["status"]}
            ...     real_name=${dict["real_name"]} 
    END

User Can See Correct Amount Of Heroes
    ${expected_number_of_heros}=  Get Length   ${LIST_OF_SUPERHEROS}
    Dynamic Table Contains Number Of Rows    ${expected_number_of_heros}
