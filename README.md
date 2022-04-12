# CopyDiscordStatusOfUser-SelfBot

# Basic Function
Automatically copy the Discord Status of a friend User whom you share a server with (These conditions have to be satisfied to work!)

# Installation
You must haved installed python 3 (with default standard libraries) as well as the discord.py python library by typing in terminal the following:
```
pip install discord.py
```
Then go ahead and download both the 'UserToken&IDs.txt', 'oldstatus.txt', and 'statuscopier.py' file from this repository in the same directory/folder

# Requirements for the Program to Work (READ)

You have to be friended to the person whose status you want to copy, as well as share a server with them. Although further investigation might find a more lenient way to achieve the same purpose of the program, these rules hold because with the discord api the only way I have found to access the status of someone is through the 'activity' of a 'Member' object, which can only be accessed through sharing a server. In addition, I believe discord won't allow selfbots to access Member objects without being friended to them and I believe that is do to me not being able to add [Discord Intents](https://discordpy.readthedocs.io/en/stable/intents.html) as a selfbot.

# Setup (IMPORTANT: MUST READ)

You must retrieve your personal discord [authorization token](https://www.youtube.com/watch?v=YEgFvgg7ZPI), the [User ID](https://techswift.org/2020/04/22/how-to-find-your-user-id-on-discord/) of the person whose status you want to copy, as well as the Mutual Server ID (using the same steps you used to find the User ID).

Once you retrive these information, **you must paste** those values into the UserToken&IDs.txt file in the correct order specified in the template that exists in that file already, and only then are you ready to run the program.

Using any IDE or Terminal simply run the python program you downloaded before:

```
python3 statuscopier.py
```

# How it Runs
The program runs using python requests library and sends a HTTP patch request updating the user's custom discord status and uses the discord library api to access other person's status. It checks that user's status every minute; In addition, since you are running an automated self-bot on your user account, **you are at risk of being banned by violating discord's anti-self bot policy** (use at own risk), **although it's likely discord has more important things to worry about,** as long as the program is not sending too many requests (which this one probably isn't).

The 'UserToken&IDs.txt' file holds the discord token, user id, and server id while the 'oldstatus.txt' holds the current user status in order to retain the current status variable string information even after the program is terminated in whatever IDE is running it.

Side-note: The Discord API is really weird, it was made for the purpose of actual discord bots not discord users, because self-botting was banned years ago, so certain operations using the API discord.py wrapper **are just weird and were often prone to error** when originally coding this

# Program Console Code in Terminal

<img width="608" alt="Screen Shot 2022-04-11 at 8 09 13 PM" src="https://user-images.githubusercontent.com/85262856/162871715-8237fa2a-bd3c-4b02-bf5d-437ab1ba7ce2.png">


# Discord Output

<img width="300" alt="Screen Shot 2022-04-11 at 8 10 30 PM" src="https://user-images.githubusercontent.com/85262856/162871951-dd5188ab-657e-42a8-a798-692621285738.png"> <img width="300" alt="Screen Shot 2022-04-11 at 8 10 02 PM" src="https://user-images.githubusercontent.com/85262856/162871933-f6d0c4e8-0558-44da-be57-1e6a35434218.png">  
