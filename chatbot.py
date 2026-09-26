import random

# Chatbot's knowledge base
intents = [
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "good morning"],
        "responses": [
            "Hello! Welcome to our AI chatbot.",
            "Hi there! How can I help you today?"
        ]
    },
    {
        "tag": "cloud",
        "patterns": ["what is cloud computing", "cloud computing"],
        "responses": [
            "Cloud computing means using computing services "
            "like storage, servers, and software over the internet."
        ]
    },
    {
        "tag": "chatbot",
        "patterns": ["what is a chatbot", "how do you work"],
        "responses": [
            "I am a retrieval-based chatbot. I match your "
            "message with predefined patterns and return a response."
        ]
    },
    {
        "tag": "thanks",
        "patterns": ["thank you", "thanks"],
        "responses": [
            "You're welcome!",
            "Happy to help!"
        ]
    },
    {
        "tag": "goodbye",
        "patterns": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! Have a great day."
        ]
    },
    {
        "tag": "cloud_benefits",
        "patterns": [
            "benefits of cloud computing",
            "advantages of cloud",
            "why use cloud computing"
        ],
        "responses": [
            "Cloud computing offers scalability, "
            "cost flexibility, remote access, "
            "and convenient data storage."
        ]
    },
    {
        "tag": "cloud_types",
        "patterns": [
            "types of cloud",
            "public private hybrid cloud",
            "cloud deployment models"
        ],
        "responses": [
            "Common cloud deployment models are "
            "Public Cloud, Private Cloud, and Hybrid Cloud."
        ]
    },
    {
        "tag": "internship_task",
        "patterns": [
            "what is task 4",
            "task 4",
            "internship chatbot"
        ],
        "responses": [
            "Task 4 requires an AI-powered chatbot "
            "using a retrieval-based or generative model, "
            "website integration, and testing for accuracy "
            "and user engagement."
        ]
    },
    {
        "tag": "github",
        "patterns": [
            "github submission",
            "repository name",
            "how to submit project"
        ],
        "responses": [
            "Create a GitHub repository named "
            "CodeAlpha_AI_Chatbot, upload your source code, "
            "and follow your internship's submission instructions."
        ]
    },
]


def get_response(user_message):
    message = user_message.lower().strip()

    if not message:
        return "Please enter a message."

    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in message:
                return random.choice(intent["responses"])

    return (
        "Sorry, I don't know the answer yet. "
        "Please try asking something else."
    )