import re
from utils.DatabaseHandler import DatabaseHandler
from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes, filters


from utils.event_info import ticket_info_message,EVENT_NAME, EVENT_DATE
from utils.add_group import add_to_group

# Define states for ConversationHandler
NAME, EMAIL, TICKETS = range(3)

# Validate email
def validate_email(email: str) -> bool:
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Starting registration for free tickets... \n Please enter your name:")
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Please enter your email:")
    return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['email'] = update.message.text
    if not validate_email(context.user_data['email']):
        await update.message.reply_text("Invalid email format. Please enter a valid email:")
        return EMAIL 
    await update.message.reply_text("How many tickets do you want?")
    return TICKETS

async def tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['tickets'] = int(update.message.text)
        number_of_tickets = context.user_data['tickets']

        if number_of_tickets > 5 or number_of_tickets < 1:
            await update.message.reply_text("Maximum tickets per request is 5. Please enter a number between 1 and 5.")
            return TICKETS
        
    except ValueError:
        await update.message.reply_text("Please Input valid number between 1 and 5.")
        return TICKETS
    
    user_data = context.user_data
    print(user_data)

    #calling the function for put data into database
    tickets_details=put_data_dataBase(user_data)
    #Sending ticket details to user
    await send_ticket_details(tickets_details,context.user_data['email'],update,context)

    # Add user to the Telegram group
    await add_to_group(update,context,user_data['tickets'])

    await update.message.reply_text(f"Thank you for using our service")
    return ConversationHandler.END

#use to send ticket detils to user
async def send_ticket_details(tickets_details,email,update: Update, context: ContextTypes.DEFAULT_TYPE):
    for ticket in tickets_details:
        message=ticket_info_message(ticket[0],ticket[1],ticket[3],ticket[5],email)
        await update.message.reply_text(message,parse_mode="HTML")


#This will put data into databese and return tickets deatils in list of tuples
def put_data_dataBase(user_data):
    dbHandler=DatabaseHandler('my_database1.db')
    
    name_=user_data['name']
    email_=user_data['email']
    tickets_=user_data['tickets']

    user_id=dbHandler.get_user_id(email_)
    
    if not user_id:
        dbHandler.insert_user(name_,email_)
        user_id=dbHandler.get_user_id(email_)
    
    i=0
    #Need to put all the tickets that request by user
    while(i<tickets_):
        dbHandler.insert_ticket(EVENT_NAME,EVENT_DATE,user_id)
        i=i+1

    #Getting ticket details
    tickets_details=dbHandler.get_tickets_by_email(email_,tickets_)
    return tickets_details

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Registration canceled.')
    return ConversationHandler.END
