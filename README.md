# E-Commerce Chatbot

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
This project is an AI-powered E-Commerce Chatbot designed to assist users in finding products, handling orders, and answering FAQs.<br>
**Link to Demo:** [comming-soon](#) 





![E-Commerce Chatbot](https://i.imgur.com/XEuERhR.jpeg)

---

## Overview
The E-Commerce Chatbot enhances customer shopping experience by providing real-time assistance. Users can inquire about product availability, receive personalized recommendations, track orders, and get support for their shopping needs.

Key Features:

<!-- - Uses mistralai/Mistral-7B-Instruct-v0.3 for generating responses. -->

- AI-powered product search and recommendations.

- Order tracking and customer support.

- Secure and privacy-focused.

- Deployed as a web application for accessibility.
---

## Motivation


With the rise of online shopping, customers often require quick assistance while browsing products or placing orders. This chatbot ensures seamless user engagement by offering instant responses to queries, reducing response time, and improving customer satisfaction.

---

## Technical Aspect

1️⃣ Model & AI Framework

- Llama 2 (Meta-Llama/Llama-2-7b-chat-hf) – Core LLM for medical responses
 - LangChain – Efficient LLM integration and chaining

2️⃣ Retrieval & Storage
- Pinecone – Vector database for storing and retrieving medical knowledge
- FAISS (Alternative) – For local vector search

 3️⃣ Backend & Web Framework
- Flask – Web API for chatbot
- FastAPI (Planned) – High-performance alternative

4️⃣ Frontend
- HTML + CSS + JavaScript – Basic UI
- Streamlit (Planned) – Interactive UI for real-time chat

5️⃣ Deployment
- Render / Hugging Face Spaces / AWS (TBD)



---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 
```
E--Commerce-Chatbot/
├── .github/                   📁 GitHub workflows & configurations  
├── data/                      📁 Dataset storage (user queries, product details, etc.)  
├── experiments/               📁 Model training & experimentation logs  
├── logs/                      📁 Application logs  
├── chatbot/                   📁 Core chatbot logic  
│   ├── __init__.py            📄 Package initialization  
│   ├── chatbot.py             🤖 Chatbot conversation handling  
│   ├── preprocess.py          🔄 Data preprocessing functions  
│   ├── model.py               🧠 AI Model loading & inference  
│   ├── utils.py               🛠️ Utility functions  
├── static/                    📁 Static files (CSS, JS, images)  
├── templates/                 📁 HTML templates for UI  
│   ├── index.html             🖥️ Chatbot UI  
├── venv/                      🐍 Virtual environment  
├── .env                       🌍 Environment variables  
├── .gitignore                 🚫 Files & folders to ignore in Git  
├── LICENSE                    📜 License file  
├── app.py                     🚀 Flask/FastAPI application entry point  
├── README.md                  📖 Project documentation  
├── requirements.txt           📦 Python dependencies  
├── setup.py                   🔧 Installation setup  
└── tests/                     📁 Unit & integration tests  
    ├── test_chatbot.py        ✅ Test cases for chatbot functionality  
    ├── test_api.py            ✅ Test cases for API endpoints  
 

```

## To Do

- xpand medical knowledge base.

- Improve chatbot response accuracy.

- Integrate a symptom checker module.

- Enhance the UI with interactive visualization features.

- Implement multimodal input to analyze medicine images and provide information

- Integrate an audio system for voice-based interactions.


## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- Python 3.10 🐍 – Core programming language
- Flask 🧩 – Web framework for building the chatbot API
- LangChain 🦜🔗 – LLM orchestration and prompt management
- Astra DB 🚀 – Serverless NoSQL database for scalable E-Commerce knowledge retrieval
- Hugging Face 🤗 – Pretrained transformer models for natural language processing
- HTML 🖥️ – Structure for the chatbot's user interface
- CSS 🎨 – Styling for an enhanced user experience
- JavaScript ⚡ – Interactive and dynamic UI functionality






![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/Ggvqguk.png" width=170>](https://python.langchain.com/docs/introduction/) 
[<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
[<img target="_blank" src="https://i.imgur.com/ojLpr2j.jpeg" width=170 height="170">](https://docs.pinecone.io/guides/get-started/overview) 

[<img target="_blank" src="https://logowik.com/content/uploads/images/hugging-face1720994339.logowik.com.webp" width=170 height="170">](https://huggingface.co/docs) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEc9A_S6BPxCDRp5WjMFEfXrpCu1ya2OO-Lw&s" width=170 height="170">](https://developer.mozilla.org/en-US/docs/Web/HTML) 
[<img target="_blank" src="https://cdn-icons-png.flaticon.com/512/919/919826.png" width=170>](https://developer.mozilla.org/en-US/docs/Web/CSS) 



---

## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|

**Bablu Kumar Pandey**

- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
- **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

Special thanks to the contributors of using llms and other open-source projects that made this chatbot possible.