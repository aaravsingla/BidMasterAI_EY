# ⚡ BidMaster AI: Autonomous RFP Orchestration Engine

> **Winner Strategy for EY Techathon 6.0 | Challenge IV** > *Transforming B2B Tender Responses from "5 Days" to "5 Minutes"*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Prototype%20Live-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)]()

---

## 📖 Executive Summary

**BidMaster AI** is an agentic workflow solution designed to solve the critical bottleneck in Industrial B2B Manufacturing: the slow, manual, and error-prone process of responding to Government RFPs (Requests for Proposals).

By deploying a multi-agent system, we automate the lifecycle of tendering—from identifying opportunities on portals to generating legally compliant, technically validated commercial bids.

### 🎯 The Problem
- **Lost Revenue:** 90% of tender wins correlate to early submission, yet manual discovery causes delays.
- **Engineering Burnout:** Technical teams spend 70% of their time searching for datasheets instead of validating designs.
- **Compliance Risk:** Manual copy-pasting leads to pricing errors and missed "poison pill" clauses.

### 🚀 The Solution
A "Human-in-the-Loop" Autonomous System featuring:
1.  **Sales Agent:** 24/7 Portal Scanner & "Right-to-Win" Predictor.
2.  **Technical Agent:** RAG-based Parametric Engine that maps RFP specs to internal SKUs.
3.  **Pricing Agent:** Real-time ERP lookups for dynamic margin estimation.

---

## 💡 Key Innovations (The "Secret Sauce")

### 1. 🔍 Semantic Parametric Matching (Not Just Keywords)
Standard AI compares text. **BidMaster AI** extracts engineering parameters (e.g., *Voltage: 1100V*, *Sheath: FRLS*) and performs a weighted vector search against the OEM datasheet repository.

### 2. ⚠️ Automated Gap Analysis & "Make-to-Order" Trigger
If an exact SKU isn't found, the system doesn't fail. It explicitly calculates the **delta** (e.g., *"Gap Detected: RFP requires Strip Armour, SKU has Round Wire"*). 
* **Impact:** Turns potential "No-Bids" into new manufacturing revenue streams.

### 3. 📊 "Right-to-Win" Predictive Scoring
We don't just bid on everything. The system assigns a confidence score based on historical win rates, competitor density, and margin potential.

---

## 🛠️ Technology Stack

| Component | Prototype (This Repo) | Final Industry Solution |
| :--- | :--- | :--- |
| **Frontend** | Streamlit (Python) | React.js / Next.js |
| **Orchestration** | Python Functions | LangChain / LangGraph |
| **AI / LLM** | Simulated Logic | Azure OpenAI (GPT-4o) |
| **Database** | JSON / CSV Flat Files | Pinecone (Vector) + PostgreSQL |
| **Visualization** | Plotly / Matplotlib | PowerBI Embedded |
| **Output** | FPDF (PDF Gen) | Enterprise PDF Engine |

---

## 🏗️ Architecture

```mermaid
graph TD
    User[Government Portal] -->|Scrape| SalesAgent[🕵️ Sales Agent]
    SalesAgent -->|Filter| WinModel{⚡ Right-to-Win Model}
    WinModel -- High Score --> Orchestrator[🤖 Main Orchestrator]
    
    Orchestrator --> TechAgent[🔧 Technical Agent]
    TechAgent <-->|Vector Search| DB[(Datasheets DB)]
    TechAgent -->|Gap Analysis| Orchestrator
    
    Orchestrator --> PricingAgent[💰 Pricing Agent]
    PricingAgent <-->|Cost Lookup| ERP[(Enterprise ERP)]
    
    PricingAgent --> Output[📄 Final Proposal PDF]
'''
h
