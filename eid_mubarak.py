import streamlit as st
import random
import time
from datetime import datetime, date
import base64
from PIL import Image
import io
import pytz
import requests
from io import BytesIO
import numpy as np
import math

# Page configuration
st.set_page_config(
    page_title="✨ Eid ul Adha Mubarak ✨",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium animations and styling
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Dancing+Script:wght@700&display=swap');
    
    body {
        overflow-x: hidden;
    }
    
    .main {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    }

    .stApp {
        background: radial-gradient(ellipse at center, #fdfcfb 0%, #e2d1c3 100%);
    }
    
    .floating-element {
        animation: float 6s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(2deg); }
        50% { transform: translateY(0) rotate(0deg); }
        75% { transform: translateY(10px) rotate(-2deg); }
        100% { transform: translateY(0) rotate(0deg); }
    }
    
    .premium-container {
        border: 1px solid rgba(255, 215, 0, 0.3);
        background-color: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05), 0 1px 8px rgba(0,0,0,0.05), 0 0 1px rgba(0,0,0,0.05);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        transition: all 0.5s ease;
    }
    
    .premium-container:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.05);
    }

    .reflection {
        position: relative;
        overflow: hidden;
    }
    
    .reflection::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            to right,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.3) 100%
        );
        transform: skewX(-25deg);
        animation: reflection 6s infinite;
    }
    
    @keyframes reflection {
        0% { left: -100%; }
        20%, 100% { left: 100%; }
    }
    
    .shimmer-text {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 4rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .elegant-wish {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        color: #d4af37;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        margin: 30px 0;
    }
    
    .countdown {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        margin: 30px 0;
        color: #333;
    }
    
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    
    .countdown-box {
        background: linear-gradient(145deg, #f5f5f5, #ffffff);
        box-shadow: 8px 8px 16px #d9d9d9, -8px -8px 16px #ffffff;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        min-width: 100px;
        text-align: center;
    }
    
    .countdown-value {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 5px;
        background: linear-gradient(to right, #d4af37, #f9f295);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .countdown-label {
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #666;
    }
    
    .premium-button {
        background: linear-gradient(to right, #d4af37, #f9f295);
        color: #fff;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        border-radius: 50px;
        padding: 12px 30px;
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
        transition: all 0.3s ease;
    }
    
    .premium-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4);
    }
    
    .gold-border {
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 30px;
        position: relative;
    }
    
    .gold-border::before {
        content: "";
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        border-radius: 20px;
        background: linear-gradient(45deg, #d4af37, #f9f295, #d4af37, #f9f295);
        background-size: 400% 400%;
        z-index: -1;
        animation: border-shift 5s linear infinite;
    }
    
    @keyframes border-shift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    .message-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        font-family: 'Montserrat', sans-serif;
        position: relative;
        overflow: hidden;
    }
    
    .message-card::before {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(212, 175, 55, 0.3) 0%, rgba(255, 255, 255, 0) 70%);
        top: -100px;
        left: -100px;
    }
    
    .message-card::after {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(212, 175, 55, 0.2) 0%, rgba(255, 255, 255, 0) 70%);
        bottom: -100px;
        right: -100px;
    }
    
    .rose-gold-text {
        background: linear-gradient(to right, #ec6f66, #f3a183);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    .photo-frame {
        border: 10px solid white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transform: rotate(2deg);
        transition: all 0.5s ease;
    }
    
    .photo-frame:hover {
        transform: rotate(0deg) scale(1.05);
    }
    
    .shake-animation {
        animation: shake 5s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        5%, 15% { transform: rotate(-5deg); }
        10%, 20% { transform: rotate(5deg); }
        25% { transform: rotate(0deg); }
    }
    
    .memory-polaroid {
        background: white;
        padding: 15px 15px 60px 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: rotate(random() * 10 - 5 + deg);
        transition: all 0.3s ease;
        position: relative;
        margin: 20px;
    }
    
    .memory-polaroid:hover {
        transform: scale(1.05) rotate(0deg);
        z-index: 10;
    }
    
    .memory-polaroid::after {
        content: "Memories";
        position: absolute;
        bottom: 20px;
        left: 0;
        right: 0;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 1.5rem;
        color: #333;
    }
    
    .sparkle {
        position: absolute;
        width: 20px;
        height: 20px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E%3Cpath d='M10 0L12 7H19L13 12L15 20L10 15L5 20L7 12L1 7H8L10 0Z' fill='%23FFD700'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
        opacity: 0;
    }
    
    @keyframes sparkle-fade {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1); opacity: 1; }
        100% { transform: scale(0); opacity: 0; }
    }
    
    .cake-animation {
        animation: cake-float 3s ease-in-out infinite, cake-glow 2s ease-in-out infinite;
    }
    
    @keyframes cake-float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes cake-glow {
        0%, 100% { filter: drop-shadow(0 0 8px rgba(255, 215, 0, 0.7)); }
        50% { filter: drop-shadow(0 0 15px rgba(255, 215, 0, 1)); }
    }
    
    </style>
    """, unsafe_allow_html=True)

# Function to auto-play audio from URL
def autoplay_audio_url(url):
    try:
        response = requests.get(url)
        audio_bytes = response.content
        b64 = base64.b64encode(audio_bytes).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except Exception:
        st.error("Could not load background music. Please ensure you have an internet connection.")

# Function to generate premium confetti
def generate_confetti():
    confetti_html = ""
    colors = ["#FFD700", "#d4af37", "#FFC0CB", "#FF69B4", "#C9A9A6"]
    
    for i in range(50):
        size = random.randint(5, 15)
        delay = random.uniform(0, 5)
        duration = random.uniform(3, 8)
        color = random.choice(colors)
        left_pos = random.randint(0, 100)
        opacity = random.uniform(0.6, 1)
        
        confetti_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: -5%; 
            width: {size}px; 
            height: {size * 1.5}px; 
            background-color: {color}; 
            opacity: {opacity};
            animation: confetti-fall {duration}s {delay}s ease-in-out infinite;
            z-index: -1;
            transform: rotate({random.randint(0, 360)}deg);
        "></div>
        """
    
    st.markdown(confetti_html, unsafe_allow_html=True)

