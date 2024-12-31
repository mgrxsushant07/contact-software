from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Dictionary to store student data
students = {
    "202301": "Laude Aadush(Aayush Chhetri) mg failed bhanxas randi ramro snaga padh mugii",#For Aayush
    "202302": "B+",
    "202303": "B",
    "202304": "C",
    "202305": "A+",
    "202306": "A",
    "202307": "Laa mugi suddo(Ankit Acharya) rn Failed bhaxau rn rmaro snaga padha arko term ma pass hunu parxa",#For suddo
    "202308": "B+",
    "202309": "C",
    "202310": "Eaa mugi (Bahun)Aryan Poudel khatya padhne gark mugii failed bhaxash yo term ma panii",#For Aryan
    "202311": "A",
    "202312": "B",
    "202313": "B+",
    "202314": "C",
    "202315": "A+",
    "202316": "A",
    "202317": "B",    
    "202318": "",#FOr salin khadka
    "202319": "A+",
    "202320": "A",
    "202321": "B",    
    "202322": "B+",    
    "202323": "C",    
    "202324": "Failed",
    "202325": "A+",    
    "202326": "Eaa mugii padhna ja failed holash mgg gante jhattuu",    
    "202327": "B",    
    "202328": "B+",
    "202329": "C",    
    "202330": "A+",    
    "202331": "Eaa mugi bage(Prajwal Adhikari) rn fialed bhaxash yrr ramro snga padh kti haru na herdherai",#For Bage   
    "202332": "B",
    
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Grade Checker Bot!\nEnter your symbol number to check your grade.")

async def check_grade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol_number = update.message.text.strip()
    grade = students.get(symbol_number)
    
    if grade:
        await update.message.reply_text(f"The grade for symbol number {symbol_number} is: {grade}")
    else:
        await update.message.reply_text("Symbol number not found. Please try again.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = "7871290438:AAH4ZGTmqCpvnS0t1F6TOtKxMSpAQW0xMU4"

    application = Application.builder().token(bot_token).build()

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Message handler for symbol number input
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_grade))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()