# ⚙ Cowin-Vaccine-Searching-Automation ⚙
🌟 __Selenium Automation__
🌟 __Python__

As you must know registering for COVID vaccine on COWIN website is real headache for Age group 18 - 44. Available slots stay open for barely a minute you have to be fast to register for vaccine.

# Disclaimer 🚦

1. I am not responsible if somehow your account is blocked.
2. I made this Bot to brush up my Selenium skills
3. Please check Date ,  Vaccine , Pincode before confirming your vaccination 
4. Again I am not responsible for anything you face because of this script


# Inputs for Bot 🤖

* Registered Mobile Number 
* List of your choice of pin codes
* Path to your Webdriver
* [Optional] Change bot sleep time while entering OTP


# ⚠ Before you run the Bot ⚠

1. Selenium requires WEBDRIVER in order to execute the script
2. You can Download WEBDRIVER for Chrome from [Chrome Webdriver](https://chromedriver.chromium.org/downloads)
3. Make sure you download proper version of Webdriver with respect to your Browser version
4. Make sure you have already registered on Cowin using a mobile number
5. You'll get 30 seconds to Enter OTP on site you can change seconds
6. Also you have to manually select multiple members (if you have added more members) you'll get 15 seconds
7. You just have to Enter OTP don't press any button Selenium auto clicks the button after 30 seconds
8. You'll only interact with site to enter OTP, Select Members and to confirm slots after the bot has found available slot


# 📋 Procedure of Bot 📋

1. Visits Cowin Login Page [Cowin Page](https://selfregistration.cowin.gov.in/)
2. Waits for 30 seconds for you to Enter OTP
3. Waits for 15 seconds for you to Select Members
4. Selects a random pin code for your provided list and searches for availability
5. Filters results by Age 18-45
6. Check if there are Vaccine available on any day
7. If no available slots Bot jumps to Step 4
8. If found the Bot opens the Page where you manually have to select time slot and confirm your registeration for vaccine 


# 💪 How you can help to improve the Bot 💪

* Add more inputs to accept Age of user and filter results accordingly
* I have added comments please go through once
* Open for suggestions


# ✌ Peace
