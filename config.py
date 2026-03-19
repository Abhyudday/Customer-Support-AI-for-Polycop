import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Directory containing your .md knowledge base files
KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), "knowledge_base")

# OpenAI model for text-only queries (cheaper)
CHAT_MODEL = "gpt-4o-mini"

# OpenAI model for image queries (vision-capable)
VISION_MODEL = "gpt-4o"

# OpenAI model for embeddings
EMBEDDING_MODEL = "text-embedding-3-small"

# Number of top relevant chunks to include in context
TOP_K_CHUNKS = 3

# Max tokens per chunk when splitting .md files
CHUNK_SIZE = 500

# Overlap tokens between chunks for continuity
CHUNK_OVERLAP = 50

# Cache file for pre-computed embeddings
EMBEDDINGS_CACHE_FILE = os.path.join(os.path.dirname(__file__), ".embeddings_cache.json")

# System prompt — customize this to control how the AI responds
SYSTEM_PROMPT = """You are a helpful and friendly customer support assistant for Polycop.
Answer only using the provided context.
Do not guess or add information that is not in the context.
Keep responses short, simple, polite, and professional.
Only ask a follow-up question if it is truly needed to solve the issue or understand the problem better.
Do not ask unnecessary follow-up questions.
Do not use the customer’s name.
If the answer is not in the context, say that you do not have that information and ask the customer to contact support directly.
Do not use bold, italics, underline, markdown, or any text styling.
"""
