import streamlit as st
import random

st.set_page_config(page_title="Social Media Chatbot", page_icon="🤖")

# Chatbot data
social_media_info = {
    "instagram": [
        "Instagram is a photo and video sharing social network owned by Meta.",
        "Instagram Reels allow short video sharing, similar to TikTok.",
        "Use hashtags on Instagram to improve your reach."
    ],
    "facebook": [
        "Facebook is one of the oldest and largest platforms, owned by Meta.",
        "You can create pages, groups, and events on Facebook.",
        "Facebook Marketplace is used to buy and sell locally."
    ],
    "tiktok": [
        "TikTok is a short-form video platform popular among Gen Z.",
        "It uses an advanced algorithm for personalized recommendations.",
        "TikTok is known for trends, challenges, and viral content."
    ],
    "twitter": [
        "Twitter, now rebranded as X, is a microblogging platform.",
        "Tweets are short messages limited to 280 characters.",
        "Twitter is used for news, trends, and conversations."
    ],
    "linkedin": [
        "LinkedIn is a professional social network.",
        "It's used for job searching, networking, and industry updates.",
        "You can showcase your resume and career achievements."
    ],
    "youtube": [
        "YouTube is the largest video-sharing platform, owned by Google.",
        "Creators earn revenue via ads, memberships, and super chats.",
        "YouTube Shorts offer short vertical videos like TikTok."
    ]
}

default_responses = [
    "Sorry, I don't have information on that platform. Try Instagram, TikTok, Facebook, etc.",
    "I can only help with popular platforms like YouTube or LinkedIn. Try asking about one of those.",
    "Can you try asking about a specific social media app?"
]

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    for platform in social_media_info:
        if platform in user_input:
            return random.choice(social_media_info[platform])
    return random.choice(default_responses)

# Streamlit app layout
st.title("🤖 Social Media Chatbot")
st.write("Ask me about social media platforms like Instagram, TikTok, Facebook, etc.")

# Session state for chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input from user
user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

# Display chat history
for speaker, msg in st.session_state.chat:
    st.markdown(f"**{speaker}:** {msg}")
