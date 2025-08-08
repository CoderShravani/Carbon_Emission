# 🌱 Eco Dashboard - Carbon Footprint Calculator

## Overview

The Eco Dashboard is a comprehensive user interface that provides detailed tracking and visualization of carbon emission data, user achievements, and environmental impact. It features a modern, visually appealing design with interactive elements and gamification features.

## 🚀 New Features Added

### 1. **User Dashboard** (`dashboard.py`)

A dedicated dashboard page with the following features:

#### 📊 Carbon Stats

- Monthly CO₂ emissions tracking
- Day streak counter
- Badges earned counter
- Goal progress percentage

#### 🔥 Streaks Section

- Walking streak (10k+ steps daily)
- Recycling streak (proper recycling days)
- Energy saving streak (low energy usage days)

#### 🏆 Badges System

- **Earned Badges:**

  - 🌱 Eco Beginner (First 10% reduction)
  - 🚶‍♂️ Walker (7 days of walking)
  - ♻️ Recycler (30 days of recycling)
  - 💡 Energy Saver (20% energy reduction)
  - 🌿 Eco Warrior (25% emission reduction)
  - 🚲 Cyclist (14 days of biking)

- **Locked Badges:**
  - 🌍 Climate Hero (50% emission reduction)
  - 👑 Eco Master (Complete all challenges)

#### 🎮 Active Challenges

- **Zero Waste Week:** Reduce waste by 80% with progress tracking
- **10K Steps Challenge:** Walk 10,000 steps daily for 30 days

#### 📅 Upcoming Events

- 🌍 Earth Day Challenge (April 22, 2024)
- ♻️ Recycling Workshop (March 15, 2024)
- 🚴‍♂️ Bike to Work Day (May 17, 2024)

#### 📈 Carbon Journey Chart

- Interactive time series chart showing daily emissions vs goals
- Visual progress tracking with Plotly charts

#### 🎉 Recent Achievements

- Achievement cards showing recent accomplishments
- Progress milestones and celebrations

### 2. **Analytics Page** (`analytics.py`)

A detailed analytics page with comprehensive data visualization:

#### 📈 Key Metrics

- Total emissions tracking
- Target progress monitoring
- Daily average calculations
- Carbon offset tracking

#### 📊 Emission Breakdown

- Interactive pie chart showing emissions by category:
  - Transport (45%)
  - Energy (25%)
  - Waste (15%)
  - Food (10%)
  - Consumption (5%)

#### 📈 Time Series Analysis

- Daily emissions over time
- 7-day moving average
- Trend analysis and patterns

#### 📊 Monthly Comparison

- Year-over-year comparison charts
- Weekly pattern analysis
- Seasonal trends identification

#### 💡 Insights & Recommendations

- Positive trends identification
- Areas for improvement
- Actionable recommendations

### 3. **Enhanced Navigation**

- Seamless navigation between all pages
- Consistent UI/UX across the application
- Quick access to all features

## 🎨 Design Features

### Visual Appeal

- **Gradient Backgrounds:** Modern gradient designs throughout
- **Card-based Layout:** Clean, organized information display
- **Color-coded Sections:** Different colors for different feature areas
- **Interactive Elements:** Hover effects and smooth transitions
- **Emoji Integration:** Visual icons for better user experience

### Responsive Design

- Mobile-friendly layout
- Adaptive column structures
- Optimized for different screen sizes

## 🛠️ Technical Implementation

### Dependencies Added

- `plotly==5.17.0` - For interactive charts and visualizations

### Files Created/Modified

1. **`dashboard.py`** - Main dashboard page
2. **`analytics.py`** - Analytics and detailed analysis page
3. **`app.py`** - Updated with dashboard tab and navigation
4. **`requirements.txt`** - Added plotly dependency

### Key Features

- **Real-time Data Visualization:** Interactive charts with Plotly
- **Gamification Elements:** Badges, streaks, and challenges
- **Progress Tracking:** Visual progress bars and metrics
- **Event Management:** Upcoming environmental events
- **Achievement System:** Recognition for eco-friendly actions

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the main application:

```bash
streamlit run app.py
```

3. Navigate to the dashboard:
   - Click on the "🏆 Dashboard" tab in the main app
   - Or directly access `dashboard.py` for the full dashboard experience

## 🎯 User Experience

### Gamification Elements

- **Streaks:** Encourage consistent eco-friendly behavior
- **Badges:** Provide recognition for achievements
- **Challenges:** Create engaging weekly/monthly goals
- **Progress Tracking:** Visual feedback on environmental impact

### Educational Features

- **Carbon Education:** Learn about different emission sources
- **Actionable Insights:** Specific recommendations for improvement
- **Event Participation:** Connect with environmental initiatives

### Motivation Features

- **Achievement Celebrations:** Recognize user accomplishments
- **Progress Visualization:** Clear visual feedback on goals
- **Community Events:** Connect with broader environmental movement

## 🌟 Key Benefits

1. **User Engagement:** Gamification keeps users motivated
2. **Data Visualization:** Clear understanding of carbon impact
3. **Goal Setting:** Structured approach to emission reduction
4. **Community Building:** Events and challenges foster connection
5. **Educational Value:** Learn about environmental impact
6. **Actionable Insights:** Specific recommendations for improvement

## 🔮 Future Enhancements

- User authentication and personal data storage
- Social features and leaderboards
- Integration with smart home devices
- Real-time emission tracking
- Community challenges and competitions
- Carbon offset marketplace integration

---

_The Eco Dashboard transforms carbon footprint tracking from a simple calculator into an engaging, educational, and motivating experience that encourages sustainable living._
