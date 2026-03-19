import logging
import base64
from io import BytesIO
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config
from knowledge_search import KnowledgeBase

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize OpenAI client and knowledge base
openai_client = OpenAI(api_key=config.OPENAI_API_KEY)
kb = KnowledgeBase()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    await update.message.reply_text(
        "👋 Hello! I'm the Polycop Customer Support Bot.\n\n"
        "Ask me anything about our products, pricing, orders, or policies.\n"
        "I'm here to help!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    await update.message.reply_text(
        "You can ask me questions like:\n\n"
        "• What products do you offer?\n"
        "• How much does PolyCop Shield Pro cost?\n"
        "• What is your return policy?\n"
        "• How do I place an order?\n"
        "• Do you offer bulk discounts?\n\n"
        "Just type your question and I'll find the answer for you!"
    )


async def reload_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /reload command to refresh the knowledge base."""
    await update.message.reply_text("🔄 Reloading knowledge base...")
    kb.reload()
    await update.message.reply_text(f"✅ Knowledge base reloaded with {len(kb.chunks)} chunks.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming user messages — search KB, build context, call OpenAI."""
    user_query = update.message.text or update.message.caption or ""
    user_name = update.message.from_user.first_name or "Customer"
    has_image = bool(update.message.photo)
    image_base64 = None

    logger.info(f"Query from {user_name} (image={has_image}): {user_query}")

    if not user_query and not has_image:
        await update.message.reply_text("Please send a message or an image with a caption.")
        return

    # Show typing indicator
    await update.message.chat.send_action("typing")

    # Download image if present
    if has_image:
        photo = update.message.photo[-1]  # highest resolution
        file = await photo.get_file()
        buf = BytesIO()
        await file.download_to_memory(buf)
        image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    # Search knowledge base for relevant chunks (using text query)
    results = []
    if user_query:
        results = kb.search(user_query)

    # Build context from retrieved chunks
    context_text = ""
    if results:
        context_parts = []
        for r in results:
            context_parts.append(f"[Source: {r['source']}]\n{r['text']}")
        context_text = "\n\n---\n\n".join(context_parts)

    # Build user message content
    text_payload = ""
    if context_text:
        text_payload += f"Context from knowledge base:\n\n{context_text}\n\n---\n\n"
    text_payload += f"Customer query: {user_query}" if user_query else "Customer sent an image without text."

    if has_image and image_base64:
        # Vision model: send image + text as structured content
        user_content = [
            {"type": "text", "text": text_payload},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
        ]
        model = config.VISION_MODEL
    else:
        # Text-only: use cheaper model
        user_content = text_payload
        model = config.CHAT_MODEL

    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT},
        {"role": "user", "content": user_content}
    ]

    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.3,
            max_tokens=1024
        )
        reply = response.choices[0].message.content
        logger.info(f"Used model: {model}")
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        reply = (
            "I'm having trouble processing your request right now. "
            "Please try again in a moment or contact support@polycop.com."
        )

    await update.message.reply_text(reply)


def main():
    """Start the bot."""
    if not config.TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in .env")
    if not config.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in .env")

    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("reload", reload_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_message))

    logger.info("Bot is starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
