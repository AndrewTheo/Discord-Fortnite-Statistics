# Work with Python 3.6
import discord

import requests
import json

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


TOKEN = 'INSERT DISCORD API TOKEN HERE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!fnlink '):
        messageAuthorId = message.author.id
        start = message.content
        fname = start.split("!fnlink ")[1]
        with open('fort.json', encoding='utf-8') as f:
            data = json.load(f)
        data[messageAuthorId] = fname

        with open('fort.json', 'w') as outfile:
            json.dump(data, outfile)




    if message.content == ('!fn'):
        messageAuthorId = message.author.id
        with open('fort.json', encoding='utf-8') as f:
            data = json.load(f)
        try:
            fnName = data[messageAuthorId]
        except NameError:
            msg = '{0.author.mention} No Linked Username Found. Try !fnlink <username>'.format(message)
            await client.send_message(message.channel, msg)
        except KeyError:
            msg = '{0.author.mention} No Linked Username Found. Try !fnlink <username>'.format(message)
            await client.send_message(message.channel, msg)
        else:
            fnName = data[messageAuthorId]
            start = message.content
            name = fnName
            print(name)

            url = "https://api.fortnitetracker.com/v1/profile/pc/"
            api_url = url + name
            print(api_url)

            header = {"TRN-Api-Key": '02900164-e2e6-4216-80e2-1fedc9c5276d'}

            r = requests.get(api_url, headers=header)
            data = json.loads(r.text)
            

            try:
                name = data["epicUserHandle"]
            except KeyError:
                msg = '{0.author.mention} No player found.'.format(message)
                await client.send_message(message.channel, msg)
            else:    
                lifeStats = data["lifeTimeStats"]
                matches = lifeStats[7]["value"]


                totalWins = lifeStats[8]["value"]
                totalKD = lifeStats[11]["value"]
                totalWinP = lifeStats[9]["value"]
                totalKills = lifeStats[10]["value"]

                soloWins = data["stats"]["p2"]["top1"]["value"]
                soloKD = data["stats"]["p2"]["kd"]["value"]
                soloKills = data["stats"]["p2"]["kills"]["value"]
                soloWinP = data["stats"]["p2"]["winRatio"]["value"]+"%"

                duoWins = data["stats"]["p10"]["top1"]["value"]
                duoKD = data["stats"]["p10"]["kd"]["value"]
                duoKills = data["stats"]["p10"]["kills"]["value"]
                duoWinP = data["stats"]["p10"]["winRatio"]["value"]+"%"

                squadWins = data["stats"]["p9"]["top1"]["value"]
                squadKD = data["stats"]["p9"]["kd"]["value"]
                squadKills = data["stats"]["p9"]["kills"]["value"]
                squadWinP = data["stats"]["p9"]["winRatio"]["value"] +"%"

                kdnow = float(totalKills)/(float(matches) - float(totalWins))
                lifekd = str(kdnow)
                try:
                    num = str(lifekd[4])
                except:
                    num = "0"

                numbers = ["5","6","7","8","9","0","1","2","3","4"]
                barLength = (numbers.index(num)+1)*67.5



                fnt = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 40)
                fntTwo = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 65)
                fntThree = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 50)
                fntFour = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 34)
                fntFive = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 28)
                img = Image.open("test52.jpg")

                draw = ImageDraw.Draw(img)
                draw.rectangle([(65, 142), (barLength, 167)], (81,204,123))
                draw.text((30, 55), name, (255,255,255), font=fnt)
                draw.text((615, 50), matches, (255,255,255), font=fntFive)
                draw.text((900, 60), totalWins, (255,255,255), font=fntTwo)
                draw.text((865, 290), totalKD, (255,255,255), font=fntThree)
                draw.text((865, 410), totalWinP, (255,255,255), font=fntThree)
                draw.text((865, 535), totalKills, (255,255,255), font=fntThree)

                draw.text((240, 248), soloWins, (255,255,255), font=fntFour)
                draw.text((591, 248), soloKills, (255,255,255), font=fntFour)
                draw.text((347, 248), soloKD, (255,255,255), font=fntFour)
                draw.text((465, 248), soloWinP, (255,255,255), font=fntFour)

                draw.text((376, 360), duoKills, (255,255,255), font=fntFour)
                draw.text((133, 360), duoKD, (255,255,255), font=fntFour)
                draw.text((253, 360), duoWinP, (255,255,255), font=fntFour)
                draw.text((27, 360), duoWins, (255,255,255), font=fntFour)

                draw.text((246, 472), squadWins, (255,255,255), font=fntFour)
                draw.text((598, 472), squadKills, (255,255,255), font=fntFour)
                draw.text((354, 472), squadKD, (255,255,255), font=fntFour)
                draw.text((472, 472), squadWinP, (255,255,255), font=fntFour)




                img.save("sample.jpg")

                await client.send_file(message.channel, "sample.jpg")





    if message.content.startswith('!fn'):
        msg = 'Hello {0.author.mention}'.format(message)
        print(message.author.id)

        start = message.content
        name = start.split("!fn ")[1]
        print(name)

        url = "https://api.fortnitetracker.com/v1/profile/pc/"
        api_url = url + name
        print(api_url)

        header = {"TRN-Api-Key": '02900164-e2e6-4216-80e2-1fedc9c5276d'}

        r = requests.get(api_url, headers=header)
        data = json.loads(r.text)
        

        try:
            name = data["epicUserHandle"]
        except KeyError:
            msg = '{0.author.mention} No player found.'.format(message)
            await client.send_message(message.channel, msg)
        else:    
            lifeStats = data["lifeTimeStats"]
            matches = lifeStats[7]["value"]


            totalWins = lifeStats[8]["value"]
            totalKD = lifeStats[11]["value"]
            totalWinP = lifeStats[9]["value"]
            totalKills = lifeStats[10]["value"]

            soloWins = data["stats"]["p2"]["top1"]["value"]
            soloKD = data["stats"]["p2"]["kd"]["value"]
            soloKills = data["stats"]["p2"]["kills"]["value"]
            soloWinP = data["stats"]["p2"]["winRatio"]["value"]+"%"

            duoWins = data["stats"]["p10"]["top1"]["value"]
            duoKD = data["stats"]["p10"]["kd"]["value"]
            duoKills = data["stats"]["p10"]["kills"]["value"]
            duoWinP = data["stats"]["p10"]["winRatio"]["value"]+"%"

            squadWins = data["stats"]["p9"]["top1"]["value"]
            squadKD = data["stats"]["p9"]["kd"]["value"]
            squadKills = data["stats"]["p9"]["kills"]["value"]
            squadWinP = data["stats"]["p9"]["winRatio"]["value"] +"%"

            kdnow = float(totalKills)/(float(matches) - float(totalWins))
            lifekd = str(kdnow)
            try:
                num = str(lifekd[4])
            except:
                num = "0"

            numbers = ["5","6","7","8","9","0","1","2","3","4"]
            barLength = (numbers.index(num)+1)*67.5



            fnt = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 40)
            fntTwo = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 65)
            fntThree = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 50)
            fntFour = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 34)
            fntFive = ImageFont.truetype('C:\Windows\Fonts\LuckiestGuy-Regular', 28)
            img = Image.open("test52.jpg")

            draw = ImageDraw.Draw(img)
            draw.rectangle([(65, 142), (barLength, 167)], (81,204,123))
            draw.text((30, 55), name, (255,255,255), font=fnt)
            draw.text((615, 50), matches, (255,255,255), font=fntFive)
            draw.text((900, 60), totalWins, (255,255,255), font=fntTwo)
            draw.text((865, 290), totalKD, (255,255,255), font=fntThree)
            draw.text((865, 410), totalWinP, (255,255,255), font=fntThree)
            draw.text((865, 535), totalKills, (255,255,255), font=fntThree)

            draw.text((240, 248), soloWins, (255,255,255), font=fntFour)
            draw.text((591, 248), soloKills, (255,255,255), font=fntFour)
            draw.text((347, 248), soloKD, (255,255,255), font=fntFour)
            draw.text((465, 248), soloWinP, (255,255,255), font=fntFour)

            draw.text((376, 360), duoKills, (255,255,255), font=fntFour)
            draw.text((133, 360), duoKD, (255,255,255), font=fntFour)
            draw.text((253, 360), duoWinP, (255,255,255), font=fntFour)
            draw.text((27, 360), duoWins, (255,255,255), font=fntFour)

            draw.text((246, 472), squadWins, (255,255,255), font=fntFour)
            draw.text((598, 472), squadKills, (255,255,255), font=fntFour)
            draw.text((354, 472), squadKD, (255,255,255), font=fntFour)
            draw.text((472, 472), squadWinP, (255,255,255), font=fntFour)




            img.save("sample.jpg")

            await client.send_file(message.channel, "sample.jpg")
            #await client.send_file(message.channel, "test5.jpg")

    if message.content.startswith('!top'):
        await client.send_file(message.channel, "leader.jpg")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
