*** Variables ***
${DYNAMIC_TABLE_HEADER}    //thead//*[contains(text(), "Superhero")]/following::*[contains(text(), "Status")]/following::*[contains(text(), "Real Name")]
@{LIST_OF_SUPERHEROS}=    
...    &{DICT1}    &{DICT2}    &{DICT3}    &{DICT4}    &{DICT5}    &{DICT6}    &{DICT7}    &{DICT8}  
&{DICT1}    superhero_name=Ant-Man    email=ant-man@avengers.com    status=Active    real_name=Eric O'Grady
&{DICT2}    superhero_name=Black Widow    email=black-widow@avengers.com    status=Active    real_name=Natasha Alianovna Romanova
&{DICT3}    superhero_name=Iron Man    email=iron-man@avengers.com    status=Active    real_name=Anthony 'Tony' Stark
&{DICT4}    superhero_name=Hulk    email=hulk@avengers.com    status=Active    real_name=Robert Bruce Banner
&{DICT5}    superhero_name=Captain America    email=captain-america@avengers.com    status=Active    real_name=Steve Rogers
&{DICT6}    superhero_name=Deadpool    email=deadpool@avengers.com   status=Active    real_name=Wade Wilson
&{DICT7}    superhero_name=Doctor Strange    email=doctor-strange@avengers.com   status=Active    real_name=Stephen Vincent Strange
&{DICT8}    superhero_name=Spider-Man    email=spider-man@avengers.com   status=Active    real_name=Peter Parker
${DYNAMIC_TABLE_ROW}      //tbody/tr

*** Keywords ***
Dynamic Table Row XPath
    [Arguments]     ${superhero_name}   ${email}    ${status}   ${real_name}
    ${xpath}=   Catenate    SEPARATOR=
    ...     //tr//*[contains(text(), "${superhero_name}")]/following::
    ...     *[contains(text(), "${email}")]//following::
    ...     *[contains(text(), "${status}")]//following::
    ...     *[contains(text(), "${real_name}")]
    ...     /../..

    [Return]    ${xpath}

