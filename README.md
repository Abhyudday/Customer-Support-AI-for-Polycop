# Customer Support AI Bot for Polycop

A Telegram bot that uses OpenAI to answer customer queries based on a custom knowledge base stored in `.md` files. Uses semantic search (embeddings) to find only the relevant information before sending to the AI — **minimizing token usage**.

## How It Works

1. **Knowledge Base**: Your custom data lives in `knowledge_base/*.md` files
2. **Embeddings**: On startup, all `.md` files are chunked and embedded using OpenAI's embedding model
3. **Query Matching**: When a user sends a message, their query is embedded and matched against knowledge base chunks using cosine similarity
4. **AI Response**: Only the top relevant chunks (not the entire database) are sent to OpenAI along with your system prompt

## Setup

### 1. Clone & Install

```bash
cd "/Users/abhyuday/Desktop/mod ai"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your keys:
- `TELEGRAM_BOT_TOKEN` — Get from [@BotFather](https://t.me/BotFather) on Telegram
- `OPENAI_API_KEY` — Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### 3. Customize Knowledge Base

Add/edit `.md` files in the `knowledge_base/` directory. Each file can cover a different topic (products, FAQ, policies, etc.).

### 4. Customize System Prompt

Edit `SYSTEM_PROMPT` in `config.py` to change how the AI responds.

### 5. Run the Bot

```bash
python bot.py
```

## Configuration (`config.py`)

| Setting | Default | Description |
|---------|---------|-------------|
| `CHAT_MODEL` | `gpt-4o-mini` | OpenAI model for responses |
| `EMBEDDING_MODEL` | `text-embedding-3-small` | Model for embeddings |
| `TOP_K_CHUNKS` | `3` | Number of relevant chunks sent to AI |
| `CHUNK_SIZE` | `500` | Max tokens per chunk |
| `CHUNK_OVERLAP` | `50` | Overlap between chunks |

## Bot Commands

- `/start` — Welcome message
- `/help` — Usage examples
- `/reload` — Reload knowledge base (after editing .md files)

## Project Structure

```
mod ai/
├── bot.py                  # Main Telegram bot
├── knowledge_search.py     # Embedding + semantic search engine
├── config.py               # All configuration
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── .env.example            # Template for .env
├── knowledge_base/         # Your custom data
│   ├── about.md
│   ├── products.md
│   └── faq.md
└── README.md
```
