from telegram import Update 
from telegram.ext import ContextTypes

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

from telethon.tl.types import InputPeerUser,PeerUser

from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
admin_phone_number = os.getenv('ADMIN_PHONE_NUMBER')
channel_id =int(os.getenv('CHANNEL_ID'))
channel_access_hash =os.getenv('CHANNEL_ACCESS_HASH')

# Adding user to the Telegram group
async def add_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE,tickets_no): 

    

    user_id = update.message.from_user.id
    
    try:
        client = TelegramClient('adding to group',api_id, api_hash)
        await client.start(phone=admin_phone_number)
        channel = await client.get_entity(channel_id)
        channel = await client.get_entity(channel)
        # Get the user entity
        user = await client.get_entity(PeerUser(user_id))
        #full_user = await client(GetFullUserRequest(user_id))
        #user = full_user.user
        print("add to group run")
        await client(InviteToChannelRequest(
            channel=channel,
            users=[user]
        )) 
    except Exception as e:
        print(f'Error: {e}')


    # invite_link='https://t.me/+tP8NGEyLkHljNTJl' # Link of the group that users going toa add
    #Creating invite link using the channel id
    invite_link = await context.bot.create_chat_invite_link(channel_id)
    
    try:    
        user_id = update.message.from_user.id
        # Assuming the bot has admin rights to manage group members
        await context.bot.approve_chat_join_request(channel_id, user_id)
        await update.message.reply_text(f"You get {tickets_no} free tickets. You have been added to the group.")
    except Exception as e:
        if 'User_already_participant' in str(e):
            await update.message.reply_text(f"You get {tickets_no} free tickets. You are Already in the Telegram Group.\nUse /help command to get help")
        else:
            await update.message.reply_text(
            "Thank you for using our service. However, there was an error adding you to the group. "
            "Please use the following link to join the group: "
            f"<a href='{invite_link}'>Link</a>\nUse /help command to get help",
            parse_mode="HTML"
            )
            print(e)


#use to get hash of the user
async def get_user_access_hash(client,user_id):
    await client.connect()  
    # Try encountering the user through dialogs 
    await client.get_dialogs()
    
    # Attempt to get user entity with access_hash
    try:
        user = await client.get_input_entity(user_id)
        if isinstance(user, InputPeerUser):
            access_hash = user.access_hash
            print(f"Found access_hash: {access_hash}")
            return access_hash
        else:
            print("Couldn't get access_hash for user (might not be encountered yet).")
    except ValueError:
        print("Encountering user failed (user might not be in dialogs).")
    
#can use to get username of the user
async def get_username_by_id(client,user_id): 
  try:
    # Get the user entity
    user = await client.get_entity(user_id)
    
    # Check if username exists
    if user.username:
      username = user.username
      print(username)
      return username
    else:
      return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None
  


