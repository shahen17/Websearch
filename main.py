import os
import wikipedia
import requests
from keep_alive import keep_alive
from config import *


import interactions


bot = interactions.Client(Token)


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(
    name="hello-world",
    description="A simple example command",
    scope=919153167814520902,
)
async def hello_world(ctx: interactions.CommandContext):
    await ctx.send("Hello World!")


@bot.command(
    name="type",
    description="search the web!",
    scope=919153167814520902,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="search",
            description="web-search by -shahen-",
            required=True,
        ),
        
    ],
)
async def type(ctx: interactions.CommandContext, search: str):
    wiki_search = wikipedia.summary(search, sentences=2)
    await ctx.send(wiki_search)

keep_alive()
bot.start()
