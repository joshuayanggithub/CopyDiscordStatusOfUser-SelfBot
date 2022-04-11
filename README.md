# CopyDiscordStatusOfUser-SelfBot

# Basic Function
Automatically copy the Discord Status of a Friend User whom you share a server with (These conditions have to be satisfied to work!)


# Preresequites
Installed python 3 (with default standard libraries) as well as the discord python library by typing in terminal the following:
```
pip install discord.py
```

# Installation
You need to download both the 'info.txt' and 'statuscopier.py' file from this repository in the same directory/folder

You also need your discord [authorization token](https://www.youtube.com/watch?v=YEgFvgg7ZPI), the [User ID](https://techswift.org/2020/04/22/how-to-find-your-user-id-on-discord/) of the person whose status you want to copy, as well as the Mutual Server ID (using the same steps you used to find the USER ID)

After you paste those values into the info.txt file in the correct order specified in the template in the file already, you are ready to run the program.

# How it Runs
The program runs using python requests library and sends a http patch request updating the user's custom discord status and uses the discord library api to access other person's status. It checks that user's status every minute; In addition, since you are running an automated self-bot on your user account, **you are at risk of being banned by violating discord's anti-self bot policy** (use at own risk), **although it's likely discord has more important things to worry about,** as long as the program is not sending too many requests (which this one probably isn't).

Side-note: The Discord API is really weird, it was made for the purpose of actual discord bots not discord users, and since we are self-botting, not only can we get banned, so certain operations using the API discord.py wrapper **are just weird and were often prone to error** when originally coding this

# Program Console Code in Terminal

<img width="639" alt="Screen Shot 2022-04-10 at 7 11 30 PM" src="https://user-images.githubusercontent.com/85262856/162653600-f538bd7f-2838-4e4b-bfa7-d9ccab90fcef.png">

# Discord Output
<img width="277" alt="Screen Shot 2022-04-09 at 6 51 31 PM" src="https://user-images.githubusercontent.com/85262856/162597816-b022b839-c658-4c25-a4f7-f6c3b34b7c23.png"> <img width="293" alt="Screen Shot 2022-04-09 at 6 52 11 PM" src="https://user-images.githubusercontent.com/85262856/162597818-4c70e4dc-3471-406b-91a9-345265e337c2.png">