# Function to generate sparkles
def generate_sparkles():
    sparkle_html = ""
    
    for i in range(30):
        size = random.randint(10, 20)
        delay = random.uniform(0, 15)
        duration = random.uniform(2, 4)
        left_pos = random.randint(0, 100)
        top_pos = random.randint(0, 100)
        
        sparkle_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: {top_pos}%; 
            width: {size}px; 
            height: {size}px;
            background-image: url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22%3E%3Cpath fill=%22%23FFD700%22 d=%22M12,1L9,9L1,12L9,15L12,23L15,15L23,12L15,9Z%22/%3E%3C/svg%3E');
            background-size: cover;
            animation: sparkle-fade {duration}s {delay}s ease-in-out infinite;
            z-index: 1;
        "></div>
        """
    
    st.markdown(sparkle_html, unsafe_allow_html=True)

# Premium Eid wishes templates
def get_premium_eid_wishes():
    return [
        "May Allah's blessings be with you today and always. Eid ul Adha Mubarak!",
        "On this blessed occasion of Eid ul Adha, may Allah accept your sacrifices and grant you peace and prosperity.",
        "May the divine blessings of Allah bring you hope, faith, and joy on Eid ul Adha and forever.",
        "As you celebrate Eid ul Adha, may Allah's blessings be showered upon you and your family.",
        "Wishing you a blessed Eid ul Adha filled with peace, joy, and happiness.",
        "May this Eid bring joy, happiness, and wealth to your life. Eid ul Adha Mubarak!",
        "On this special day, may Allah's blessings be with you and your family. Eid ul Adha Mubarak!",
        "May Allah's blessings be with you today and always. Eid ul Adha Mubarak!"
    ]

# Function to create fancy text with sparkle animation
def fancy_header(text, element_class="shimmer-text", tag="h1"):
    return f'<{tag} class="{element_class}">{text}</{tag}>'

# Personal memories and quotes for Eid
def get_personal_memories():
    return [
        "The beautiful moments of prayer and togetherness",
        "The joy of sharing meals with family and friends",
        "The spirit of giving and sacrifice",
        "The warmth of family gatherings",
        "The blessings of Allah's mercy",
        "The peace that comes with faith",
        "The happiness of celebrating with loved ones",
        "The memories of past Eid celebrations"
    ]

# Check if today is Eid
def is_eid():
    # Use a specific timezone (e.g., Asia/Karachii for Pakistan Standard Time)
    timezone = pytz.timezone('Asia/Karachi')
    today = datetime.now(timezone).date()
    return today.month == 6 and today.day == 7

# Calculate time until Eid
def time_until_eid():
    timezone = pytz.timezone('Asia/Karachi')
    now = datetime.now(timezone)
    current_year = now.year
    
    # Create Eid datetime object for this year
    eid_date = datetime(current_year, 6, 7, 0, 0, 0, tzinfo=timezone)
    
    # If Eid has already passed this year, look for next year
    if now > eid_date:
        eid_date = datetime(current_year + 1, 6, 7, 0, 0, 0, tzinfo=timezone)
    
    # Calculate time remaining
    delta = eid_date - now
    
    # Extract days, hours, minutes and seconds
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Display premium countdown
def show_premium_countdown():
    days, hours, minutes, seconds = time_until_eid()
    
    if days > 0 or hours > 0 or minutes > 0 or seconds > 0:
        st.markdown("""
        <div class="premium-container reflection">
            <h2 style="text-align: center; font-family: 'Playfair Display', serif; margin-bottom: 30px;">
                Eid ul Adha Celebration
            </h2>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="countdown">
            <div class="countdown-container">
                <div class="countdown-box">
                    <div class="countdown-value">{days}</div>
                    <div class="countdown-label">Days</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{hours}</div>
                    <div class="countdown-label">Hours</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{minutes}</div>
                    <div class="countdown-label">Minutes</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{seconds}</div>
                    <div class="countdown-label">Seconds</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style="text-align: center; font-family: 'Montserrat', sans-serif; font-size: 1.2rem; margin: 30px 0;">
            A blessed celebration is approaching.
        </p>
        
        <div style="text-align: center; margin: 40px 0;">
            <img src="https://media.giphy.com/media/3o7TKz2eMXx7dn95FS/giphy.gif" width="300" style="border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
        </div>
        
        <p style="text-align: center; font-family: 'Dancing Script', cursive; font-size: 2rem; color: #d4af37; margin-top: 20px;">
            Coming Soon...
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        return False
    else:
        return True

