*** Settings ***
Resource    ../Resources/oneTwoButtonsResources.robot

*** Test Cases ***
TC-1 Open page and press start button
    [Tags]    TC-1    buttonsPage    StartButton
    When User navigates to buttons page
    Then User press Start button
    And User press One button
    And User can see button Two

*** Keywords ***
User navigates to buttons page
    Navigate to buttonsPage  
User press Start button
    Press Start Button
User press One button
    Press One button
User can see button Two
    Validate if button Two Is Visible

