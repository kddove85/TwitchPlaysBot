# TwitchPlaysBot

## Installation

1. Run ```pip install -r requirements.txt```
2. You will need a token for your bot. To get one, go to https://twitchtokengenerator.com/
3. You need to see 3 environmental variables:<br>
3a. ```token``` which is your new token you created in step 2<br>
3b. ```prefix``` which is the character that will begin all your commands in chat. I chose an "!" so my commands look like ```!command```<br>
3c. ```initial_channel``` which is just your channel, so for instance mine is ```dove06```<br>

## Warnings

You may receive the following error:
UserWarning: 32-bit application should be automated using 32-bit Python (you use 64-bit Python) warnings.warn

If you get this, it means that you are using a version of python 64 bit and the application you are trying to control (your video game) is 32 bit. If this happens, your choices as of now are to ignore it and accept the risk or you man migrate to Python 32 bit. In my experience, although I receive the warning, the bot is still able to interact with the video game despite the warning.
