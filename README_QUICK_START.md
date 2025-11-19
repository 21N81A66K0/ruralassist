# 🌾 RuralAssist - Quick Start Guide

A **multi-agent offline RAG system** for verified rural health and agriculture guidance.

---

## 📋 Table of Contents

- [What is RuralAssist?](#what-is-ruralassist)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Troubleshooting](#troubleshooting)

---

## 🌱 What is RuralAssist?

RuralAssist is an intelligent system that provides:

✅ **Verified Information** - Based on government documents and proven agricultural practices  
✅ **Offline & Private** - Works completely offline, no internet needed  
✅ **Zero Cost** - No cloud APIs, no subscriptions, no billing  
✅ **Smart Agents** - Multi-agent architecture for accurate guidance  
✅ **Local RAG** - Retrieval-Augmented Generation using FAISS vector search  

**Perfect for rural communities with:**
- Limited internet connectivity
- Need for trusted health & farming guidance
- Low-resource devices (Raspberry Pi, laptops)

---

## 🚀 Quick Start (5 minutes)

### Prerequisites
- Python 3.8 or higher
- 2GB+ free disk space
- 2GB+ RAM

### Step 1: Clone & Navigate

```bash
git clone https://github.com/21N81A66K0/ruralassist.git
cd ruralassist
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

*(This will install FAISS, sentence-transformers, pdfminer, and other libraries)*

### Step 4: Build Vector Store (First Time Only)

```bash
python agents/curator.py
```

This will:
- 📄 Parse PDFs from `data/raw/`
- 🔢 Generate embeddings
- 🗂️ Build FAISS index
- ⏱️ Takes ~2-5 minutes depending on data size

### Step 5: Run Test Pipeline

```bash
python test_pipeline.py
```

**Expected Output:**
```
============================================================
RuralAssist - Pipeline Test
============================================================

📝 Query: My maize leaves are turning yellow
------------------------------------------------------------
✅ Category: agriculture

📚 Summary:
[Evidence about nitrogen deficiency...]

📋 Recommended Steps:
   1. Inspect the affected crop section...
   2. Compare symptoms with...
   ...
```

### Step 6: Try Interactive Mode

```bash
python app/orchestrator.py
```

Then type your question:
```
Enter your question for RuralAssist: My maize leaves are turning yellow

=== RuralAssist Response ===
Category: agriculture

Summary of retrieved evidence:
[Evidence text...]

Recommended steps:
1. Inspect the affected crop section...
```

---

## 📥 Installation

### Full Setup Guide

#### Windows

```bash
# 1. Clone repository
git clone https://github.com/21N81A66K0/ruralassist.git
cd ruralassist

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Build vector store
python agents/curator.py

# 5. Test it works
python test_pipeline.py
```

#### macOS/Linux

```bash
# 1. Clone repository
git clone https://github.com/21N81A66K0/ruralassist.git
cd ruralassist

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Build vector store
python agents/curator.py

# 5. Test it works
python test_pipeline.py
```

#### Raspberry Pi (Low-Resource Device)

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3-pip python3-venv

# Clone and setup (same as Linux above)
git clone https://github.com/21N81A66K0/ruralassist.git
cd ruralassist
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Note: First FAISS build may take 5-10 minutes on Pi
python agents/curator.py
```

---

## 🎯 Usage

### Option 1: Interactive CLI (Recommended for Users)

```bash
python app/orchestrator.py
```

Features:
- 💬 Ask natural language questions
- 🌾 Get farming advice
- 🏥 Get health guidance
- 📚 See evidence sources
- ⏱️ Instant responses (no internet needed)

**Example Queries:**
```
"My rice crop has brown spots"
"How to treat fever at home?"
"What fertilizer for tomato plants?"
"My child has a cough"
```

### Option 2: Test Pipeline (For Development)

```bash
python test_pipeline.py
```

Tests:
- ✅ Agriculture queries
- ✅ Health queries
- ✅ Out-of-domain detection
- ✅ Error handling

### Option 3: Programmatic API (For Developers)

```python
import sys
import os
sys.path.insert(0, os.getcwd())

from app.orchestrator import run_pipeline

# Ask a question
result = run_pipeline("My maize leaves are turning yellow")

# Access results
print(f"Category: {result['category']}")
print(f"Advice: {result['advice_steps']}")
```

---

## 📁 Project Structure

```
RuralAssist/
│
├── 📄 README_QUICK_START.md          # This file
├── README.md                          # Full documentation
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package configuration
│
├── 🤖 agents/
│   ├── curator.py                     # Data ingestion & FAISS building
│   ├── query_understanding.py         # Query classification & entity extraction
│   ├── synthesizer.py                 # RAG retrieval & cross-validation
│   └── advisor.py                     # Guidance generation
│
├── 🛠️ tools/
│   ├── pdf_parser.py                  # PDF extraction & chunking
│   ├── embedder.py                    # Embedding generation
│   ├── logger.py                      # Logging & observability
│   └── ...
│
├── 💾 data/
│   ├── raw/                           # Place your PDFs here
│   ├── processed/                     # Parsed chunks (auto-generated)
│   └── vector_store/                  # FAISS index (auto-generated)
│
├── 🧪 tests/
│   └── test_pipeline.py               # Test all agents
│
├── 📖 docs/
│   ├── architecture.md                # System design
│   ├── api_reference.md               # API documentation
│   └── ...
│
└── 🚀 app/
    └── orchestrator.py                # Main entry point
```

---

## ✨ Features

| Feature | Status | Details |
|---------|--------|---------|
| **Offline Operation** | ✅ | Works completely offline, no APIs needed |
| **Multi-Agent** | ✅ | 4 specialized agents for accuracy |
| **FAISS RAG** | ✅ | Fast semantic search on CPU |
| **Zero Cost** | ✅ | No cloud services, no billing |
| **Error Handling** | ✅ | Graceful fallbacks for edge cases |
| **Logging** | ✅ | Full observability & debugging |
| **Multi-Language** | 🔄 | Coming soon (Telugu, Hindi, Bengali) |
| **Android APK** | 🔄 | Mobile version planned |

---

## ❓ Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'agents'`

**Solution:**
Ensure you're in the correct directory and Python path is set:

```bash
cd /path/to/ruralassist
python app/orchestrator.py
```

### Issue: `faiss.index` not found

**Solution:**
Build the vector store first:

```bash
python agents/curator.py
```

This creates the FAISS index from PDFs in `data/raw/`

### Issue: `No such file or directory: 'data/raw'`

**Solution:**
The folder should exist. If not, create it:

```bash
mkdir -p data/raw
```

Then add PDFs and rebuild:

```bash
python agents/curator.py
```

### Issue: Memory errors on low-resource devices

**Solution:**
Reduce batch size in the code or add more PDFs gradually:

```python
# In tools/embedder.py, modify batch size
batch_size = 16  # Reduce from 32
```

### Issue: Very slow on first run

**This is normal!** First run downloads the embedding model (~90MB). Subsequent runs are much faster.

---

## 🎓 Learning Resources

- **Architecture**: Read `docs/architecture.md`
- **API Reference**: Check `docs/api_reference.md`
- **Data Sources**: See `docs/dataset_sources.md`

---

## 🤝 Contributing

Want to improve RuralAssist?

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test
4. Commit: `git commit -m "Add: your feature"`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request

See `CONTRIBUTING.md` for detailed guidelines.

---

## 📜 License

MIT License - See `LICENSE` for details

---

## 🌍 Support

- **GitHub Issues**: Report bugs at https://github.com/21N81A66K0/ruralassist/issues
- **Discussions**: Ask questions at https://github.com/21N81A66K0/ruralassist/discussions
- **Documentation**: Full docs at `docs/`

---

## 🙏 Acknowledgments

Built with ❤️ for rural communities using:
- **FAISS** - Vector search
- **sentence-transformers** - Embeddings
- **pdfminer** - PDF parsing
- **PyTorch** - Deep learning

---

<div align="center">

### ⭐ If RuralAssist helped you, please star the repository!

**Made with ❤️ for rural communities worldwide** 🌱

---

**Version:** 0.1.0  
**Last Updated:** November 19, 2025  
**Status:** Active Development

</div>
