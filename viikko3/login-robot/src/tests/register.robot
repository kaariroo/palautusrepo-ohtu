*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username in already in use

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username contains wrong characters

Register With Valid Username And Too Short Password
    Input Credentials  ville  ville12
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  villekalle
    Output Should Contain  Password should contain numbers or special characters