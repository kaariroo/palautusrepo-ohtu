*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    # seuraava rivi on kommentoitu toistaiseksi pois
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}    

Login Page Should Be Open
    Title Should Be  Login

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Starting Page Should Be Open
    Title Should Be  Ohtu Application

Register Page Should Be Open
    Title Should Be  Register

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Go To Register Page
    Go To  ${REGISTER_URL}