# Create floating images with parallax effect
def create_floating_image(image_url, size=200, rotation=5, delay=0):
    return f"""
    <img src="{image_url}" width="{size}" style="
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: rotate({rotation}deg);
        animation: float 6s {delay}s ease-in-out infinite;
    ">
    """

# Main function
def main():
    # Add timezone information to the app
    # st.sidebar.markdown("### Celebration Details")
    # st.sidebar.markdown("**Timezone:** Asia/Karachi (Pakistan Standard Time)")
    # st.sidebar.markdown("**Current Date in Selected Timezone:**")
    # timezone = pytz.timezone('Asia/Karachi')
    # current_time = datetime.now(timezone)
    # st.sidebar.markdown(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    local_css()
    generate_confetti()
    generate_sparkles()
    
    # Play background music (a peaceful Eid nasheed)
    try:
        # Using a publicly available audio URL - replace with your preferred nasheed
        audio_url = "https://github.com/AkashGutha/birthday-greetings/raw/master/song.mp3"
        autoplay_audio_url(audio_url)
    except:
        pass  # Silently fail if audio can't be loaded
    
    # Check if today is Eid
    show_full_content = is_eid()
    
    # If it's not Eid, show countdown instead
    if not show_full_content:
        access_granted = show_premium_countdown()
        
        # Add a backdoor for testing (remove in production)
        if st.sidebar.checkbox("Preview Eid Content", value=False):
            access_granted = True
            st.sidebar.warning("Preview mode enabled")
        
        if not access_granted:
            # Add footer
            st.markdown("""
            <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
                <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666;">
                    Crafted with ❤️ for Eid ul Adha | 2025
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
    
    # Full Eid content
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Header
        st.markdown(f"""
        <div class="premium-container reflection" style="text-align: center;">
            {fancy_header("Eid ul Adha Mubarak", "shimmer-text")}
            <p class="elegant-wish">Blessed Celebration</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Premium Eid layout
    st.markdown("""
    <div class="premium-container gold-border">
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div class="shake-animation" style="margin-bottom: 30px;">
                <span style="font-size: 80px;">🕌✨🌙</span>
            </div>
    """, unsafe_allow_html=True)
    
    # Display premium personalized message
    eid_message = random.choice(get_premium_eid_wishes())
    
    st.markdown(f"""
        <div class="message-card">
            <h2 style="font-family: 'Montserrat', sans-serif; font-weight: 600; margin-bottom: 20px; color: #333;">
                Dear Friends and Family,
            </h2>
            <p style="font-family: 'Playfair Display', serif; font-size: 1.3rem; line-height: 1.8; color: #444; margin-bottom: 20px;">
                {eid_message}
            </p>
            <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666; margin-top: 30px;">
                On this blessed occasion of Eid ul Adha, may Allah's blessings be with you and your family. May this special day bring peace, joy, and happiness to your life.
            </p>
            <p class="rose-gold-text" style="text-align: right; font-size: 1.5rem; margin-top: 30px;">
                Eid Mubarak!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday memories and quotes
    st.markdown("""
        <h3 style="font-family: 'Playfair Display', serif; text-align: center; margin: 40px 0 20px; color: #333;">
            ✨ Celebrating What Makes You Special ✨
        </h3>
    """, unsafe_allow_html=True)
    
    # Special memories and quotes in 4 columns
    memories = get_personal_memories()
    
    # Create 4 columns for memories
    col1, col2, col3, col4 = st.columns(4)
    memory_cols = [col1, col2, col3, col4]
    
    # Distribute memories across columns
    for i, memory in enumerate(memories):
        col_index = i % 4  # Determine which column to place the memory
        with memory_cols[col_index]:
            st.markdown(f"""
                <div style="
                    background: linear-gradient(145deg, #ffffff, #f5f5f5);
                    border-radius: 20px;
                    padding: 20px;
                    box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
                    transform: rotate({random.uniform(-2, 2)}deg);
                    margin: 10px 5px;
                    min-height: 150px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    <p style="font-family: 'Montserrat', sans-serif; font-size: 1rem; color: #555; text-align: center;">
                        "{memory}"
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Interactive "gift" - digital birthday cake
    st.markdown("""
        <h3 style="font-family: 'Playfair Display', serif; text-align: center; margin: 40px 0 20px; color: #333;">
            Eid Blessings
        </h3>
        
        <div style="text-align: center; margin: 40px 0;">
            <div class="cake-animation" style="font-size: 120px; margin: 20px 0 40px 0; display: inline-block;">
                🕌✨🌙
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Make a wish section
    st.markdown("""
        <div class="premium-container" style="text-align: center; max-width: 600px; margin: 30px auto;">
            <h3 style="font-family: 'Dancing Script', cursive; font-size: 2.5rem; color: #d4af37; margin-bottom: 20px;">
                Send Blessings
            </h3>
            <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666; margin-bottom: 30px;">
                Share your prayers and blessings for this blessed occasion!
            </p>
    """, unsafe_allow_html=True)
    
    # Blessings button with animation - centered using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Share Blessings ✨", key="blessings_button", use_container_width=True):
            st.balloons()
            st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <h3 style="font-family: 'Dancing Script', cursive; font-size: 2rem; color: #d4af37;">
                    May Allah accept your prayers!
                </h3>
                <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666;">
                    May Allah's blessings be with you and your loved ones.
                </p>
                <div style="font-size: 50px; margin: 20px 0;">
                    ✨🕌🌙
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday quotes carousel
    st.markdown("""
        <div style="text-align: center; margin: 40px 0;">
            <h3 style="font-family: 'Playfair Display', serif; color: #333; margin-bottom: 20px;">
                Eid ul Adha Blessings
            </h3>
            <div class="premium-container" style="background: linear-gradient(to right, rgba(212, 175, 55, 0.1), rgba(249, 242, 149, 0.1)); text-align: center; padding: 30px;">
                <p style="font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: #333;">
                    "May Allah's blessings be with you today and always. May this Eid bring joy, peace, and prosperity to your life."
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Final Eid wish
    st.markdown("""
   <style>
                 <div class="premium-container" style="text-align: center; margin: 50px 0;">
        <img src="https://media.giphy.com/media/3o7TKz2eMXx7dn95FS/giphy.gif" width="300" 
             style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin-bottom: 30px;">
        
        <h2 style="font-family: 'Dancing Script', cursive; font-size: 3rem; color: #d4af37; margin: 20px 0;">
            Eid ul Adha Mubarak!
        </h2>
        
        <p style="font-family: 'Montserrat', sans-serif; font-size: 1.2rem; color: #666; margin-bottom: 40px;">
            May Allah's blessings be with you today and always!
        </p>
    </div>
                </style>
""", unsafe_allow_html=True)
    
    # End the container
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
        <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666;">
            Crafted with ❤️ for Eid ul Adha | 2025
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()