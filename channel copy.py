import discord

client = discord.Client()
token = 'token'                     # Insert own token here

from_id = 123456789        # Enter channel ID which you want to copy the messages from
to_id = 987654321          # Enter channel ID which you want to paste the messages to

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    from_channel = client.get_channel(id=from_id)
    to_channel = client.get_channel(id=to_id)
    
    messages = await from_channel.history(limit=None).flatten()
    messages.reverse()

    count = 1
    for message in messages:
        print(count)
        count += 1
        if message.attachments:
            await to_channel.send(message.attachments[0].url)
        else:
            await to_channel.send(message.content)

    print('Done!')

client.run(token, bot=False)
