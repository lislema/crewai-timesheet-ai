# CrewAI Timesheet Anomaly Detector

This project uses **CrewAI agents** and OpenAI LLMs to analyze employee timesheet data from Excel, detect anomalies, and generate professional HR summaries.

---

## 🧩 Overview

**CrewAI Roles:**

- `DataLoaderAgent`: Loads timesheet data from Excel files.
- `AnomalyAgent`: Detects anomalies like overwork, underwork, long lunches, sick leave, and vacations.
- `QueryAgent`: Summarizes anomalies using OpenAI (via GPT-3.5-turbo).
- `SupervisorAgent`: Coordinates the full flow, including report generation and summary orchestration.

**Input:**  
An Excel file in `data/` named like: `timesheet_may2025.xlsx`

**Output:**
- Anomaly reports in `/reports/` folder, one Excel file per anomaly type.
- Console summary via the LLM (or optionally written to file).

---

## ✅ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crewai-timesheet-ai.git
cd crewai-timesheet-ai
```

### 2. Create the `.env` File

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Requirements

We recommend using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 4. Run the Supervisor

```bash
python main.py
```

---

## 📊 Anomalies Detected

- Over 9 hours/day
- Under 9 hours/day
- Long lunches (> 2 hours)
- Sick leave
- Vacation

Each anomaly is exported to a separate timestamped Excel file.

---

## 📁 Project Structure

```
crewai_timesheet_ai/
├── agents/
│   ├── anomaly_agent.py
│   ├── data_loader_agent.py
│   ├── query_agent.py
│   └── supervisor_agent.py
├── tools/
│   ├── excel_utils.py
│   └── reporting.py
├── data/
│   └── timesheet_may2025.xlsx
├── reports/
├── main.py
├── .env              # <-- Not included in repo
├── .gitignore
└── requirements.txt
```

---

## 🛡️ Notes

- Do **not commit your `.env`** file.
- OpenAI token limits are respected through intelligent chunking.
- Extendable with Slack, email, or database integrations.

---

## 🧠 Future Enhancements

- Agent memory and chat history
- Web dashboard (Streamlit)
- CLI summaries
- Support for custom anomaly rules

---

Built with ❤️ using CrewAI + OpenAI by Mark Antony.
