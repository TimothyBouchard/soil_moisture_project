# soil_moisture_project

4/16/2023 
I'v been working on this project for about a month now, my goal is to create a mobile application that can help users effectivly grow a garden.
I have uploaded everything i have devloped thus far, all the data was created by me from surching the internet. The code was also devloped by me as well. 

So far the only thing i have somwhat completed is the main AI chatbot, this is a bot that i want to implament into the application that would make the user feel like the application is personalized to them, or their garden. 

goal 1: are going to be to make the chatbot more personalble and relateable.

goal 2: i would like to implment a weather api get request to add weather data into the application. Im hoping i can find this data online somwhere, if not i have to create my own data set which i already have started the process in doing so, i have a Arduino micro controller that can monitor soil moisture, temp, and humidity levels, im having issues saving the data though, i have an sd card reader that i could save the data too but its not working. i tried saving the data to a google doc. but im having issues with that as well. If i cant find soil moisture, and weather pattern data online i may have to continue where i left off in making the device. 

------------------------------------------------------------------------------------------------------------------------------------------------------------

5/9/2023
Iv created a Arduino device to monitor moisture levels, compared to weather data pulled from openweathermap api request, this records the data on a SD card. The dataset is going to be used to create patterns of how weahter affects the soil moisture levels. 

Device: 
Arduino ESP32 Wemos D1 R32 dev bored
Soil moisture sensor
SD card reader
32GB patriot micro SDHC card 

Im going to run a 24 hour test in outdoor conditions, with api records every hour. 
Wiring diagram will be available soon. 

future improvements to the device would be to add a i2c display to display some data, and a outlet powersupply other than my PC so i dont run up electric bill. Reasons for the 24 hour test.

12/26/2024
Edited files and took a look back into old project. To clarify this project turned into a garden chatbot

no major updates to the roject and will hope to resume in the future
