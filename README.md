# League of Voicechat
Hello! This is a project I made back in 2022 and stored on google drive for whatever reason instead of github. I moved it here into an abandoned repo where I had planned to update it. That was years ago so I decided to dig up the old files and have it here to archive or maybe to update in the future.

## What is this?
This was a fun side side project for me and my friends. I didn't learn databases in highschool yet, so I was like "hey, google sheet can save and share data across the internet right," and I made my own system using google sheets haha. 

## How it works
Anyway it uses OpenCV on a local python program to scan and track your League of Legends minimap and turn it into coordinates.

Then it would send those via google api credentials to a google sheet. All 10 people in the game would be running their own coordinate publisher locally. 

They would also be in the same special discord server. This server has a special bot with admin permissions to move people around calls. It would read the data from the google sheet, and move the corresponding user assigned to that role around 5 different voicechats, pertaining to each area of the Summoner's Rift. Also before the match started you would need to tell the bot which discord tag was in which role on which side.

## Duct Tape and Dreams
Yeah imma be honest this thing is jank, and held together by literal packaging tape. But it was just for me an my friends to have like a semi-proximity chat for custom games. I actually messaged a support ticket when I previously planned to update this project when Riot Vanguard was ported to League from Valorant, and they said something vague and I didn't want to get banned for making the proximity chat so maybe that's why I never got around to doing it. Anyway this is obviously missing a credentials file, and also a google api token for the discord bot code in `Bot Code.py`. I'll put in a sample of all the stuff just if anyone evers stumbles across and is like "nah i wanna get this thing working again" haha. Cheers - Leo