
# Gemini Chatbot with Streamlit

Interact with Google's Gemini model in a conversational web app built using [Streamlit](https://streamlit.io/) and the [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/quickstart#install-gemini-library).

---

## Features

- Conversational chat UI (Streamlit)
- Google Gemini (genai) model integration
- Persistent chat history

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sheikh-mohammad-rakib/chatbot.git
cd chatbot
```

### 2. Create and activate a virtual environment

- **Windows**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS/Linux**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Google GenAI credentials

You need a Google GenAI API key. You can store it in a `.env` file or set it as an environment variable.

#### Using a `.env` file (recommended for local development):
1. Copy the provided `.env.example` file to `.env`:
   - **macOS/Linux**:
     ```bash
     cp .env.example .env
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     copy .env.example .env
     ```
2. Open `.env` and replace the placeholder with your actual API key.
3. Ensure your code loads environment variables from `.env` (e.g., with the `python-dotenv` package).

#### Alternatively, set as an environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

On Streamlit Cloud, add this as a secret in the app settings.

### 5. Run the app locally

```bash
streamlit run chat_gemini.py
```

---

## File Structure

- `chat_gemini.py` — Main Streamlit app
- `requirements.txt` — Python dependencies
- `.env.example` — Example environment variable file
- `README.md` — Project documentation

---

## License

MIT
