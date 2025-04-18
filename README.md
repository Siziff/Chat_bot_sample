# 🍻 Blaze Chat – Praktika Trial Task

## Stack

- **FastAPI** (async microservice API)
- **OpenAI GPT-4o-mini** for conversational logic
- **Streamlit** as the frontend UI
- **python-dotenv** for managing secrets
- **Custom RAG system** (in-memory keyword retriever)
- **Manual metrics script** for "in-character" analysis

## Project Structure

blaze_chat/ 

├── main.py # FastAPI backend with /chat and /health endpoints 

├── models.py # Pydantic request/response schemas 

├── character.py # Prompt template and OpenAI chat logic 

├── rag_memory.py # RAG retrieval logic 

├── john_facts.py # Static personal facts about John 

├── chat_ui.py # Streamlit frontend (chat interface) 

├── metrics.py # Slang & bar-focus analysis utilities 

├── requirements.txt 

└── README.md

## Installation & Running Locally
    unzip praktika.zip
    cd praktika
    pip install -r requirements.txt


## Set your OpenAI API key
    Create a .env file:
    OPENAI_API_KEY= sk-your-key


## Run FastAPI server
    uvicorn main:app --reload

Chat: POST http://localhost:8000/chat { "message": "Hey Blaze" }
Health: GET http://localhost:8000/health

## Run frontend UI
    streamlit run chat_ui.py
    Open: http://localhost:8501


## Ensuring Blaze stays consistently “edgy” and slang-heavy

### Prompt Engineering
Blaze's system prompt defines:
- Personality: rebellious, energetic, slang-obsessed
- Interests: basketball, skating, memes, dance battles
- Tone: high energy, hype, mischievous

### Message History
- Maintains recent dialogue history (last 10 exchanges) to stay contextual and reactive.

### RAG (Retrieval-Augmented Generation)
- Blaze retrieves facts about John (from john_facts.py) at runtime.
- If John mentions hobbies like "iced coffee", Blaze brings it up naturally:
“Brooo you still on that iced coffee grind?”


## Proposed Metrics for Evaluation

### In-Character Consistency

| Metric              | Description                                                    |
|---------------------|----------------------------------------------------------------|
| Slang Score         | Percent of slang words per response                            |
| Slang Presence      | Does the message include at least 1 slang word?                |
| Energy Indicators   | Count of !, emojis, and hype words like “fr”, “fam”, “yo”      |
| Optional Classifier | Detects "off-style" messages using TF-IDF or embedding model   |

### Bar Scenario Focus

| Metric              | Description                                                    |
|---------------------|----------------------------------------------------------------|
| Bar Word Score      | Percent of bar-related words per response                      |
| Bar Relevance       | Message references bar content if user asks about drinks/food  |
| Semantic Similarity | (Optional) Compare topic to bar-related reference embeddings   |


> Slang and bar scores are calculated using `metrics.py`.

## Credits

Built with by **Ivan Mikheev**  
As part of the **Praktika Senior LLM/AI Engineer** application process.

📧 mikheev.ie@phystech.edu  
🔗 [linkedin.com/in/n01e1se](https://linkedin.com/in/n01e1se)
