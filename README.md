# RuralAssist: Offline Agent for Verified Rural Guidance

![GitHub License](https://img.shields.io/github/license/21N81A66K0/ruralassist)
![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Contributors](https://img.shields.io/github/contributors/21N81A66K0/ruralassist)

An **Agents for Good** Capstone Project — delivering *trusted, offline, zero-cost* health and farming guidance using a **multi-agent Offline RAG architecture** powered entirely by free, open-source tools.

RuralAssist is a **multi-agent offline intelligence system** designed to combat misinformation and knowledge gaps in rural communities. By combining structured agents with a local **FAISS vector store**, RuralAssist provides reliable and verified guidance on health, agriculture, and essential services — completely offline and at zero recurring cost.

---

## 🌱 Problem

Rural areas face:

- ❌ Poor or no internet connectivity  
- ❌ High spread of misinformation  
- ❌ Limited access to experts  
- ❌ Dependency on cloud tools that require API keys or billing  

This leads to unsafe remedies, crop loss, and reduced community productivity.

**RuralAssist solves this by operating fully offline with zero cloud dependency.**

---

## 🧠 Solution Overview

RuralAssist uses a **Multi-Agent System** to process queries through structured, specialized agents:

- **Data Curator Agent:** Builds local FAISS vector database from public PDFs  
- **Query Understanding Agent:** Processes and classifies user queries  
- **Knowledge Synthesizer Agent:** Retrieves relevant evidence using FAISS  
- **Action Advisor Agent:** Creates clear, safe, verified step-by-step guidance  

All processing happens **offline**, ensuring privacy and zero-cost operation.

---

## 🧩 Key Features

- 🌀 Multi-Agent Architecture  
- 💾 Offline RAG Pipeline (FAISS + Sentence Transformers)  
- 📄 PDF Parsing using pdfminer  
- 📡 100% Offline – No Cloud, No API Keys  
- 🔐 Full Privacy & Zero Billing  
- 🌾 Designed for rural communities & low-resource deployment  

---

## 🧠 Architecture Diagram

<p align="center">
  <img src="docs/architecture.png" alt="RuralAssist Architecture Diagram" width="900">
</p>

---

## 📁 Project Structure

