*** Settings ***
Library         SeleniumLibrary
Library         KW.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
URL Test - Selenium Library
    Open Browser        https://www.tesla.com/    Chrome
    Maximize Browser Window
    Sleep        10
    Element Should Be Visible       xpath=/html/body/div[5]/main/div/div[2]/div/section/div/div/div[1]
    Click Element       xpath=/html/body/div[5]/main/div/div[2]/div/section/div/div/div[1]/section/a[1]
    Get Location
    Capture Page Screenshot
    Close Browser

URL Test - customKW Library
    Open Site
    Click Services