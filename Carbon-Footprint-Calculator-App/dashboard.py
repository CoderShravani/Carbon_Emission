import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    layout="wide",
    page_title="Eco Dashboard - Carbon Footprint Calculator",
    page_icon="./media/favicon.ico"
)

# Custom CSS for dashboard
dashboard_css = """
<style>
.dashboard-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 20px;
    margin: 10px 0;
    color: white;
}

.stats-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin: 10px 0;
    text-align: center;
}

.badge-card {
    background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
    color: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin: 5px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.challenge-card {
    background: linear-gradient(135deg, #4ecdc4, #44a08d);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.streak-card {
    background: linear-gradient(135deg, #ff9a9e, #fecfef);
    color: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.event-card {
    background: linear-gradient(135deg, #a8e6cf, #88d8c0);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.progress-ring {
    width: 120px;
    height: 120px;
    margin: 0 auto;
}

.achievement-icon {
    font-size: 3em;
    margin: 10px 0;
}

.metric-value {
    font-size: 2.5em;
    font-weight: bold;
    margin: 10px 0;
}

.metric-label {
    font-size: 1.1em;
    opacity: 0.9;
}

.gradient-text {
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: bold;
}
</style>
"""

st.markdown(dashboard_css, unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 25px; margin: 20px 0; color: white;">
    <h1 style="font-size: 3em; margin: 0;">🌱 Eco Dashboard</h1>
    <p style="font-size: 1.3em; margin: 10px 0;">Track Your Carbon Journey & Achievements</p>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col2:
    if st.button("📊 Calculator", use_container_width=True):
        st.switch_page("app.py")
with col3:
    if st.button("🎯 Goals", use_container_width=True):
        st.switch_page("app.py")
with col4:
    if st.button("🏆 Dashboard", use_container_width=True, type="primary"):
        pass
with col5:
    if st.button("📈 Analytics", use_container_width=True):
        st.switch_page("analytics.py")

# User Stats Section
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📈 Your Carbon Stats</h2>
</div>
""", unsafe_allow_html=True)

# Stats Cards
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown("""
    <div class="stats-card">
        <div class="achievement-icon">🌍</div>
        <div class="metric-value">2,847</div>
        <div class="metric-label">Monthly CO₂ (kg)</div>
        <div style="color: #ff6b6b; font-weight: bold;">↓ 12% vs last month</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
    <div class="stats-card">
        <div class="achievement-icon">🔥</div>
        <div class="metric-value">14</div>
        <div class="metric-label">Day Streak</div>
        <div style="color: #4ecdc4; font-weight: bold;">Personal Best!</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
    <div class="stats-card">
        <div class="achievement-icon">🏆</div>
        <div class="metric-value">8</div>
        <div class="metric-label">Badges Earned</div>
        <div style="color: #ff8e8e; font-weight: bold;">3 new this week</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
    <div class="stats-card">
        <div class="achievement-icon">🎯</div>
        <div class="metric-value">78%</div>
        <div class="metric-label">Goal Progress</div>
        <div style="color: #29ad9f; font-weight: bold;">On track!</div>
    </div>
    """, unsafe_allow_html=True)

# Streaks Section
st.markdown("""
<div style="background: linear-gradient(135deg, #ff9a9e, #fecfef); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">🔥 Your Streaks</h2>
</div>
""", unsafe_allow_html=True)

streak_col1, streak_col2, streak_col3 = st.columns(3)

with streak_col1:
    st.markdown("""
    <div class="streak-card">
        <h3 style="margin: 0 0 10px 0;">🚶‍♂️ Walking</h3>
        <div class="metric-value">14</div>
        <p style="margin: 5px 0;">Days of 10k+ steps</p>
        <div style="font-size: 2em;">👟</div>
    </div>
    """, unsafe_allow_html=True)

with streak_col2:
    st.markdown("""
    <div class="streak-card">
        <h3 style="margin: 0 0 10px 0;">♻️ Recycling</h3>
        <div class="metric-value">21</div>
        <p style="margin: 5px 0;">Days of proper recycling</p>
        <div style="font-size: 2em;">♻️</div>
    </div>
    """, unsafe_allow_html=True)

with streak_col3:
    st.markdown("""
    <div class="streak-card">
        <h3 style="margin: 0 0 10px 0;">💡 Energy Saving</h3>
        <div class="metric-value">7</div>
        <p style="margin: 5px 0;">Days of low energy usage</p>
        <div style="font-size: 2em;">💡</div>
    </div>
    """, unsafe_allow_html=True)

# Badges Section
st.markdown("""
<div style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">🏆 Your Badges</h2>
</div>
""", unsafe_allow_html=True)

# Create badge grid
badge_col1, badge_col2, badge_col3, badge_col4 = st.columns(4)

badges = [
    {"name": "🌱 Eco Beginner", "description": "First 10% reduction", "earned": True},
    {"name": "🚶‍♂️ Walker", "description": "7 days of walking", "earned": True},
    {"name": "♻️ Recycler", "description": "Recycle for 30 days", "earned": True},
    {"name": "💡 Energy Saver", "description": "Reduce energy by 20%", "earned": True},
    {"name": "🌿 Eco Warrior", "description": "25% emission reduction", "earned": True},
    {"name": "🚲 Cyclist", "description": "Use bike for 14 days", "earned": True},
    {"name": "🌍 Climate Hero", "description": "50% emission reduction", "earned": False},
    {"name": "👑 Eco Master", "description": "Complete all challenges", "earned": False},
]

for i, badge in enumerate(badges):
    col = [badge_col1, badge_col2, badge_col3, badge_col4][i % 4]
    with col:
        opacity = "1" if badge["earned"] else "0.3"
        st.markdown(f"""
        <div class="badge-card" style="opacity: {opacity};">
            <div style="font-size: 2em; margin: 10px 0;">{badge['name'].split()[0]}</div>
            <h4 style="margin: 5px 0;">{badge['name'].split(' ', 1)[1]}</h4>
            <p style="font-size: 0.9em; margin: 5px 0;">{badge['description']}</p>
            <div style="font-size: 1.5em;">{'🏆' if badge['earned'] else '🔒'}</div>
        </div>
        """, unsafe_allow_html=True)

# Challenges Section
st.markdown("""
<div style="background: linear-gradient(135deg, #4ecdc4, #44a08d); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">🎮 Active Challenges</h2>
</div>
""", unsafe_allow_html=True)

challenge_col1, challenge_col2 = st.columns(2)

with challenge_col1:
    st.markdown("""
    <div class="challenge-card">
        <h3 style="margin: 0 0 15px 0;">🌱 Zero Waste Week</h3>
        <p style="margin: 10px 0;">Reduce your waste by 80% this week</p>
        <div style="background: rgba(255,255,255,0.3); border-radius: 10px; padding: 10px; margin: 10px 0;">
            <div style="display: flex; justify-content: space-between; margin: 5px 0;">
                <span>Progress</span>
                <span>65%</span>
            </div>
            <div style="background: rgba(255,255,255,0.5); height: 8px; border-radius: 4px;">
                <div style="background: white; height: 100%; width: 65%; border-radius: 4px;"></div>
            </div>
        </div>
        <div style="font-size: 2em;">🗑️</div>
    </div>
    """, unsafe_allow_html=True)

with challenge_col2:
    st.markdown("""
    <div class="challenge-card">
        <h3 style="margin: 0 0 15px 0;">🚶‍♂️ 10K Steps Challenge</h3>
        <p style="margin: 10px 0;">Walk 10,000 steps every day for 30 days</p>
        <div style="background: rgba(255,255,255,0.3); border-radius: 10px; padding: 10px; margin: 10px 0;">
            <div style="display: flex; justify-content: space-between; margin: 5px 0;">
                <span>Progress</span>
                <span>14/30 days</span>
            </div>
            <div style="background: rgba(255,255,255,0.5); height: 8px; border-radius: 4px;">
                <div style="background: white; height: 100%; width: 47%; border-radius: 4px;"></div>
            </div>
        </div>
        <div style="font-size: 2em;">👟</div>
    </div>
    """, unsafe_allow_html=True)

# Events Section
st.markdown("""
<div style="background: linear-gradient(135deg, #a8e6cf, #88d8c0); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📅 Upcoming Events</h2>
</div>
""", unsafe_allow_html=True)

event_col1, event_col2, event_col3 = st.columns(3)

with event_col1:
    st.markdown("""
    <div class="event-card">
        <h3 style="margin: 0 0 10px 0;">🌍 Earth Day Challenge</h3>
        <p style="margin: 5px 0; font-size: 0.9em;">April 22, 2024</p>
        <p style="margin: 10px 0;">Join the global movement to protect our planet</p>
        <div style="font-size: 2em;">🌍</div>
        <button style="background: white; color: #a8e6cf; border: none; padding: 8px 16px; border-radius: 20px; margin-top: 10px; font-weight: bold;">Join Event</button>
    </div>
    """, unsafe_allow_html=True)

with event_col2:
    st.markdown("""
    <div class="event-card">
        <h3 style="margin: 0 0 10px 0;">♻️ Recycling Workshop</h3>
        <p style="margin: 5px 0; font-size: 0.9em;">March 15, 2024</p>
        <p style="margin: 10px 0;">Learn advanced recycling techniques</p>
        <div style="font-size: 2em;">♻️</div>
        <button style="background: white; color: #a8e6cf; border: none; padding: 8px 16px; border-radius: 20px; margin-top: 10px; font-weight: bold;">Register</button>
    </div>
    """, unsafe_allow_html=True)

with event_col3:
    st.markdown("""
    <div class="event-card">
        <h3 style="margin: 0 0 10px 0;">🚴‍♂️ Bike to Work Day</h3>
        <p style="margin: 5px 0; font-size: 0.9em;">May 17, 2024</p>
        <p style="margin: 10px 0;">Reduce emissions by cycling to work</p>
        <div style="font-size: 2em;">🚴‍♂️</div>
        <button style="background: white; color: #a8e6cf; border: none; padding: 8px 16px; border-radius: 20px; margin-top: 10px; font-weight: bold;">Participate</button>
    </div>
    """, unsafe_allow_html=True)

# Carbon Emission Chart
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📊 Your Carbon Journey</h2>
</div>
""", unsafe_allow_html=True)

