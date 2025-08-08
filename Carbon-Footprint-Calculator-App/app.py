import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import base64
from functions import *

st.set_page_config(layout="wide",page_title="Carbon Footprint Calculator", page_icon="./media/favicon.ico")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background = get_base64("./media/background_min.jpg")
icon2 = get_base64("./media/icon2.png")
icon3 = get_base64("./media/icon3.png")

with open("./style/style.css", "r") as style:
    css=f"""<style>{style.read().format(background=background, icon2=icon2, icon3=icon3)}</style>"""
    st.markdown(css, unsafe_allow_html=True)

def script():
    with open("./style/scripts.js", "r", encoding="utf-8") as scripts:
        open_script = f"""<script>{scripts.read()}</script> """
        html(open_script, width=0, height=0)


left, middle, right = st.columns([2,3.5,2])
main, comps, result, goals, dashboard = middle.tabs([" ", " ", " ", "🎯 Goals & Progress", "🏆 Dashboard"])

with open("./style/main.md", "r", encoding="utf-8") as main_page:
    main.markdown(f"""{main_page.read()}""")

_,but,_ = main.columns([1,2,1])
if but.button("Calculate Your Carbon Footprint!", type="primary"):
    click_element('tab-1')

tab1, tab2, tab3, tab4, tab5 = comps.tabs(["👴 Personal","🚗 Travel","🗑️ Waste","⚡ Energy","💸 Consumption"])
tab_result,_ = result.tabs([" "," "])

def component():
    tab1col1, tab1col2 = tab1.columns(2)
    height = tab1col1.number_input("Height",0,251, value=None, placeholder="160", help="in cm")
    weight = tab1col2.number_input("Weight", 0, 250, value=None, placeholder="75", help="in kg")
    if (weight is None) or (weight == 0) : weight = 1
    if (height is None) or (height == 0) : height = 1
    calculation = weight / (height/100)**2
    body_type = "underweight" if (calculation < 18.5) else \
                 "normal" if ((calculation >=18.5) and (calculation < 25 )) else \
                 "overweight" if ((calculation >= 25) and (calculation < 30)) else "obese"
    sex = tab1.selectbox('Gender', ["female", "male"])
    diet = tab1.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'], help="""
                                                                                              Omnivore: Eats both plants and animals.\n
                                                                                              Pescatarian: Consumes plants and seafood, but no other meat\n
                                                                                              Vegetarian: Diet excludes meat but includes plant-based foods.\n
                                                                                              Vegan: Avoids all animal products, including meat, dairy, and eggs.""")
    social = tab1.selectbox('Social Activity', ['never', 'often', 'sometimes'], help="How often do you go out?")

    transport = tab2.selectbox('Transportation', ['public', 'private', 'walk/bicycle'],
                               help="Which transportation method do you prefer the most?")
    if transport == "private":
        vehicle_type = tab2.selectbox('Vehicle Type', ['petrol', 'diesel', 'hybrid', 'lpg', 'electric'],
                                      help="What type of fuel do you use in your car?")
    else:
        vehicle_type = "None"

    if transport == "walk/bicycle":
        vehicle_km = 0
    else:
        vehicle_km = tab2.slider('What is the monthly distance traveled by the vehicle in kilometers?', 0, 5000, 0, disabled=False)

    air_travel = tab2.selectbox('How often did you fly last month?', ['never', 'rarely', 'frequently', 'very frequently'], help= """
                                                                                                                             Never: I didn't travel by plane.\n
                                                                                                                             Rarely: Around 1-4 Hours.\n
                                                                                                                             Frequently: Around 5 - 10 Hours.\n
                                                                                                                             Very Frequently: Around 10+ Hours. """)

    waste_bag = tab3.selectbox('What is the size of your waste bag?', ['small', 'medium', 'large', 'extra large'])
    waste_count = tab3.slider('How many waste bags do you trash out in a week?', 0, 10, 0)
    recycle = tab3.multiselect('Do you recycle any materials below?', ['Plastic', 'Paper', 'Metal', 'Glass'])

    heating_energy = tab4.selectbox('What power source do you use for heating?', ['natural gas', 'electricity', 'wood', 'coal'])

    for_cooking = tab4.multiselect('What cooking systems do you use?', ['microwave', 'oven', 'grill', 'airfryer', 'stove'])
    energy_efficiency = tab4.selectbox('Do you consider the energy efficiency of electronic devices?', ['No', 'Yes', 'Sometimes' ])
    daily_tv_pc = tab4.slider('How many hours a day do you spend in front of your PC/TV?', 0, 24, 0)
    internet_daily = tab4.slider('What is your daily internet usage in hours?', 0, 24, 0)

    shower = tab5.selectbox('How often do you take a shower?', ['daily', 'twice a day', 'more frequently', 'less frequently'])
    grocery_bill = tab5.slider('Monthly grocery spending in $', 0, 500, 0)
    clothes_monthly = tab5.slider('How many clothes do you buy monthly?', 0, 30, 0)

    data = {'Body Type': body_type,
            "Sex": sex,
            'Diet': diet,
            "How Often Shower": shower,
            "Heating Energy Source": heating_energy,
            "Transport": transport,
            "Social Activity": social,
            'Monthly Grocery Bill': grocery_bill,
            "Frequency of Traveling by Air": air_travel,
            "Vehicle Monthly Distance Km": vehicle_km,
            "Waste Bag Size": waste_bag,
            "Waste Bag Weekly Count": waste_count,
            "How Long TV PC Daily Hour": daily_tv_pc,
            "Vehicle Type": vehicle_type,
            "How Many New Clothes Monthly": clothes_monthly,
            "How Long Internet Daily Hour": internet_daily,
            "Energy efficiency": energy_efficiency
            }
    data.update({f"Cooking_with_{x}": y for x, y in
                 dict(zip(for_cooking, np.ones(len(for_cooking)))).items()})
    data.update({f"Do You Recyle_{x}": y for x, y in
                 dict(zip(recycle, np.ones(len(recycle)))).items()})


    return pd.DataFrame(data, index=[0])

df = component()
data = input_preprocessing(df)

sample_df = pd.DataFrame(data=sample,index=[0])
sample_df[sample_df.columns] = 0
sample_df[data.columns] = data

ss = pickle.load(open("./models/scale.sav","rb"))
model = pickle.load(open("./models/model.sav","rb"))
prediction = round(np.exp(model.predict(ss.transform(sample_df))[0]))

column1,column2 = tab1.columns(2)
_,resultbutton,_ = tab5.columns([1,1,1])
if resultbutton.button(" ", type = "secondary"):
    tab_result.image(chart(model,ss, sample_df,prediction), use_column_width="auto")
    click_element('tab-2')

pop_button = """<button id = "button-17" class="button-17" role="button"> ❔ Did You Know</button>"""
_,home,_ = comps.columns([1,2,1])
_,col2,_ = comps.columns([1,10,1])
col2.markdown(pop_button, unsafe_allow_html=True)
pop = """
<div id="popup" class="DidYouKnow_root">
<p class="DidYouKnow_title TextNew" style="font-size: 20px;"> ❔ Did you know</p>
    <p id="popupText" class="DidYouKnow_content TextNew"><span>
    Each year, human activities release over 40 billion metric tons of carbon dioxide into the atmosphere, contributing to climate change.
    </span></p>
