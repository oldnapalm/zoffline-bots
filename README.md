# zoffline-bots

Bots are replays of activities saved using zwift-offline.

Download: [bots.zip](https://github.com/oldnapalm/zoffline-bots/releases/download/bots/bots.zip)

To install, download the bots.zip file, unzip it, and place the "storage" folder into the same directory
that contains the zoffline executable.

The file [enable_bots.txt](https://github.com/oldnapalm/zoffline-bots/blob/main/storage/enable_bots.txt)
in the storage folder enables the feature and the number it contains is a multiplier value.

Type ``.group`` in chat to group the bots, or ``.groupall`` to include duplicates (if using multiplier).
Type ``.autogroup`` or ``.autogroupall`` to automatically group whenever you change roads.
Type ``.stopautogroup`` to stop automatic grouping, or ``.disperse`` to randomize positions.

Names, nationalities and equipment can be customized by creating a file bot.txt inside the storage folder
([bot_teams.txt](https://github.com/oldnapalm/zoffline-bots/blob/main/storage/bot_teams.txt) is a sample file,
rename it to bot.txt to use it). The script [get_pro_names.py](https://github.com/zoffline/zwift-offline/blob/master/scripts/get_pro_names.py)
can be used to populate this file.

The script [check_bots.py](https://github.com/oldnapalm/zoffline-bots/blob/main/check_bots.py) removes bots with
gaps and short bots (to avoid having bots disappearing frequently).
