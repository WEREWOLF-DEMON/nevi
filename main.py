import random
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode
import os

# Use environment variable to load the token
TOKEN = '7937364044:AAHUVBKse5Mn3b8JINjxNeO9fvC0bxwHF58'

# List of user IDs that are exempt from message deletion
EXEMPT_USER_IDS = [6545754981, 7379318591]  # Replace these with actual user IDs

# Define the owner’s user ID who can manage the exempt list
OWNER_USER_ID = 6656608288  # Replace with the actual owner's user ID

# Set a maximum length for messages
MAX_MESSAGE_LENGTH = 100

# List of video file URLs to send randomly
VIDEO_LIST = [
    "https://telegra.ph/file/1722b8e21ef54ef4fbc23.mp4",
    "https://telegra.ph/file/ac7186fffc5ac5f764fc1.mp4",
    "https://telegra.ph/file/4156557a73657501918c4.mp4",
    "https://telegra.ph/file/0d896710f1f1c02ad2549.mp4",
    "https://telegra.ph/file/03ac4a6e94b5b4401fa5a.mp4",
]

# Function to create the main inline keyboard
def get_main_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("‣ʜᴇʟᴘ&ᴄᴏᴍᴍᴀɴᴅ‣", callback_data="help"),
            InlineKeyboardButton("‣ᴀᴅᴅ ᴍᴇ‣", url="https://t.me/ProtectorCopyrightBot?startgroup=true"),
        ],
        [
            InlineKeyboardButton("‣ꜱᴜᴘᴘᴏʀᴛ‣", url="https://t.me/kaalCarder"),
            InlineKeyboardButton("‣ᴏᴡɴᴇʀ‣", url="https://t.me/WereWolfDemon"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Function to create the "Back" button to return to the main menu
def get_back_inline_keyboard():
    keyboard = [[InlineKeyboardButton("‣ʙᴀᴄᴋ‣", callback_data="back")]]
    return InlineKeyboardMarkup(keyboard)

# Function to check if a user is exempt from deletion
def is_exempt_user(user_id):
    return user_id in EXEMPT_USER_IDS

# Handler for the /start command
async def start_command(update: Update, context):
    message = update.message

    # Step 1: Animate the message "dιиg dιиg"
    accha = await message.reply_text(
        text="❤️‍🔥ᴅιиg ᴅιиg ꨄ︎ ѕтαятιиg••"
    )
    await asyncio.sleep(0.2)
    await accha.edit_text("💛ᴅιиg ᴅιиg ꨄ︎ sтαятιиg•••")
    await asyncio.sleep(0.2)
    await accha.edit_text("🩵ᴅιиg ᴅιиg ꨄ︎ sтαятιиg•••••")
    await asyncio.sleep(0.2)
    await accha.edit_text("🤍ᴅιиg ᴅιиg ꨄ︎ sтαятιиg••••••••")
    await asyncio.sleep(0.2)
    await accha.delete()

    # Step 2: Select a random video from the VIDEO_LIST
    video_url = random.choice(VIDEO_LIST)

    # Step 3: Prepare the final message caption
    caption = (
        f"╭───────────────────────── \n"
        f"╰──●нυι тнιѕ ιѕ ˹ᴄᴏᴘʏʀɪɢʜᴛ✗ᴘʀᴏᴛᴇᴄᴛᴏʀ˼🤍\n\n"
        f"●ᴏυʀ ᴍιѕѕιᴏɴ ιѕ тᴏ ᴇɴѕυʀᴇ ᴀ ѕᴇᴄυʀᴇ ᴀɴᴅ ᴘʟᴇᴀѕᴀɴт ᴇɴvιʀᴏɴᴍᴇɴт ғᴏʀ ᴇvᴇʀyᴏɴᴇ.\n"
        f"ғʀᴏм ᴄᴏᴘyʀιɢнт ᴘʀᴏтᴇcтιᴏɴ тᴏ ᴍᴀιɴтᴀιɴιɴɢ ᴅᴇcᴏʀυм, ᴡᴇ'vᴇ ɢᴏт ιт cᴏvᴇʀᴇᴅ. 🌙\n\n"
        f"●ɴᴏ cᴏммᴀɴᴅ, ᴊᴜѕт ᴀᴅᴅ тнιѕ ʙᴏᴛ, ᴇvᴇʀyтнιɴɢ ιѕ ᴀυтᴏ 🍁\n\n"
        f"⋆━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ\n"
        f"ᴍᴀᴅᴇ ᴡιтн 🖤 ʙy @WerewolfDemon❣️"
    )

    # Step 4: Send the video with the caption and inline keyboard
    await message.reply_video(
        video=video_url,
        caption=caption,
        parse_mode="HTML",
        reply_markup=get_main_inline_keyboard()
    )

# Handler for button presses
async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        help_text = (
            "💫Here are some commands:\n\n"
            "● [/start] - Start the bot\n"
            "● This bot automatically deletes edited messages, long messages, and shared links or PDFs.🍃\n"
            "● If you want to add a new video, send it to @WerewolfDemon.🤍\n"
            "● If you need any kind of helo dm @WereWolfDemon🩵\n"
            "● If you want to add your self in sudo,contact @WerewolfDemon.💛\n\n"
            "#𝐒ᴀғᴇ ᴇᴄᴏ🍃 , #𝐗ᴏᴛɪᴋ❤️‍🔥"
        )
        await query.message.edit_caption(help_text, reply_markup=get_back_inline_keyboard())

    elif query.data == "back":
        video_url = random.choice(VIDEO_LIST)
        caption = (
            f"╭─────────────────────────\n"
            f"╰──●нυι тнιѕ ιѕ ˹ᴄᴏᴘʏʀɪɢʜᴛ✗ᴘʀᴏᴛᴇᴄᴛᴏʀ˼🤍\n\n"
            f"●ᴏυʀ ᴍιѕѕιᴏɴ ιѕ тᴏ ᴇɴѕυʀᴇ ᴀ ѕᴇᴄυʀᴇ ᴀɴᴅ ᴘʟᴇᴀѕᴀɴт ᴇɴvιʀᴏɴᴍᴇɴт ғᴏʀ ᴇvᴇʀyᴏɴᴇ.\n"
            f"ғʀᴏм ᴄᴏᴘyʀιɢнт ᴘʀᴏтᴇcтιᴏɴ тᴏ ᴍᴀιɴтᴀιɴιɴɢ ᴅᴇcᴏʀυм, ᴡᴇ'vᴇ ɢᴏт ιт cᴏvᴇʀᴇᴅ. 🌙\n\n"
            f"●ɴᴏ cᴏммᴀɴᴅ, ᴊᴜѕт ᴀᴅᴅ тнιѕ ʙᴏᴛ, ᴇvᴇʀyтнιɴɢ ιѕ ᴀυтᴏ 🍁\n\n"
            f"⋆━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ┄ׅ━ׄ\n"
            f"ᴍᴀᴅᴇ ᴡιтн 🖤 ʙy @xazoc❣️"
        )
        await query.message.edit_caption(caption, reply_markup=get_main_inline_keyboard())

# Handler to delete edited messages
async def delete_edited_messages(update: Update, context):
    if update.edited_message:
        user_id = update.edited_message.from_user.id

        # Check if the user is exempt from deletion
        if is_exempt_user(user_id):
            return  # Do nothing if the user is exempt

        user_mention = update.edited_message.from_user.mention_html()

        # Delete the edited message
        await context.bot.delete_message(
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id
        )

        # Notify the group about the deleted edited message
        await context.bot.send_message(
            chat_id=update.edited_message.chat_id,
            text=f"🚫 {user_mention}, edited messages are not allowed and have been deleted!",
            parse_mode=ParseMode.HTML
        )

# Handler to delete links, PDFs, long messages, and notify the user
async def delete_invalid_messages(update: Update, context):
    user_id = update.message.from_user.id

    # Check if the user is exempt from deletion
    if is_exempt_user(user_id):
        return  # Do nothing if the user is exempt

    user_mention = update.message.from_user.mention_html()

    # Check if the message contains a link or PDF
    if (update.message.entities and any(entity.type in [MessageEntity.URL, MessageEntity.TEXT_LINK] for entity in update.message.entities)) or \
            update.message.document:
        await update.message.delete()

        # Notify the group about the deleted message
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"🚫 {user_mention}, links or PDFs are not allowed and have been deleted!",
            parse_mode=ParseMode.HTML
        )

    # Check if the message exceeds the maximum length
    elif len(update.message.text) > MAX_MESSAGE_LENGTH:
        await update.message.delete()

        # Notify the group about the deleted message
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text=f"🚫 {user_mention}, long messages are not allowed and have been deleted!",
            parse_mode=ParseMode.HTML
        )

# Error handler function
async def error_handler(update: Update, context):
    print(f"Error: {context.error}")


# Handler to add user ID to the EXEMPT_USER_IDS list
async def add_user_command(update: Update, context):
    # Only allow the owner to use this command
    if update.message.from_user.id != OWNER_USER_ID:
        await update.message.reply_text("❌ You don't have permission to add users!")
        return

    # Check if the command has the correct arguments
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("❌ Invalid command! Usage: /adduser <user_id>")
        return

    # Get the user ID from the command arguments
    user_id = int(context.args[0])

    # Check if the user is already in the exempt list
    if user_id in EXEMPT_USER_IDS:
        await update.message.reply_text(f"✅ User ID {user_id} is already in the exempt list!")
        return

    # Add the user ID to the exempt list
    EXEMPT_USER_IDS.append(user_id)
    await update.message.reply_text(f"✅ User ID {user_id} has been added to the exempt list!")


# Main function to run the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Add handlers to the application
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, delete_edited_messages))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_invalid_messages))

    # Set the error handler
    application.add_error_handler(error_handler)

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
