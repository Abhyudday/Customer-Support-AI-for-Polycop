import os
import json
import hashlib
import numpy as np
from openai import OpenAI
import tiktoken
import config


client = OpenAI(api_key=config.OPENAI_API_KEY)
tokenizer = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))


def chunk_text(text: str, source: str, chunk_size: int = config.CHUNK_SIZE, overlap: int = config.CHUNK_OVERLAP) -> list[dict]:
    """Split text into overlapping chunks based on token count."""
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append({
            "text": chunk_text.strip(),
            "source": source,
            "token_count": len(chunk_tokens)
        })
        start += chunk_size - overlap

    return chunks


def load_knowledge_base() -> list[dict]:
    """Load all .md files from the knowledge base directory and split into chunks."""
    all_chunks = []
    kb_dir = config.KNOWLEDGE_BASE_DIR

    if not os.path.exists(kb_dir):
        print(f"Knowledge base directory not found: {kb_dir}")
        return all_chunks

    for filename in sorted(os.listdir(kb_dir)):
        if filename.endswith(".md"):
            filepath = os.path.join(kb_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            chunks = chunk_text(content, source=filename)
            all_chunks.extend(chunks)

    print(f"Loaded {len(all_chunks)} chunks from {kb_dir}")
    return all_chunks


def get_content_hash(chunks: list[dict]) -> str:
    """Generate a hash of all chunk texts to detect changes."""
    combined = "".join(c["text"] for c in chunks)
    return hashlib.md5(combined.encode()).hexdigest()


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Get embeddings from OpenAI for a list of texts."""
    response = client.embeddings.create(
        model=config.EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


class KnowledgeBase:
    def __init__(self):
        self.chunks: list[dict] = []
        self.embeddings: np.ndarray | None = None
        self._load_and_embed()

    def _load_and_embed(self):
        """Load knowledge base, compute or load cached embeddings."""
        self.chunks = load_knowledge_base()

        if not self.chunks:
            print("No knowledge base chunks found.")
            return

        content_hash = get_content_hash(self.chunks)

        # Try loading from cache
        if os.path.exists(config.EMBEDDINGS_CACHE_FILE):
            try:
                with open(config.EMBEDDINGS_CACHE_FILE, "r") as f:
                    cache = json.load(f)
                if cache.get("hash") == content_hash:
                    self.embeddings = np.array(cache["embeddings"])
                    print(f"Loaded {len(self.embeddings)} cached embeddings.")
                    return
            except (json.JSONDecodeError, KeyError):
                pass

        # Compute new embeddings
        print("Computing embeddings for knowledge base...")
        texts = [c["text"] for c in self.chunks]
        raw_embeddings = get_embeddings(texts)
        self.embeddings = np.array(raw_embeddings)

        # Save to cache
        cache = {
            "hash": content_hash,
            "embeddings": [e.tolist() for e in self.embeddings]
        }
        with open(config.EMBEDDINGS_CACHE_FILE, "w") as f:
            json.dump(cache, f)
        print(f"Computed and cached {len(self.embeddings)} embeddings.")

    def search(self, query: str, top_k: int = config.TOP_K_CHUNKS) -> list[dict]:
        """Find the top-k most relevant chunks for a given query."""
        if not self.chunks or self.embeddings is None:
            return []

        query_embedding = np.array(get_embeddings([query])[0])

        similarities = []
        for i, chunk_emb in enumerate(self.embeddings):
            sim = cosine_similarity(query_embedding, chunk_emb)
            similarities.append((i, sim))

        similarities.sort(key=lambda x: x[1], reverse=True)

        results = []
        for idx, score in similarities[:top_k]:
            results.append({
                "text": self.chunks[idx]["text"],
                "source": self.chunks[idx]["source"],
                "score": round(score, 4)
            })

        return results

    def reload(self):
        """Reload the knowledge base (useful if .md files are updated)."""
        self._load_and_embed()
