from telethon import TelegramClient

api_id = '27066935'
api_hash = '4f21d03b65fe9a736ca7c79422d9ac2d'
group_id = -1002215923063

# Replace with your Telegram API credentials
client = TelegramClient('session_file', api_id, api_hash)

async def get_group_access_hash(group_id):
    async with client:
        # Get the group entity with access_hash
        group = await client.get_entity(group_id)
        access_hash = group.access_hash
        return access_hash

async def main():
    access_hash = await get_group_access_hash(group_id)
    print(access_hash)

# Run the main function
client.loop.run_until_complete(main())
