import interactions
from constants import DISCORD_TOKEN

from tweets import fetch_tweets, get_random_tweet

client = interactions.Client(DISCORD_TOKEN)

@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.me}!")
    fetch_tweets()


@client.command(name="dog", description='犬botが喋ります"')
async def dog(ctx: interactions.CommandContext) -> (interactions.Message or None):
    if not ctx.guild:
        return await ctx.send(
            content="このコマンドは DM で使用できません。"
        )
    sentence = get_random_tweet()
    await ctx.send(
        content=sentence
    )

client.start()