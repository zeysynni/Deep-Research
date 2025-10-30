# Deep Research — Automated Research Workflow using OpenAI SDK and Gradio

This project automates the process of researching a topic using OpenAI’s SDK and a chain of AI agents that plan searches, gather web results, write detailed reports, and send notifications. The system includes a simple Gradio web UI to start a research session.

---

## 🚀 Features
- **Interactive Web UI** using [Gradio](https://www.gradio.app/) to input queries and stream results.
- **Multi-agent architecture** using OpenAI SDK:
  - **Planner Agent** — plans web search queries.
  - **Search Agent** — performs searches and summarizes findings.
  - **Writer Agent** — synthesizes findings into a structured Markdown report.
  - **Notification Agent** — sends a summary via the Pushover API.
- **Async orchestration** for concurrent search execution.
- **OpenAI trace integration** for tracking runs in [OpenAI platform traces](https://platform.openai.com/traces).

---

## 📂 Project Structure
```
.
├── deep_research.py        # Gradio UI entry point
├── research_manager.py     # Orchestrates the research process
├── planner_agent.py        # Plans search terms
├── search_agent.py         # Executes web searches and summarizes
├── writer_agent.py         # Writes long-form research report
├── notification_agent.py   # Sends notifications via Pushover
└── agents/                 # (Imported dependency: defines Agent, Runner, etc.)
```

---

## 🧩 Requirements

Python **3.10+** recommended.

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.\.venv\Scripts\Activate.ps1  # Windows

pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file with the following variables:

```
OPENAI_API_KEY=sk-...
PUSHOVER_TOKEN=your_pushover_app_token
PUSHOVER_USER=your_pushover_user_key
```

---

## 🖥️ Usage

Run the app locally:

```bash
python deep_research.py
```

Then open the automatically launched browser tab (default: http://127.0.0.1:7860) and enter your research topic.

You’ll see streaming updates like:
```
View trace: https://platform.openai.com/traces/trace?trace_id=...
Starting research...
Searches planned, starting to search...
Searches complete, writing report...
Report written, sending email...
Notification sent, research complete.
```

The final Markdown report will be displayed in the Gradio interface.

---

## 🧠 How it Works

1. **deep_research.py** creates the UI and calls `ResearchManager().run(query)`.
2. **ResearchManager** coordinates the full pipeline:
   - Plans searches with `planner_agent`.
   - Performs them concurrently with `search_agent`.
   - Writes a report with `writer_agent`.
   - Sends a push notification with `notification_agent`.
3. Each agent uses the `Agent` abstraction from the `agents` package, backed by OpenAI SDK models like `gpt-4o-mini`.

---

## 📦 requirements.txt
```
openai>=1.51.0
gradiο>=4.44.0
python-dotenv>=1.0.1
requests>=2.32.3
pydantic>=2.8.2
```
---

