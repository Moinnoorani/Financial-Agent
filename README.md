# 📈 Financial AI Agent

**Real-time stock analysis powered by AI agents**  
Fetch live market data, news, and analyst insights with a single command. Built for investors, analysts, and developers.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

- **Live Stock Data**: Prices, fundamentals, and analyst recommendations via `yfinance`
- **Web Search Integration**: Latest news and sources via DuckDuckGo
- **AI-Powered Analysis**: Groq's Llama3 70B model for concise insights
- **Multiple Interfaces**: 
  - CLI for quick queries
  - Web playground for interactive exploration
- **Markdown Output**: Beautifully formatted tables and citations

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys** (create `.env` file):
   ```env
   OPENAI_API_KEY=your_key_here  # Optional for OpenAI fallback
   GROQ_API_KEY=your_key_here
   ```

3. **Run the CLI agent**:
   ```bash
   python financial_agent.py "Summarize NVIDIA stock performance"
   ```

4. **Launch web playground**:
   ```bash
   python playground.py
   ```
   Visit `http://localhost:8000`

## 🛠️ Tech Stack

| Component       | Technology |
|-----------------|------------|
| Core Framework  | `phidata`  |
| LLM             | Groq (Llama3) |
| Data Sources    | yfinance, DuckDuckGo |
| Web Interface   | FastAPI + Uvicorn |
| Output Format   | Markdown |

## 🌟 Example Output

```markdown
## NVIDIA (NVDA) - Analyst Recommendations

| Firm       | Rating | Price Target |
|------------|--------|--------------|
| Morgan Stanley | Overweight | $750 |
| Goldman Sachs | Buy | $800 |

📰 **Latest News**:  
- "NVIDIA unveils next-gen AI chips" (Source: Reuters)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -am 'Add some feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request


### Key Sections Included:
1. **Badges** - For quick visibility of Python version and license
2. **Features** - Highlighting unique value propositions
3. **Setup Instructions** - With clear code blocks
4. **Tech Stack Table** - Visually organized
5. **Example Output** - Showing markdown formatting
6. **Contribution Guidelines** - Standard GitHub flow

Would you like me to:
1. Add a more detailed architecture diagram?
2. Include troubleshooting steps for common issues?
3. Add benchmark comparisons with similar tools?