# Create sample data for the chart
dates = pd.date_range(start='2024-01-01', end='2024-03-01', freq='D')
emissions = [random.uniform(80, 120) for _ in range(len(dates))]
goals = [100] * len(dates)

# Create the chart
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=dates,
    y=emissions,
    mode='lines+markers',
    name='Daily Emissions',
    line=dict(color='#ff6b6b', width=3),
    marker=dict(size=6)
))

fig.add_trace(go.Scatter(
    x=dates,
    y=goals,
    mode='lines',
    name='Goal (100 kg CO₂)',
    line=dict(color='#4ecdc4', width=2, dash='dash')
))

fig.update_layout(
    title="Daily Carbon Emissions vs Goal",
    xaxis_title="Date",
    yaxis_title="CO₂ Emissions (kg)",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#333'),
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Achievement Summary
st.markdown("""
<div style="background: linear-gradient(135deg, #ff9a9e, #fecfef); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">🎉 Recent Achievements</h2>
</div>
""", unsafe_allow_html=True)

achievement_col1, achievement_col2, achievement_col3 = st.columns(3)

with achievement_col1:
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
        <div style="font-size: 3em;">🏆</div>
        <h3 style="color: #ff6b6b; margin: 10px 0;">Eco Warrior Badge</h3>
        <p style="color: #666; margin: 5px 0;">Achieved 25% emission reduction</p>
        <p style="color: #999; font-size: 0.9em;">Earned 2 days ago</p>
    </div>
    """, unsafe_allow_html=True)

with achievement_col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
        <div style="font-size: 3em;">🔥</div>
        <h3 style="color: #4ecdc4; margin: 10px 0;">14-Day Streak</h3>
        <p style="color: #666; margin: 5px 0;">Consistent eco-friendly choices</p>
        <p style="color: #999; font-size: 0.9em;">Current streak</p>
    </div>
    """, unsafe_allow_html=True)

with achievement_col3:
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
        <div style="font-size: 3em;">🌱</div>
        <h3 style="color: #29ad9f; margin: 10px 0;">Zero Waste Week</h3>
        <p style="color: #666; margin: 5px 0;">Reduced waste by 80%</p>
        <p style="color: #999; font-size: 0.9em;">Completed yesterday</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 15px; margin: 30px 0;">
    <p style="color: white; margin: 0;">🌱 Keep up the great work! Every small action counts towards a greener future.</p>
</div>
""", unsafe_allow_html=True)
