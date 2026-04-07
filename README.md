# ✈️ TravelBuddy – AI Travel Assistant (LangGraph)

TravelBuddy is an intelligent travel assistant built with **LangGraph + LLM + Tool Calling**.
It helps users plan trips by searching flights, suggesting hotels, and calculating budgets — all through natural conversation.

---

## 🚀 Features

* ✈️ Search flights between cities
* 🏨 Recommend hotels based on budget
* 💰 Calculate trip expenses
* 🤖 ReAct-style AI agent (tool-calling + reasoning)
* 🇻🇳 Vietnamese conversational assistant

---

## 🧠 Architecture

```
User → Agent (LLM) → Tools → Agent → Response
```

* **Agent Node**: decides whether to call tools
* **Tool Node**: executes functions (`search_flights`, `search_hotels`, `calculate_budget`)
* **StateGraph (LangGraph)**: controls flow

---

## 📁 Project Structure

```
.
├── agent.py            # Main agent + LangGraph flow
├── tools.py            # Tool implementations (flight, hotel, budget)
├── system_prompt.txt   # Agent behavior (persona, rules, format)
├── test_api.py         # API test (LLM connection)
├── test_results.md     # Example outputs
└── README.md
```

---

## ⚙️ Setup

### 1. Create environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```bash
pip install langchain langgraph langchain-openai langchain-azure-ai python-dotenv
```

### 3. Add API key

Create `.env`:

```env
OPENAI_API_KEY=your_key_here
```

---

## ▶️ Run

```bash
python agent.py
```

---

## 💬 Example Usage

```
Bạn: Tìm chuyến bay từ Hà Nội đến Đà Nẵng
→ Agent gọi tool search_flights

Bạn: Đi Phú Quốc 2 đêm, budget 5 triệu
→ Agent gọi nhiều tools:
   - search_flights
   - search_hotels
   - calculate_budget
```

---

## 🔧 Tools

### `search_flights(origin, destination)`

* Tìm chuyến bay giữa 2 thành phố

### `search_hotels(city, max_price_per_night)`

* Gợi ý khách sạn theo ngân sách

### `calculate_budget(total_budget, expenses)`

* Tính chi phí và tiền còn lại

---

## 🧩 Key Concepts

* **LangGraph State**:

  ```python
  messages: Annotated[list, add_messages]
  ```

  → lưu lịch sử hội thoại

* **Tool Calling**:
  LLM quyết định khi nào gọi tool

* **Conditional Edges**:

  ```python
  builder.add_conditional_edges("agent", tools_condition)
  ```

---

## 📌 Notes

* Supports Vietnamese natural conversation
* Uses simple in-memory database (no external API)
* Designed for learning **AI Agents + LangGraph**

---

## 📈 Future Improvements

* Add real API (Skyscanner, Booking)
* UI (Streamlit / Web app)
* Multi-language support
* Memory persistence

---

## 👨‍💻 Author

* Khang-Water

---

## ⭐ Summary

This project demonstrates how to build a **real AI agent with tool usage**, not just a chatbot.
