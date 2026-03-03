# 🧪 Gen AI Practice Lab

Quick reference guide for my AI development practice code.

## � Directory Map
| Folder | Purpose |
| :--- | :--- |
| `CineSage/` | Structured movie metadata extraction from raw text. |
| `chatmodels/` | Various LLM chat implementations (CLI, UI, Local, API). |
| `embeddingmodels/` | Vector embedding generation (Google, HuggingFace). |

## 🚀 Quick Run Commands
- **Dynamic UI Chatbot**: `streamlit run chatmodels/UIchatbot.py`
- **CLI Mood Chatbot**: `python chatmodels/chatbot.py`
- **Movie Extraction**: `python CineSage/core.py`
- **DeepSeek API Test**: `python chatmodels/huggingface.py`
- **TinyLlama Local**: `python chatmodels/localmodel.py` (M1/M2/M3 optimized)

## 🛠️ Setup Reminder
1. **Sync Env**: `uv sync`
2. **Secrets**: Ensure `.env` has:
   - `MISTRAL_API_KEY`
   - `GOOGLE_API_KEY`
   - `HUGGINGFACEHUB_API_TOKEN`
   - `GROQ_API_KEY`

## 🧩 Key Models Used
- **Mistral**: `mistral-small-2506` (Primary chat/logic)
- **Google**: `gemini-embedding-001` (Embeddings)
- **DeepSeek**: `DeepSeek-R1` via HuggingFace Endpoint
- **Groq**: `llama-3.3-70b-versatile` (Ultra fast)
- **Local**: `TinyLlama-1.1B` (Hardware testing)
