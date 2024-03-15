# zoffline-bots

This is a collection of bots to be used with [zwift-offline](https://github.com/zoffline/zwift-offline).
Bots are the same as ghosts. Think of them as replays of activities saved using zwift-offline.
The difference between bots and ghosts is that ghosts are loaded when you start riding the same route
as the original ride, while bots are loaded when zwift-offline is launched and stay riding all the time in a loop.

The file [enable_bots.txt](https://github.com/oldnapalm/zoffline-bots/blob/main/storage/enable_bots.txt)
in the storage folder enables the feature and the number it contains is a multiplier value (use with caution,
if the resulting number of bots is too high, it may cause performance issues or not work at all).

Names, nationalities and equipment can be customized by creating a file bot.txt inside the storage folder
([bot_teams.txt](https://github.com/oldnapalm/zoffline-bots/blob/main/storage/bot_teams.txt) is a sample file,
rename it to bot.txt to use it). The scripts [get_pro_names.py](https://github.com/zoffline/zwift-offline/blob/master/scripts/get_pro_names.py)
and [get_strava_names.py](https://github.com/zoffline/zwift-offline/blob/master/scripts/get_strava_names.py)
can be used to populate this file.

The script [check_bots.py](https://github.com/oldnapalm/zoffline-bots/blob/main/check_bots.py) removes bots with
gaps and short bots (to avoid having bots disappearing frequently).
