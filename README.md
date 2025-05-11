## Farmers Schemes Chatbot
🧑‍🌾 Farmers Scheme Chatbot (Tamil & English Support)
Agriculture is the backbone of many communities, and governments offer numerous schemes to support farmers. However, many farmers are either unaware of these schemes or find it difficult to access the right information—especially in their native language.

This Farmers Scheme Chatbot is an intelligent conversational assistant built using the Rasa open-source framework. It helps farmers and agricultural stakeholders quickly discover and understand government schemes relevant to their needs by simply asking questions in Tamil or English.

🎯 Key Features
🗣️ Bilingual Support: Ask questions in either Tamil or English.

📚 Scheme Recommendation: Get government schemes related to irrigation, seeds, subsidies, loans, insurance, and more.

🌐 Web Interface: Easy-to-use HTML frontend for chatting with the bot.

⚙️ Custom Rasa Actions: Backend logic to fetch or process scheme-related information.

🧠 Trainable: Add new intents, languages, and schemes easily via training data.

🧩 Extendable: Easily integrates with databases, APIs, or WhatsApp for rural reach.

# Required Dependencies

Below are the dependencies listed in `requirements.txt`:

- rasa==3.6.15
- rasa-sdk==3.6.2
- aiohttp
- flask
- requests
- tensorflow~=2.11.0

## 📁 Project Folder Structure

```
FARMERS_SCHEME_CHATBOT/
│
├── actions/
│   ├── __init__.py
│   ├── actions.py
│   └── index.html              # Web interface
│
├── data/
│   ├── nlu.yml                 # Training data for NLU
│   ├── rules.yml               # Rules for conversation
│   └── stories.yml             # Sample stories
│
├── models/                     # Trained Rasa models
├── tests/                      # Test cases (if any)
│
├── config.yml                  # NLU pipeline and policies
├── credentials.yml             # Channel credentials
├── domain.yml                  # Intents, responses, entities, etc.
├── endpoints.yml               # Action endpoint
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```


# Farmers Schemes Chatbot

## Clone the Repository

1. Clone the repository from GitHub:
<pre> <code>git clone https://github.com/Tamil1157/Farmers_scheme_chatbot.git</code> </pre>
2. Navigate into the project directory:
<pre> <code>cd Farmers_scheme_chatbot </code> </pre>



⚙️ Setup Instructions
1. 🌀 Create & Activate a Virtual Environment
<pre> <code>python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate </code> </pre>
2. 📦 Install Dependencies
<pre> <code>pip install -r requirements.txt </code> </pre>
🚀 Running the Chatbot
🖥️ You need to open three terminals:

📌 Terminal 1 - Start Rasa Server
<pre> <code>rasa run --enable-api --cors "*" </code> </pre>
📌 Terminal 2 - Start Action Server
<pre> <code>rasa run actions </code> </pre>
📌 Terminal 3 - Launch Web Interface
<pre> <code>cd actions python -m http.server 8000 </code> </pre>
🔗 Then open your browser and go to:
👉 http://localhost:8000/index.html


Example Queries
1. Sample queries to test the chatbot:
Tamil: "சோலார் டன்னல் ட்ரையர்ஸ் எங்கு பயன்படுத்தலாம் எவை?"
English: "Where can I apply for solar tunnel dryers?"
2. Expected Outputs:
Scheme Details: Displays relevant farmers' schemes based on the query.
Eligibility Check: Shows eligibility criteria for the requested scheme.


## 🧾 Conclusion
🌾 The Farmers Scheme Rasa Chatbot is a user-friendly digital assistant designed to bridge the gap between farmers and vital government scheme information.

🗣️ Supporting both English and Tamil languages, it ensures inclusivity and ease of use for a diverse user base.

🤖 Built on the Rasa framework, the chatbot effectively handles natural language queries and delivers accurate, real-time responses.

🚀 This solution can be easily extended to include more features such as weather updates, crop suggestions, and expert support.

🎯 By empowering farmers with timely and reliable information, this chatbot contributes to better decision-making and improved access to agricultural benefits.
