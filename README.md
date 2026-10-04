<<<<<<< HEAD
# Local RAG Assistant

> A fully local, privacy-first RAG assistant for your notes and documents — chat with your knowledge base without sending a single byte to the cloud.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Powered by Ollama](https://img.shields.io/badge/powered%20by-Ollama-black)](https://ollama.com/)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](#roadmap)

## Overview

**Local RAG Assistant** is a desktop application that turns your personal notes and documents into a searchable, conversational knowledge base. It combines hybrid retrieval (vector search + BM25) with a locally hosted LLM to answer questions in natural language — while keeping 100% of your data on your machine.

No accounts. No telemetry. No external APIs. Just you, your notes, and a local model.

### Why?

- 🔒 **Privacy by design** — everything runs offline. Your data never leaves your device.
- 🧠 **Hybrid RAG** — semantic search finds meaning, BM25 finds exact terms. You get the best of both.
- 📝 **Notes-first** — lightweight reminders and a Markdown editor built around your notes, not the other way around.
- ⚡ **Modern stack** — `uv`, Ollama, Qwen 2.5, Chroma, and a clean Python core.

## Key Features

- **Multi-format ingestion** — import `.txt`, `.md`, `.pdf` (with OCR), and `.docx`.
- **Hybrid retrieval** — vector search (embeddings) + BM25 fused via Reciprocal Rank Fusion.
- **Local LLM** — powered by [Ollama](https://ollama.com/) with Qwen 2.5 (7B / 14B).
- **Markdown-native chat** — answers rendered with sources and expandable chunks.
- **Note management** — tags, colors, folders, favorites, soft-delete, and a Markdown editor with live preview.
- **Reminders** — attach time-based or recurring reminders to specific notes (not a full task manager, by design).
- **Extensible** — pluggable embedders, LLMs, and parsers.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.11+ |
| Package manager | [uv](https://github.com/astral-sh/uv) |
| LLM runtime | [Ollama](https://ollama.com/) |
| Default LLM | Qwen 2.5 (7B / 14B) |
| Embeddings | `nomic-embed-text`, `bge-m3` |
| Vector store | Chroma (default) / Qdrant (optional) |
| Metadata store | SQLite + SQLAlchemy |
| RAG framework | LlamaIndex |
| Scheduler | APScheduler |
| PDF parsing | PyMuPDF, Tesseract (OCR) |
| DOCX parsing | python-docx |

## Prerequisites

Before you begin, make sure you have:

- **Python 3.11 or newer**
- **[uv](https://github.com/astral-sh/uv)** — fast Python package manager
- **[Ollama](https://ollama.com/download)** — running locally

Pull the required models:

```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

> If you have a GPU with 12+ GB VRAM, you can use `qwen2.5:14b` for better answers.

## Installation

Clone the repository and install dependencies with `uv`:

```bash
git clone https://github.com/[your-username]/local-rag-assistant.git
cd local-rag-assistant
uv sync
```

Copy the example environment file and adjust if needed:

```bash
cp .env.example .env
```

On Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

## Usage

Make sure Ollama is running, then launch the assistant:

```bash
uv run python -m app.main
```

On first run, the app will:

1. Create its data directory (`~/.local_rag_assistant/`).
2. Verify that Ollama is reachable.
3. Check that the required models are installed.

Expected output:

```
2025-XX-XX ... | INFO | Запуск Local RAG Assistant
2025-XX-XX ... | INFO | Папка данных: /home/user/.local_rag_assistant
2025-XX-XX ... | INFO | Ollama доступен. Модели: ['qwen2.5:7b', 'nomic-embed-text']
```

> **Note:** the CLI is a work in progress. The desktop UI will land in a future release — see [Roadmap](#roadmap).

## Project Structure

```
local-rag-assistant/
├── app/
│   ├── config.py           # Settings loaded from .env
│   ├── main.py             # Entry point
│   ├── core/
│   │   ├── rag/            # Chunking, embeddings, retrieval
│   │   ├── storage/        # SQLite + Chroma
│   │   └── llm/            # Ollama client
│   └── ui/                 # Desktop UI (future)
├── tests/
├── pyproject.toml
├── uv.lock
├── .env.example
├── LICENSE
└── README.md
```

## Roadmap

- [x] **Stage 0** — Project scaffolding, config, Ollama health check
- [ ] **Stage 1 (MVP)** — `.txt` / `.md` ingestion, vector search, chat with Qwen, note editor, tags
- [ ] **Stage 2** — PDF & DOCX, hybrid search (vector + BM25), reminders, dark theme
- [ ] **Stage 3** — Reranking, auto-tagging, summarization, graph view, export, hotkeys
- [ ] **Stage 4** — Semantic reminders, plugins & integrations

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR. For bug reports and feature requests, use the GitHub Issues tab.

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.com/) — for making local LLMs painless
- [Qwen](https://github.com/QwenLM/Qwen2.5) — for an excellent open model family
- [Chroma](https://www.trychroma.com/) and [LlamaIndex](https://www.llamaindex.ai/) — for the RAG building blocks
- [Astral](https://astral.sh/) — for `uv` and `ruff`
=======
# local-rag-assistant
Local RAG-assistant for notes and documents
>>>>>>> f0bdeb1437f1f353f40d0fa3adb29991f8b9e08d
