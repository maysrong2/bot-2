import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ดึง token จาก Environment ของ Render
TOKEN = os.getenv("BOT_TOKEN")

# คำสั่งเริ่มต้น
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("บอทพร้อมทำงานแล้ว 🚀")

# ฟังก์ชันลบข้อความที่มี keyword
KEYWORDS = ["ลบเลย", "ต้องห้าม"]

async def delete_if_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if any(word in text for word in KEYWORDS):
            await update.message.delete()

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_if_keyword))

    app.run_polling()

if __name__ == "__main__":
    main()
