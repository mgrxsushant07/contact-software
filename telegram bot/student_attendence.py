import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Initialize the database
def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            roll_no INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()

    # Add 30 students with roll numbers
    students = [
        ("Alice", 1), ("Bob", 2), ("Charlie", 3), ("David", 4), ("Eve", 5),
        ("Frank", 6), ("Grace", 7), ("Hannah", 8), ("Isaac", 9), ("Jack", 10),
        ("Karen", 11), ("Leo", 12), ("Mia", 13), ("Nina", 14), ("Oscar", 15),
        ("Paul", 16), ("Quincy", 17), ("Rachel", 18), ("Sam", 19), ("Tina", 20),
        ("Uma", 21), ("Victor", 22), ("Wendy", 23), ("Xavier", 24), ("Yara", 25),
        ("Zane", 26), ("Amber", 27), ("Brian", 28), ("Chloe", 29), ("Dylan", 30)
    ]

    cursor.execute("DELETE FROM attendance")
    for student in students:
        cursor.execute("INSERT INTO attendance (student_name, roll_no, date) VALUES (?, ?, '')", (student[0], student[1]))

    conn.commit()
    conn.close()

# Add attendance to the database
def add_attendance(student_name, roll_no, date):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_name, roll_no, date) VALUES (?, ?, ?)", (student_name, roll_no, date))
    conn.commit()
    conn.close()

# View attendance records
def get_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT student_name, roll_no, date FROM attendance")
    records = cursor.fetchall()
    conn.close()
    return records

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Attendance Bot! Use /mark <roll_no> to mark attendance or /view to view attendance records."
    )

# /mark command handler
async def mark_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        roll_no = int(context.args[0])
        from datetime import datetime
        date = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT student_name FROM attendance WHERE roll_no = ?", (roll_no,))
        student = cursor.fetchone()

        if student:
            student_name = student[0]
            cursor.execute("UPDATE attendance SET date = ? WHERE roll_no = ?", (date, roll_no))
            conn.commit()
            await update.message.reply_text(f"Attendance marked for {student_name} (Roll No: {roll_no}) on {date}.")
        else:
            await update.message.reply_text(f"No student found with Roll No: {roll_no}.")

        conn.close()
    except ValueError:
        await update.message.reply_text("Please provide a valid roll number. Usage: /mark <roll_no>")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

# /view command handler
async def view_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        records = get_attendance()
        if not records:
            await update.message.reply_text("No attendance records found.")
            return

        response = "Attendance Records:\n"
        for student_name, roll_no, date in records:
            status = "Present" if date else "Absent"
            response += f"- {student_name} (Roll No: {roll_no}): {status}\n"

        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

# Main function to set up the bot
def main():
    # Initialize the database
    init_db()

    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token("7552723926:AAEkymH0TkldxkkAQp60H68xDKjK4dU4atk").build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("mark", mark_attendance))
    application.add_handler(CommandHandler("view", view_attendance))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
