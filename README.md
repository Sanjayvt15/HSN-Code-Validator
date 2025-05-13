    # HSN Lookup Agent

A lightweight AI-powered assistant that provides GST information based on HSN codes using Google Gemini via the Agent Development Kit (ADK).

---

## Table of Contents

- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Folder Structure](#folder-structure)
- [Getting API Key](#getting-api-key)
- [Environment Setup](#environment-setup)
- [Code Explanation](#code-explanation)
- [Running the Agent](#running-the-agent)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project allows users to query HSN codes and receive relevant descriptions and applicable GST rates. The agent is built using Google ADK with hardcoded data for demonstration purposes.

---

## Installation Instructions

Open your terminal or command prompt and run the following:

```bash
pip install google-adk pandas openpyxl
```

These libraries are needed to:
- Use the Google Agent Development Kit
- Handle Excel files (optional)

---

## Folder Structure

```
project/
│
├── hsn_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env
│
└── HSN_SAC.xlsx 
```

---

## Getting API Key

1. Go to [MakerSuite](https://makersuite.google.com/app)
2. Sign in with your Google account.
3. Click on your profile picture (top-right).
4. Select **API Keys** → click **Create API Key**.
5. Copy the key for later use.

---

## Environment Setup

Inside `hsn_agent/.env`, paste the following:

```dotenv
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your real Gemini API key.

---

## Code Explanation

### `__init__.py`
Marks `hsn_agent` as a Python module:
```python
from . import agent
```

### `agent.py`

Defines:
- A dictionary of HSN codes and GST rates
- A function `get_hsn_info` to return details for a given HSN code
- A Gemini-based agent using the `Agent` class

```python
from google.adk.agents import Agent

HSN_DATA = {
    "1001": {"description": "Wheat and meslin", "gst": "5%"},
    "8471": {"description": "Automatic data processing machines (Computers)", "gst": "18%"},
    "8703": {"description": "Motor cars and other motor vehicles", "gst": "28%"}
}

def get_hsn_info(hsn_code: str) -> dict:
    ...
    
root_agent = Agent(
    name="hsn_lookup_agent",
    model="gemini-2.0-flash",
    ...
)
```

---

## Running the Agent

From the root project folder, run:

```bash
adk web
```

This starts a local development server at:

```
http://localhost:8000
```

---

## Testing

1. Open your browser and visit: `http://localhost:8000`
2. Use queries like:
   - “What is the GST for HSN 8471?”
   - “Tell me about HSN 1001”
   - “GST rate for code 8703”

---

## Dependencies

- `google-adk` – Gemini agent development
- `pandas` – Excel reading support
- `openpyxl` – Reading `.xlsx` files

---

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Google for the Gemini API and ADK
- Python community for excellent open-source libraries
