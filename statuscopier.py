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
offline = False

intents = discord.Intents.all()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix='>', self_bot=True, intents=intents) #random command prefix

def formattedPrint(str):
	print("------------------------------------------------------------------------------------")
	print(str)
	print("------------------------------------------------------------------------------------")
def getFormattedTime():
    return time.strftime('%I:%M:%S %p %Z on %b %d, %Y')
def changeStatusOffline():
	payload = {
		"status": "invisible",
	}
	headers = {
		"authorization": token,
		"content-type": "application/json"
	}
	r = requests.patch(statuschange_url, data=json.dumps(payload), headers=headers)
	if (r.status_code == 200): #success
		formattedPrint("Succesfully went invisible " + "\nAt " + getFormattedTime())
		updateOldStatus("NO STATUS: (invisible)")
	else: #400
		formattedPrint("Error in going invisible..." + getFormattedTime())
def updateOldStatus(status):
	global oldstatus
	oldstatus = status
	f3 = open("oldstatus.txt","w")
	f3.write(status)
	f3.close()
def changeStatus(message,str_status):
	payload = {
		"status": str_status,
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
		formattedPrint("Succesfully changed status to\n\"" + message + "\"\nwhilst on " + str_status + " mode \nAt " + getFormattedTime())
		updateOldStatus(message)
	else: #400
		formattedPrint("Error in changing status... at " + getFormattedTime())
def changeAboutMe(message):
	payload = {
		"bio": message
	}
	headers = {
		"authorization": token,
		"content-type": "application/json"
	}
	r = requests.patch(statuschange_url, data=json.dumps(payload), headers=headers)
	if (r.status_code == 200): #success
		formattedPrint("Succesfully changed about me to\n\" " + message + " \"\nAt " + getFormattedTime())
	else: #400
		formattedPrint("Error in changing about me..." + getFormattedTime())
	
@bot.event
async def on_ready():
    formattedPrint("Running on the account: " + bot.user.name)
    formattedPrint("WARNING: Self-bots on discord can get you banned" + "\nStarted Bot...")
    checkStatus.start()
@tasks.loop(minutes=1)
async def checkStatus():
	global oldstatus, offline
	guild = bot.get_guild(sharedguild_id)
	person = guild.get_member(user_id)
	if (str(person.raw_status) != "offline"):
		offline = False
		activities = person.activities
		str_status = person.raw_status
		if (len(activities) != 0):
			status = str(activities[0])
			if (status != oldstatus):
				changeStatus(status,str_status)
			else:
				formattedPrint("Your status matches person's status already | " + getFormattedTime())
		else:
			status = "Baller"
			if (status != oldstatus):
				oldstatus = status
				changeStatus(status,str_status)
			formattedPrint("Person currently has no status | " + getFormattedTime())
	else:
		#await bot.change_presence(status=discord.Status.offline)
		if (not offline):
			offline = True
			changeStatusOffline()
		formattedPrint("Target User Not Online | " + getFormattedTime())

bot.run(token, bot=False)
