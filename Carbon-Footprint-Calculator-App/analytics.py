import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    layout="wide",
    page_title="Analytics - Carbon Footprint Calculator",
    page_icon="./media/favicon.ico"
)

# Custom CSS
analytics_css = """
<style>
.analytics-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 20px;
    margin: 10px 0;
    color: white;
}

.chart-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin: 10px 0;
}

.metric-card {
    background: linear-gradient(135deg, #4ecdc4, #44a08d);
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin: 10px 0;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}
</style>
"""

st.markdown(analytics_css, unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 25px; margin: 20px 0; color: white;">
    <h1 style="font-size: 3em; margin: 0;">📊 Carbon Analytics</h1>
    <p style="font-size: 1.3em; margin: 10px 0;">Detailed Analysis of Your Carbon Footprint</p>
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
    if st.button("🏆 Dashboard", use_container_width=True):
        st.switch_page("dashboard.py")
with col5:
    if st.button("📈 Analytics", use_container_width=True, type="primary"):
        pass

# Key Metrics
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📈 Key Metrics</h2>
</div>
""", unsafe_allow_html=True)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown("""
    <div class="metric-card">
        <h3 style="margin: 0 0 10px 0;">🌍 Total Emissions</h3>
        <div style="font-size: 2.5em; font-weight: bold;">2,847 kg</div>
        <p style="margin: 5px 0;">CO₂ this month</p>
        <div style="color: #ff6b6b; font-weight: bold;">↓ 12% vs last month</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col2:
    st.markdown("""
    <div class="metric-card">
        <h3 style="margin: 0 0 10px 0;">🎯 Target Progress</h3>
        <div style="font-size: 2.5em; font-weight: bold;">78%</div>
        <p style="margin: 5px 0;">Goal achievement</p>
        <div style="color: #4ecdc4; font-weight: bold;">On track!</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col3:
    st.markdown("""
    <div class="metric-card">
        <h3 style="margin: 0 0 10px 0;">📅 Daily Average</h3>
        <div style="font-size: 2.5em; font-weight: bold;">94.9 kg</div>
        <p style="margin: 5px 0;">CO₂ per day</p>
        <div style="color: #29ad9f; font-weight: bold;">↓ 8% improvement</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col4:
    st.markdown("""
    <div class="metric-card">
        <h3 style="margin: 0 0 10px 0;">🌱 Carbon Offset</h3>
        <div style="font-size: 2.5em; font-weight: bold;">7</div>
        <p style="margin: 5px 0;">Trees planted</p>
        <div style="color: #a8e6cf; font-weight: bold;">This month</div>
    </div>
    """, unsafe_allow_html=True)

# Emission Breakdown Chart
st.markdown("""
<div style="background: linear-gradient(135deg, #4ecdc4, #44a08d); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📊 Emission Breakdown</h2>
</div>
""", unsafe_allow_html=True)

# Create sample data for emission breakdown
categories = ['Transport', 'Energy', 'Waste', 'Food', 'Consumption']
values = [45, 25, 15, 10, 5]
colors = ['#ff6b6b', '#4ecdc4', '#29ad9f', '#a8e6cf', '#ff9a9e']

fig_pie = px.pie(
    values=values,
    names=categories,
    color_discrete_sequence=colors,
    title="Carbon Emissions by Category"
)

fig_pie.update_layout(
    title_x=0.5,
    title_font_size=20,
    height=400
)

st.plotly_chart(fig_pie, use_container_width=True)

# Time Series Analysis
st.markdown("""
<div style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📈 Time Series Analysis</h2>
</div>
""", unsafe_allow_html=True)

# Create sample time series data
dates = pd.date_range(start='2024-01-01', end='2024-03-01', freq='D')
emissions = [random.uniform(80, 120) for _ in range(len(dates))]
moving_avg = pd.Series(emissions).rolling(window=7).mean()

fig_line = go.Figure()

fig_line.add_trace(go.Scatter(
    x=dates,
    y=emissions,
    mode='lines+markers',
    name='Daily Emissions',
    line=dict(color='#ff6b6b', width=2),
    marker=dict(size=4)
))

fig_line.add_trace(go.Scatter(
    x=dates,
    y=moving_avg,
    mode='lines',
    name='7-Day Moving Average',
    line=dict(color='#4ecdc4', width=3)
))

fig_line.update_layout(
    title="Daily Carbon Emissions Over Time",
    xaxis_title="Date",
    yaxis_title="CO₂ Emissions (kg)",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#333'),
    height=400
)

st.plotly_chart(fig_line, use_container_width=True)

# Comparison Charts
st.markdown("""
<div style="background: linear-gradient(135deg, #a8e6cf, #88d8c0); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">📊 Monthly Comparison</h2>
</div>
""", unsafe_allow_html=True)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    # Monthly comparison bar chart
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    current_year = [3200, 2847, 2700, 2600, 2500, 2400]
    previous_year = [3500, 3300, 3200, 3100, 3000, 2900]
    
    fig_bar = go.Figure()
    
    fig_bar.add_trace(go.Bar(
        x=months,
        y=current_year,
        name='2024',
        marker_color='#4ecdc4'
    ))
    
    fig_bar.add_trace(go.Bar(
        x=months,
        y=previous_year,
        name='2023',
        marker_color='#ff6b6b'
    ))
    
    fig_bar.update_layout(
        title="Monthly Emissions Comparison",
        xaxis_title="Month",
        yaxis_title="CO₂ Emissions (kg)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333'),
        height=400
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

with chart_col2:
    # Weekly pattern analysis
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    avg_emissions = [95, 92, 88, 90, 105, 110, 98]
    
    fig_weekly = go.Figure()
    
    fig_weekly.add_trace(go.Bar(
        x=days,
        y=avg_emissions,
        marker_color='#29ad9f'
    ))
    
    fig_weekly.update_layout(
        title="Average Daily Emissions by Day of Week",
        xaxis_title="Day of Week",
        yaxis_title="Average CO₂ Emissions (kg)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333'),
        height=400
    )
    
    st.plotly_chart(fig_weekly, use_container_width=True)

# Insights and Recommendations
st.markdown("""
<div style="background: linear-gradient(135deg, #ff9a9e, #fecfef); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">💡 Insights & Recommendations</h2>
</div>
""", unsafe_allow_html=True)

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.markdown("""
    <div class="chart-card">
        <h3 style="color: #667eea; margin: 0 0 15px 0;">📈 Positive Trends</h3>
        <ul style="color: #666; line-height: 1.8;">
            <li>✅ 12% reduction in monthly emissions</li>
            <li>✅ Consistent improvement over 3 months</li>
            <li>✅ Weekend emissions decreased by 15%</li>
            <li>✅ Transport emissions down by 20%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with insight_col2:
    st.markdown("""
    <div class="chart-card">
        <h3 style="color: #ff6b6b; margin: 0 0 15px 0;">🎯 Areas for Improvement</h3>
        <ul style="color: #666; line-height: 1.8;">
            <li>⚠️ Energy usage peaks on Fridays</li>
            <li>⚠️ Food waste increased by 5%</li>
            <li>⚠️ Weekend consumption still high</li>
            <li>⚠️ Need to optimize heating usage</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Action Items
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 20px; margin: 20px 0; color: white;">
    <h2 style="margin: 0 0 15px 0;">🚀 Recommended Actions</h2>
</div>
""", unsafe_allow_html=True)

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    st.markdown("""
    <div class="chart-card">
        <h3 style="color: #4ecdc4; margin: 0 0 10px 0;">🏠 Home Energy</h3>
        <p style="color: #666; margin: 10px 0;">Install smart thermostats to reduce heating costs by 15%</p>
        <div style="font-size: 2em;">🏠</div>
    </div>
    """, unsafe_allow_html=True)

with action_col2:
    st.markdown("""
    <div class="chart-card">
        <h3 style="color: #ff6b6b; margin: 0 0 10px 0;">🚗 Transportation</h3>
        <p style="color: #666; margin: 10px 0;">Switch to public transport 2 more days per week</p>
        <div style="font-size: 2em;">🚌</div>
    </div>
    """, unsafe_allow_html=True)

with action_col3:
    st.markdown("""
    <div class="chart-card">
        <h3 style="color: #29ad9f; margin: 0 0 10px 0;">♻️ Waste Management</h3>
        <p style="color: #666; margin: 10px 0;">Implement composting to reduce food waste by 30%</p>
        <div style="font-size: 2em;">♻️</div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 15px; margin: 30px 0;">
    <p style="color: white; margin: 0;">📊 Use these insights to make informed decisions about your carbon footprint!</p>
</div>
""", unsafe_allow_html=True)
