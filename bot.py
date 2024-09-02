from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import yt_dlp
import requests
import instaloader
from pytube import YouTube

# Replace with your actual Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Start command handler
def start(update, context):
    update.message.reply_text("Welcome to Social Media Downloader Bot! Send me a link and I'll download it for you.")

# Instagram download handler
def download_instagram(update, context):
    url = update.message.text
    loader = instaloader.Instaloader()
    try:
        loader.download_profile(url, profile_pic_only=True)
        update.message.reply_text("Downloaded Instagram content!")
    except Exception as e:
        update.message.reply_text(f"Failed to download Instagram content: {e}")

# YouTube download handler
def download_youtube(update, context):
    url = update.message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        update.message.reply_text("Downloaded YouTube video!")
    except Exception as e:
        update.message.reply_text(f"Failed to download YouTube video: {e}")

# Unknown command handler
def unknown(update, context):
    update.message.reply_text("Sorry, I didn't understand that command.")

# Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), download_youtube))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), download_instagram))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
