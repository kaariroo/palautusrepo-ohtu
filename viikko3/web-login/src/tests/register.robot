*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  julle
    Set Password  jullekaa
    Set Password Confirmation  jullekaa
    Submit Credentials
    Register Should Fail With Message  Password should contain numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle124
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation are not the same
    
Login After Successful Registration
    Click Link  Login
    Set Username  ville
    Set Password  ville123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Click Link  Login
    Set Username  vi
    Set Password  ville123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Go To Login Page
    Login Page Should Be Open

Register Should Succeed
    Welcome Page Should be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}