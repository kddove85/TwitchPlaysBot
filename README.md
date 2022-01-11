# TwitchPlaysBot

## Installation

Assuming you already have python installed. If not, head to https://www.python.org/

1. Run ```pip install -r requirements.txt```
2. You will need a token for your bot. To get one, go to https://twitchtokengenerator.com/
3. You need to see 3 environmental variables:<br>
3a. ```token``` which is your new token you created in step 2<br>
3b. ```prefix``` which is the character that will begin all your commands in chat. I chose an "!" so my commands look like ```!command```<br>
3c. ```initial_channel``` which is just your channel, so for instance mine is ```dove06```<br>

## Uses

Once the bot is set up and running, you will have to give it mod status if you want it to be used in your channel (I'm pretty sure).
I've set this up to play Chrono Trigger on Steam by default. When the bot is running, use the command ```!list_commands``` in a channel's chat.<br><br>
If you have an instance of Chrono Trigger (Steam version) running, the bot should be able to interact with the game through commands in chat.

## Warnings

You may receive the following error:<br><br>
```UserWarning: 32-bit application should be automated using 32-bit Python (you use 64-bit Python) warnings.warn```<br><br>
If you get this, it means that you are using a version of python 64 bit and the application you are trying to control (your video game) is 32 bit. If this happens, your choices as of now are to ignore it and accept the risk or you can migrate to Python 32 bit. In my experience, although I receive the warning, the bot is still able to interact with the video game despite the warning.
