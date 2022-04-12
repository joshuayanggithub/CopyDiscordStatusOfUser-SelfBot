import discord, json ,time, requests
from discord.ext import commands,tasks

f = open( "UserToken&IDs.txt" ,"r")
statuschange_url = "https://discord.com/api/v9/users/@me/settings"
token = str(f.readline().strip())
user_id = int (f.readline().strip()) #test/sample id = 962488616058245140
sharedguild_id = int (f.readline().strip()) #test/sample id = 962491841293467650
f.close()

f2 = open("oldstatus.txt","r")
oldstatus = f2.readline().strip()

intents = discord.Intents.all()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix='>', self_bot=True, intents=intents) #random command prefix

def formattedPrint(str):
	print("------------------------------------------------------------------------------------")
	print(str)
	print("------------------------------------------------------------------------------------")
def getFormattedTime():
    return time.strftime('%I:%M %p %Z on %b %d, %Y')
def changeStatus(message):
	payload = {
		"status": "online",
		"custom_status": {
			"text": message,
		}
	}
	headers = {
		"authorization": token,
		"content-type": "application/json"
	}
	r = requests.patch(statuschange_url, data=json.dumps(payload), headers=headers)
	if (r.status_code == 200): #success
		formattedPrint("Succesfully changed status to\n\" " + message + " \"\nAt " + getFormattedTime())
		f3 = open("oldstatus.txt","w")
		f3.write(message)
		f3.close()
	else: #400
		formattedPrint("Error in changing status..." + getFormattedTime())
def storeOldStatus(status):
	print("Stored Old Status")	
	
@bot.event
async def on_ready():
    formattedPrint("Running on the account: " + bot.user.name)
    formattedPrint("WARNING: Self-bots on discord can get you banned" + "\nStarted Bot...")
    checkStatus.start()
@tasks.loop(minutes=1)
async def checkStatus():
	guild = bot.get_guild(sharedguild_id)
	person = guild.get_member(user_id)
	if (str(person.raw_status) != "offline"):
		activities = person.activities
		if (len(activities) != 0):
			status = str(activities[0])
			global oldstatus
			if (status != oldstatus):
				oldstatus = status
				changeStatus(status)
			else:
				formattedPrint("Your status matches person's status already | " + getFormattedTime())
		else:
			formattedPrint("Person currently has no status | " + getFormattedTime())
	else:
		await bot.change_presence(status=discord.Status.offline)
		formattedPrint("Target User Not Online | " + getFormattedTime())

bot.run(token, bot=False)