</div>
"""
col2.markdown(pop, unsafe_allow_html=True)

if home.button("🏡"):
    click_element('tab-0')
_,resultmid,_ = result.columns([1,2,1])

tree_count = round(prediction / 411.4)
tab_result.markdown(f"""You owe nature <b>{tree_count}</b> tree{'s' if tree_count > 1 else ''} monthly. <br> {f"<a href='https://www.tema.org.tr/en/homepage' id = 'button-17' class='button-17' role='button'> 🌳 Proceed to offset 🌳</a>" if tree_count > 0 else ""}""",  unsafe_allow_html=True)

if resultmid.button("  ", type="secondary"):
    click_element('tab-1')

# Goals and Progress Page
def create_goals_page():
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 20px; margin: 20px 0;">
        <h1 style="color: #039e8e; font-size: 2.5em; margin-bottom: 10px;">🎯 Carbon Goals & Progress</h1>
        <p style="font-size: 1.2em; color: #666;">Track your journey to a greener future!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Personal Targets Section
    col1, col2 = goals.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #29ad9f, #1dc8b8); padding: 20px; border-radius: 15px; margin: 10px 0; color: white;">
            <h2 style="margin: 0 0 15px 0;">🎯 Personal Targets</h2>
        </div>
        """, unsafe_allow_html=True)
        
        target_emission = st.number_input("Monthly Carbon Target (kg CO₂e)", min_value=0, max_value=10000, value=2000, step=100)
        target_date = st.date_input("Target Date", value=None)
        
        if st.button("Set New Target", type="primary"):
            st.success(f"🎯 Target set: {target_emission} kg CO₂e by {target_date}")
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #99d9d9, #b4e3dd); padding: 20px; border-radius: 15px; margin: 10px 0; color: white;">
            <h2 style="margin: 0 0 15px 0;">📊 Current Progress</h2>
        </div>
        """, unsafe_allow_html=True)
        
        current_emission = st.number_input("Current Monthly Emission", min_value=0, max_value=10000, value=prediction, step=100)
        progress_percentage = max(0, min(100, ((target_emission - current_emission) / target_emission) * 100))
        
        st.metric("Progress", f"{progress_percentage:.1f}%", f"{current_emission} kg CO₂e")
        st.progress(progress_percentage / 100)
    
    # Milestones Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); padding: 20px; border-radius: 15px; margin: 20px 0; color: white;">
        <h2 style="margin: 0 0 15px 0;">🏆 Milestones</h2>
    </div>
    """, unsafe_allow_html=True)
    
    milestone_col1, milestone_col2, milestone_col3 = goals.columns(3)
    
    with milestone_col1:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h3 style="color: #ff6b6b; margin: 0;">🌱 Beginner</h3>
            <p style="margin: 5px 0;">First 10% reduction</p>
            <div style="font-size: 2em;">🎉</div>
        </div>
        """, unsafe_allow_html=True)
    
    with milestone_col2:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h3 style="color: #ff8e8e; margin: 0;">🌿 Eco Warrior</h3>
            <p style="margin: 5px 0;">25% reduction achieved</p>
            <div style="font-size: 2em;">🏆</div>
        </div>
        """, unsafe_allow_html=True)
    
    with milestone_col3:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h3 style="color: #29ad9f; margin: 0;">🌍 Climate Hero</h3>
            <p style="margin: 5px 0;">50% reduction milestone</p>
            <div style="font-size: 2em;">👑</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Streaks Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4ecdc4, #44a08d); padding: 20px; border-radius: 15px; margin: 20px 0; color: white;">
        <h2 style="margin: 0 0 15px 0;">🔥 Streaks</h2>
    </div>
    """, unsafe_allow_html=True)
    
    streak_col1, streak_col2 = goals.columns(2)
    
    with streak_col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <h3 style="color: #4ecdc4; margin: 0 0 10px 0;">🔥 Current Streak</h3>
            <div style="font-size: 3em; margin: 10px 0;">7</div>
            <p style="margin: 0;">Days of eco-friendly choices</p>
        </div>
        """, unsafe_allow_html=True)
    
    with streak_col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <h3 style="color: #44a08d; margin: 0 0 10px 0;">🏆 Best Streak</h3>
            <div style="font-size: 3em; margin: 10px 0;">21</div>
            <p style="margin: 0;">Days achieved</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Challenges Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8e6cf, #88d8c0); padding: 20px; border-radius: 15px; margin: 20px 0; color: white;">
        <h2 style="margin: 0 0 15px 0;">🎮 Weekly Challenges</h2>
    </div>
    """, unsafe_allow_html=True)
    
    challenge_col1, challenge_col2, challenge_col3 = goals.columns(3)
    
    with challenge_col1:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h4 style="color: #a8e6cf; margin: 0;">🚶‍♂️ Walk More</h4>
            <p style="font-size: 0.9em; margin: 5px 0;">Walk 10,000 steps daily</p>
            <div style="font-size: 1.5em;">👟</div>
        </div>
        """, unsafe_allow_html=True)
    
    with challenge_col2:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h4 style="color: #88d8c0; margin: 0;">♻️ Zero Waste</h4>
            <p style="font-size: 0.9em; margin: 5px 0;">Reduce waste by 50%</p>
            <div style="font-size: 1.5em;">🌱</div>
        </div>
        """, unsafe_allow_html=True)
    
    with challenge_col3:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.8); border-radius: 10px; margin: 5px;">
            <h4 style="color: #29ad9f; margin: 0;">💡 Energy Saver</h4>
            <p style="font-size: 0.9em; margin: 5px 0;">Turn off unused lights</p>
            <div style="font-size: 1.5em;">💡</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Action Buttons
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <button style="background: linear-gradient(135deg, #29ad9f, #1dc8b8); color: white; border: none; padding: 15px 30px; border-radius: 25px; font-size: 1.1em; margin: 0 10px; cursor: pointer;">📊 View Detailed Analytics</button>
        <button style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); color: white; border: none; padding: 15px 30px; border-radius: 25px; font-size: 1.1em; margin: 0 10px; cursor: pointer;">🏆 Share Achievements</button>
    </div>
    """, unsafe_allow_html=True)

