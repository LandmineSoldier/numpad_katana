
import discord, asyncio
import os
import random
import time
from random import *

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("패링"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    #made by LandmineSoldier (지뢰군인)
    #내 피땀눈물 섞어만든 게임

    if message.content == '넘패드카타나':
        channel = message.channel
        await channel.send('(5초내에 그렇다 라고 답하시오)')

        def check(m):
            return m.content == '그렇다' and m.channel == channel
        await client.wait_for('message', check=check, timeout=5.0)

        embed=discord.Embed(title="넘패드카타나", description="하는 방법", color=0x371fff)
        embed.set_author(name="3초내에 봇의 공격을 맞받아치세요", url="https://steamcommunity.com/id/LandmineSoldier/", icon_url="https://cdn.discordapp.com/app-icons/681470208648544279/3194ed1f665a08c5431ff9f009b5dd61.png?size=64")
        embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/688576218152304662/324834261bb9c63f2982e0e1e41a82b6.png?size=256")
        embed.add_field(name="가로공격", value="좌우 반전", inline=True)
        embed.add_field(name="세로공격", value="상하 반전", inline=True)
        embed.add_field(name="대각선 공격", value="상하좌우 반전", inline=True)
        embed.add_field(name="가로공격 예시", value="123-> 321", inline=True)
        embed.add_field(name="세로공격 예시", value="741 -> 147", inline=True)
        embed.add_field(name="대각선 공격 예시", value="159 -> 753", inline=True)
        embed.add_field(name="kimryul", value="최고기록 371번", inline=True)
        embed.set_footer(text="60초 내에 ready라고 말하세요")
        await message.channel.send(embed=embed)

        def ready(m):
            return m.content == 'ready' and m.channel == channel
        await client.wait_for('message', check=ready, timeout=60.0)
        await channel.send('3초 후 봇의 공격이 실행됩니다!')
        time.sleep(3)
        await message.channel.send('test')
        s = 0
        while True:
            r = randint(1,16)
            if r == 1:
                await message.channel.send("123")
                def r1(m):
                    return m.content == '321' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r1, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 2:
                await message.channel.send("456")
                def r2(m):
                    return m.content == '654' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r2, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 3:
                await message.channel.send("789")
                def r3(m):
                    return m.content == '987' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r3, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 4:
                await message.channel.send("321")
                def r4(m):
                    return m.content == '123' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r4, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 5:
                await message.channel.send("654")
                def r5(m):
                    return m.content == '456' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r5, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 6:
                await message.channel.send("987")
                def r6(m):
                    return m.content == '789' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r6, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1


            if r == 7:
                await message.channel.send("147")
                def r7(m):
                    return m.content == '741' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r7, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 8:
                await message.channel.send("258")
                def r8(m):
                    return m.content == '852' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r8, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 9:
                await message.channel.send("369")
                def r9(m):
                    return m.content == '963' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r9, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 10:
                await message.channel.send("741")
                def r10(m):
                    return m.content == '147' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r10, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 11:
                await message.channel.send("852")
                def r11(m):
                    return m.content == '258' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r11, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 12:
                await message.channel.send("963")
                def r12(m):
                    return m.content == '369' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r12, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1


            if r == 13:
                await message.channel.send("159")
                def r13(m):
                    return m.content == '753' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r13, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 14:
                await message.channel.send("951")
                def r14(m):
                    return m.content == '357' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r14, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 15:
                await message.channel.send("357")
                def r15(m):
                    return m.content == '951' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r15, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
            if r == 16:
                await message.channel.send("753")
                def r16(m):
                    return m.content == '159' and m.channel == channel
                try : 
                    await client.wait_for('message', check=r16, timeout=5.0)
                except asyncio.TimeoutError:
                    break
                else:
                    s += 1
        await message.channel.send("좋은싸움이었다..")
        await message.channel.send("당신은 봇의 공격을 총")
        await message.channel.send(s)
        await message.channel.send("번 튕겨냈습니다!")
        
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
