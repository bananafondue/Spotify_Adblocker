# Spotify_Adblocker

Spotify ads are not pleasant, so here's a python script which mutes spotify when an ad pops up.
No more wind rushing by, no horns or engines. 


## Instructions:

Libraries needed:
requests : **pip install requests**

pycaw : **pip install pycaw**
-> Spotify premium is required to mute spotify through the API. To bypass this, the pycaw library is used to mute the spotify aplication through windows itself.


secrets.py
This file should contain three strings,
spotify_user_id, refresh token, base_64

spotify_user_id 
-Can be found at spotify.com/account under "Profile -> Username".

refresh token, base_64
-This one is a bit tricky. All the steps are listed in help.txt.

After obtaining the values for the strings, place them in secrets.py.

And Voila! there you have it. Start the script AFTER you run spotify.exe on your device and you wont have to listen to any more ads.
