from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio, os

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID", "-1003108999761"))

async def site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != GROUP_ID:
        await update.message.reply_text("Bu komut sadece PlayPanda grubunda çalışır.")
        return

    buttons = [
        [InlineKeyboardButton("🌐 Forum Ana Sayfa", url="https://playpanda.me")],
        [InlineKeyboardButton("💎 Sponsorlar Sayfası", url="https://playpanda.me/p/6-sponsorlar")],
        [InlineKeyboardButton("🎯 Rolling Katılım", url="https://playpanda.me/t/panda-rolling")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "🐼 *PlayPanda Forum*\n⚡ Hızlı Erişim Linkleri:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("site", site))

print("🚀 PlayPanda Bot çalışıyor...")
asyncio.run(app.run_polling())
