# GenRuntime Demo — Reliable Structured LLM Extraction

This project demonstrates how to use **GenRuntime** to build reliable LLM-powered applications that produce validated structured outputs.

The application extracts structured information from unstructured resume text using **Anthropic Claude** through GenRuntime, which provides reliability features such as:

- Schema validation
- Retry handling
- Provider abstraction
- Observability metadata

The goal of this project is to demonstrate how GenRuntime can act as a **runtime layer** between applications and LLM providers.

---

## What is GenRuntime?

**GenRuntime** is a runtime abstraction layer for LLM inference.

- GitHub: [https://github.com/tejaspawar12/GenRuntime](https://github.com/tejaspawar12/GenRuntime)
- PyPI: [https://pypi.org/project/genruntime/](https://pypi.org/project/genruntime/)

Instead of calling an LLM provider directly, applications interact with GenRuntime, which handles:

- Provider integration
- Structured output enforcement
- Retries and error handling
- Request metadata and observability

### Architecture

```
Application
     ↓
GenRuntime
     ↓
LLM Provider (Anthropic / OpenAI / Bedrock / Local models)
```

This design makes LLM systems more **reliable** and **production-ready**.

---

## Why GenRuntime?

Raw LLM APIs have several challenges in production systems:

- Inconsistent output formats
- Malformed JSON responses
- Provider-specific API logic
- Lack of retry handling
- Limited observability

GenRuntime solves these by providing:

| Problem | GenRuntime Solution |
|---------|---------------------|
| Inconsistent outputs | Schema validation |
| Invalid JSON | Structured generation |
| Provider coupling | Provider abstraction |
| Transient failures | Retry handling |
| Lack of monitoring | Metadata tracking |

---

## What This Project Demonstrates

This project shows how to build a structured LLM pipeline using GenRuntime.

The system extracts structured information from resume text and returns validated JSON.

### Pipeline

```
Client (Swagger / curl)
        ↓
FastAPI API
        ↓
GenRuntime
        ↓
Anthropic Claude
        ↓
Pydantic Schema Validation
        ↓
Structured JSON Response
```

### Example Input

```
Tejas Pawar
Email: tejas@email.com
Skills: Python, SQL, FastAPI
Education: MS Data Science, University of Delaware
Experience: Graduate Assistant, UD IT-ATS
```

### Example Output

```json
{
  "parsed": {
    "name": "Tejas Pawar",
    "email": "tejas@email.com",
    "skills": [
      "Python",
      "SQL",
      "FastAPI"
    ],
    "education": [
      "MS Data Science, University of Delaware"
    ],
    "experience": [
      "Graduate Assistant, UD IT-ATS"
    ]
  },
  "meta": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-6",
    "latency_ms": 1911,
    "input_tokens": 210,
    "output_tokens": 75
  }
}
```

The response includes both **validated structured data** and **runtime metadata**.

---

## Tech Stack

- Python
- FastAPI
- GenRuntime
- Anthropic Claude
- Pydantic
- Uvicorn

---

## Project Structure

```
project-root
│
├── app/
│   └── main.py        # FastAPI API + GenRuntime integration
│
├── schemas.py         # Structured output schema
├── prompts.py         # Prompt construction
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

**Clone the repository:**

```bash
git clone https://github.com/tejaspawar12/GenRuntime-Demo-Reliable-Structured-LLM-Extraction.git
cd GenRuntime-Demo-Reliable-Structured-LLM-Extraction
```

**Create a virtual environment:**

```bash
python -m venv .venv
```

**Activate the environment:**

Mac/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
GENRUNTIME_PROVIDER=anthropic
GENRUNTIME_MODEL=claude-sonnet-4-6
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Running the API

**Start the server:**

```bash
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

**Available endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/debug/env` | Debug environment |
| POST | `/extract/resume` | Extract resume data |

---

## Example Request

**POST /extract/resume**

Request body:

```json
{
  "document_text": "Tejas Pawar\nEmail: tejas@email.com\nSkills: Python, SQL, FastAPI\nEducation: MS Data Science, University of Delaware\nExperience: Graduate Assistant, UD IT-ATS",
  "model": null,
  "timeout": 60,
  "max_retries": 2
}
```

---

## Key Takeaway

This project demonstrates how **GenRuntime** enables reliable LLM applications by acting as a runtime layer between the application and LLM providers, ensuring **structured outputs**, **retries**, and **observability**.

---

## Author

**Tejas Pawar**  
MS Data Science — University of Delaware