# Call the goals page function
create_goals_page()

# Dashboard Page
def create_dashboard_page():
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 25px; margin: 20px 0; color: white;">
        <h1 style="font-size: 2.5em; margin: 0;">🌱 Eco Dashboard</h1>
        <p style="font-size: 1.2em; margin: 10px 0;">Track Your Carbon Journey & Achievements</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = dashboard.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <div style="font-size: 2.5em;">🌍</div>
            <h3 style="color: #667eea; margin: 10px 0;">2,847 kg</h3>
            <p style="color: #666; margin: 5px 0;">Monthly CO₂</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <div style="font-size: 2.5em;">🔥</div>
            <h3 style="color: #ff6b6b; margin: 10px 0;">14 Days</h3>
            <p style="color: #666; margin: 5px 0;">Current Streak</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <div style="font-size: 2.5em;">🏆</div>
            <h3 style="color: #4ecdc4; margin: 10px 0;">8 Badges</h3>
            <p style="color: #666; margin: 5px 0;">Earned</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; margin: 10px 0;">
            <div style="font-size: 2.5em;">🎯</div>
            <h3 style="color: #29ad9f; margin: 10px 0;">78%</h3>
            <p style="color: #666; margin: 5px 0;">Goal Progress</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation to full dashboard
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <a href="dashboard.py" target="_self" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px 30px; border-radius: 25px; text-decoration: none; font-size: 1.1em; display: inline-block;">🚀 View Full Dashboard</a>
    </div>
    """, unsafe_allow_html=True)

# Call the dashboard page function
create_dashboard_page()

with open("./style/footer.html", "r", encoding="utf-8") as footer:
    footer_html = f"""{footer.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)

script()
