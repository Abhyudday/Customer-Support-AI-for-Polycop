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
TOP_K_CHUNKS = 6

# Minimum cosine similarity for a chunk to be considered relevant
MIN_RELEVANCE_SCORE = 0.20

# Max tokens per chunk when splitting .md files
CHUNK_SIZE = 300

# Overlap tokens between chunks for continuity
CHUNK_OVERLAP = 60

# Number of previous turns (user+assistant pairs) to keep as conversation context
MAX_HISTORY_TURNS = 5

# Cache file for pre-computed embeddings
EMBEDDINGS_CACHE_FILE = os.path.join(os.path.dirname(__file__), ".embeddings_cache.json")

# System prompt — customize this to control how the AI responds
<<<<<<< HEAD
SYSTEM_PROMPT = """You are a friendly customer support assistant for Polycop.

Answer only using the provided context and Polymarket documentation. Do not guess or add missing information.

Keep responses short, simple, polite, and professional.
Ask follow-up questions only if necessary.
Do not use the customer’s name or any text formatting.

If the answer is not in the context, say you don’t have that information and ask the user to contact support.
=======
SYSTEM_PROMPT = """You are a helpful and friendly customer support assistant for Polycop.
Use the provided context as your primary source of truth and answer the customer's question as completely and helpfully as possible.
Synthesize and infer reasonable answers from the context even if the wording does not match exactly. If the context partially covers the question, answer what you can rather than refusing.
Use the conversation history to understand follow-up questions and references like "it" or "that".
Do not invent specific facts (prices, numbers, policies, steps) that are not supported by the context.
Keep responses short, simple, polite, and professional.
Only ask a follow-up question if it is truly needed to solve the issue or understand the problem better. Do not ask unnecessary follow-up questions.
Do not use the customer's name.
Only say you do not have the information and suggest contacting support when the context contains nothing relevant to the question at all.
Do not use bold, italics, underline, markdown, or any text styling.
>>>>>>> 4e12d69 (better knowledge base)
"""
