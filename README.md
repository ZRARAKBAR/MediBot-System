#  MediBot-System

> Multi-version AI Medical Assistant System with NLP, rule-based reasoning, and dataset-driven API architecture.

---

##  Overview

MediBot-System is an evolving AI healthcare assistant project that demonstrates the full lifecycle of building an AI system:

- Early stage: NLP-based symptom extraction engine (standalone core)
- Current stage: API-driven medical inference system
- Data-driven design using structured JSON and CSV medical datasets

The system simulates how real-world AI applications evolve from **prototype NLP modules → scalable backend systems**.

---

##  System Evolution

### 🔹 Phase 1 — NLP Core (Legacy / Conceptual Layer)
- Symptom extraction using NLP techniques
- Tokenization, stopword removal, fuzzy matching
- CSV-based symptom dataset processing
- Alias handling for medical terms

> ⚠️ This layer was used in early development and is now abstracted into the system design.

---

### 🔹 Phase 2 — MediBot API System (Current)

The active system is now **API + dataset driven**:

- JSON + CSV based medical knowledge engine
- Disease → symptoms → treatment mapping
- Structured response generation
- Rule-based medical inference engine
- No dependency on standalone NLP runtime module

---

##  System Architecture


User Input
↓
(API Request Layer)
↓
Medical Inference Engine
↓
Dataset Layer (CSV + JSON)
├── disease_info_100.csv
├── medicine_book.csv
├── symptoms_alias.json
↓
Response Generator
↓
Structured Output (Tests / Medicines / Precautions)


---

##  Data Sources

###  CSV Datasets
- `disease_info_100.csv` → recommended tests
- `medicine_book.csv` → medicines & dosage

###  JSON Dataset
- `symptoms_alias.json`
  - maps synonyms of symptoms
  - improves matching accuracy
  - reduces dependency on strict NLP preprocessing

---

##  Key Features

- 🧠 Rule-based medical reasoning engine
- 📊 Dataset-driven decision system
- 🧾 JSON alias-based symptom normalization
- 💊 Medicine + dosage suggestion system
- ⚠️ Safety precaution engine (avoid list)
- 🔗 API-ready modular structure
- 📦 Scalable design for ML/LLM upgrade

---

##  Project Structure


MediBot-System/
│
├── medibot-api/
│ ├── app.py
│ ├── chatbot.py
│ ├── tempeplates
│
├── medibot-core/ (legacy NLP concept)
│ ├── nlp_processor.py
│ ├── greetings.py
│
├── data/
│ ├── disease_info_100.csv
│ ├── medicine_book.csv
│ ├── symptoms_100.csv
│ ├── symptoms_alias.json
│
├── README.md
└── ARCHITECTURE.md


---

##  Design Philosophy

- Separation of data and logic
- Dataset-first AI design (CSV/JSON driven)
- Modular system evolution (core → API → scalable system)
- Rule-based interpretability over black-box ML
- Future-ready for LLM integration

---

##  Future Improvements

- FastAPI deployment layer
- LLM-based diagnosis enhancement
- Confidence scoring system
- Web UI dashboard
- Real-time medical API integration
- Hybrid ML + rule-based system

---

## ⚠️ Disclaimer

MediBot-System is an educational AI project built for learning NLP, backend design, and AI system architecture.  
It is **not intended for real medical diagnosis or treatment**.

---

##  Author

**ZRAR AKBAR**  
Computer Science Student | AI & Software Engineering Enthusiast

---

##  Project Goal

To demonstrate:
- Real-world AI system evolution
- NLP to API transition architecture
- Dataset-driven intelligence systems
- Scalable backend design principles
