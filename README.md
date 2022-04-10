# CopyDiscordStatusOfUser-SelfBot
Automatically copy the Discord Status of a Friend you share a server with (conditions have to be satisfied to work)

Install python 3 if you haven't and also install the discord python library by using 'pip install discord.py' in terminal

To run the program you need to download both the 'info.txt' and 'statuscopier.py' file in the same directory/folder

You also need your discord [authorization token](https://www.youtube.com/watch?v=YEgFvgg7ZPI), the [User ID](https://techswift.org/2020/04/22/how-to-find-your-user-id-on-discord/) of the person whose status you want to copy, as well as the Mutual Server ID (using the same steps you used to find the USER ID)

After you paste those values into the info.txt file, you are ready to run the program.

TThe program runs using python requests library to change the user's message status and discord library api to access other person's status. It checks the user's status every minute, because by running this program **you are at risk of being banned by violating discord's anti-self bot policy** (use at own risk), **although it's likely discord has more important things to worry about,** as long as the program is not sending too many requests (which this one probably isn't).

