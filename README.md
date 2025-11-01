# Squad-API-Public

# Note

I am opening this repository because Squad Busters has decided to end development. I did not want to continue paying the host for the API for those who still need it until mid-2026. Please feel free to host it.

For future users, please note that if you encounter this repository after the second half of 2026, there is a good chance that this tool will no longer function.


## Download & run
1. 
`git clone https://github.com/risporce/Squad-API-Public.git`

2.

Add the necessary files in /Files/Assets/ . Please read the assets.txt file

3. 

`python3 main.py`


---
## Routes

default port is 30000, change it to your need in main.py

### 1. Player Profile

Returns the user profile data

http://localhost:30000/user/<user_id> 

Where <user_id> is ID number you can find in Squad Busters settings page, e.g: 0-90088


---
### 2. Global Leaderboard

Returns the 1000 current players in the global leaderboard, 30 minutes cache

http://localhost:30000/leaderboard

---

### 3. Status

Get the current game status, returns an integer:

0 = API should be working

7 = Game had a content patch, the API tries to auto update but sometime fails

8 = Game had an update, will require manual update to support new version

10 = Game currently in maintenance

http://localhost:30000/status


### Enjoy
This content is not affiliated with, endorsed, sponsored, or specifically approved by Supercell and Supercell is not responsible for it. For more information see: [Supercell's Fan Content Policy](https://supercell.com/en/fan-content-policy/) and also [Supercell's Term of Service](https://supercell.com/en/terms-of-service/)




