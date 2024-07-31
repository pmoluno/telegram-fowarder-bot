from telethon import TelegramClient, events
from .config import API_ID, API_HASH, BOT_TOKEN, SOURCE_GROUP, DESTINATION_GROUP
from .message_modifier import modify_message

class TelegramForwarderBot:
    def __init__(self):
        self.client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

    async def forward_message(self, event):
        if event.chat_id == SOURCE_GROUP:
            modified_text = modify_message(event.message)
            await self.client.send_message(DESTINATION_GROUP, modified_text)

    def run(self):
        @self.client.on(events.NewMessage)
        async def handler(event):
            await self.forward_message(event)

        print("Bot is running...")
        self.client.run_until_disconnected()