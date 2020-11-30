import requests
import discord
from discord import File
import asyncio, json
import traceback
from datetime import datetime, timedelta
import discord.ext.commands as commands
import discord
import random

class Proxy(commands.Cog, command_attrs=dict(hidden=True)):
    @staticmethod
    def scrapeHTTPS(amt=500):
        data = requests.get("PUT-API-URL-HERE").text.splitlines()
        random.shuffle(data)
        if len(data) < amt:
            written = data
        else:
            written = data[:amt]
        with open("./https.txt", "w+") as file:
            file.write('\n'.join(written))

    @staticmethod
    def scrapeSOCKS4(amt=500):
        data = requests.get("PUT-API-URL-HERE").text.splitlines()
        random.shuffle(data)
        if len(data) < amt:
            written = data
        else:
            written = data[:amt]
        with open("./socks4.txt", "w+") as file:
            file.write('\n'.join(written))

    @staticmethod
    def scrapeSOCKS5(amt=500):
        data = requests.get("PUT-API-URL-HERE").text.splitlines()
        random.shuffle(data)
        if len(data) < amt:
            written = data
        else:
            written = data[:amt]
        with open("./socks5.txt", "w+") as file:
            file.write('\n'.join(written))
    
    @commands.command()
    @commands.guild_only()
    async def omni(self, ctx, arg1):
        if ctx.channel.id != 718741554281447484:
            return
        try:
            if (arg1.lower() == "https"):
                self.scrapeHTTPS()
                await ctx.author.send("Qty: 500", file = File("./https.txt", filename="https.txt"))
            elif (arg1.lower() == "socks4"):
                self.scrapeSOCKS4()
                await ctx.author.send("Qty: 250", file = File("./socks4.txt", filename="socks4.txt"))
            elif (arg1.lower() == "socks5"):
                self.scrapeSOCKS5()
                await ctx.author.send("Qty: 250", file = File("./socks5.txt", filename="socks5.txt"))
            else:
                raise Exception
            embed = discord.Embed(title = f"Yo, My Dawg {arg1.upper()} proxies have been sent to your DM's.", color=0xADD8E6)
            embed.set_footer(icon_url = "https://raw.githubusercontent.com/0x06060606/EonHub-Panel/master/hex.png" , text = "Exodus Private Proxy Bot")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed = embed)
        except Exception as e:
            embed = discord.Embed(title = "The correct Usage is  `]omni `https/socks4/socks5`", color=0xADD8E6)
            embed.set_footer(icon_url = "https://raw.githubusercontent.com/0x06060606/EonHub-Panel/master/hex.png" , text = "Exodus Private Proxy Bot")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed = embed)
            print(e)