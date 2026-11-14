import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde
import plotly.graph_objects as go
import numpy as np

# 1. Your exact page configuration (must remain the first Streamlit call)
st.set_page_config(
    page_title="My App",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def load_and_preprocess():
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')
    df = preprocessor.preprocess(df, region_df)
    return df

df = load_and_preprocess()

st.sidebar.header("Olympic Analysis")
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDwXgQG2FQShT5Z7i6ci8a8TJGziQ9dJyMsnDuj-inRw&s=10")
user_menu=st.sidebar.radio(
    'Select an option',
    ('Medal Tally',
     'Overall Analysis',
     'Country-wise Analysis',
     'Athlete wise Analysis'
     )
)



# st.dataframe(df) #used for showing

if(user_menu == "Medal Tally"):
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)
    
    selected_year=st.sidebar.selectbox("Select year",years)
    selected_country=st.sidebar.selectbox("Select country",country)


    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Analysis")
    if selected_year == 'Overall' and selected_country != 'Overall':
       st.title(f"{selected_country}'s overall performance")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f"Medal Tally in {selected_year}'s Olympics")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(f"Medal Tally of {selected_country} in {selected_year}'s Olympics")

    st.dataframe(medal_tally)
    

if(user_menu == "Overall Analysis"):
    st.header("Top Statistics")
    editions,cites,sports,events,athletes,nations=helper.fetch_overall_analysis(df)
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
            st.header("Cities")
            st.title(cites)
    with col3:
            st.header("Sports")
            st.title(sports)

    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)


    nations_over_time=helper.participating_nations_over_time(df)
    fig = px.line(nations_over_time, x=nations_over_time['Year'], y=nations_over_time['No of countries'], title="Participating Countries Over time")
    st.plotly_chart(fig)



    events_over_time=helper.events_over_time(df)
    fig = px.line(events_over_time, x=events_over_time['Year'], y=events_over_time['No of events'], title="Events Over time")
    st.plotly_chart(fig)


    athletes_over_time=helper.athletes_over_time(df)
    fig = px.line(athletes_over_time, x=athletes_over_time['Year'], y=athletes_over_time['No of athletes'], title="Athletes Over time")
    st.plotly_chart(fig)



    st.title("Events over time(Every Sport)")

    d=df.drop_duplicates(['Year','Sport','Event'])
    fig,ax=plt.subplots(figsize=(20,20))
    sns.heatmap(d.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)





    st.title("Most Succesfull Players")
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")
    selected_sport=st.selectbox("Select Sport",sport_list)
    most_successfull=helper.find_top(df,selected_sport)
    st.dataframe(most_successfull)



if(user_menu == "Country-wise Analysis"):
    years,country = helper.country_year_list(df)
    selected_country=st.sidebar.selectbox("Select Country",country)

    cwym=helper.countrywise_yearmedal(df,selected_country)
    st.title(f"How {selected_country} won medals over the years")
    fig = px.line(cwym, x='Year', y='total')
    st.plotly_chart(fig)



    hm=helper.heatmap_year_sport(df,selected_country)
    fig,ax=plt.subplots(figsize=(20,20))
    ax=sns.heatmap(hm.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0).astype(int))
    st.pyplot(fig)




    top_players_of_country=helper.find_top_bycountry(df,selected_country)
    st.dataframe(top_players_of_country)

if(user_menu=="Athlete wise Analysis"):
    athlete_df=df.drop_duplicates(subset=['Name','region'])
    fig, ax = plt.subplots(figsize=(18,8))


    x1=athlete_df['Age'].dropna()
    x2=athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3=athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4=athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    labels = ["Overall Age", "Gold Medalist", "Silver Medalist", "Bronze Medalist"]
    fig = go.Figure()

    for ages, label in zip([x1, x2, x3, x4], labels):
        ages = np.asarray(ages, dtype=float)
        if len(ages) > 1:
            x_range = np.linspace(ages.min(), ages.max(), 200)
            fig.add_trace(go.Scatter(x=x_range, y=gaussian_kde(ages)(x_range), mode='lines', name=label))

    fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Density",
        width=1000,
        height=600
    )
    st.title("Distribution probability of different medals wrt Age")
    st.plotly_chart(fig)







    # Call your helper function
    x, name = helper.age_distribution_by_sport(df)

    
    fig = go.Figure()# initializes a blank Plotly chart canvas.

    for ages, sport in zip(x, name):
        ages = np.asarray(ages, dtype=float)
        ages = ages[~np.isnan(ages)]
        if len(ages) > 1:
            x_range = np.linspace(ages.min(), ages.max(), 200)
            fig.add_trace(go.Scatter(x=x_range, y=gaussian_kde(ages)(x_range), mode='lines', name=sport))

    fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Gold medal winning probability",
        width=1000,
        height=600
    )

    st.title("Distribution of Gold Medalists wrt Age")
    st.plotly_chart(fig)




    sport_list=athlete_df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")
    selected_sport=st.selectbox("Select sport",sport_list)
    h_v_w=helper.weight_v_height(df,selected_sport)
    fig = px.scatter(
        h_v_w, 
        x='Height', 
        y='Weight', 
        color='Medal', 
        symbol='Sex',
        title=f"Height vs Weight for {sport}"
    )
    st.plotly_chart(fig)




    mf_wrtyear=helper.male_female_wrtyear(df)
    #fig = px.line(mf_wrtyear, x=mf_wrtyear['Year'], y=mf_wrtyear['Male','Female'], title="Athletes Over time")
    fig=px.line(mf_wrtyear,x='Year',y=['Male','Female'])
    st.title("Male and female contributions to Olympics over the years")
    st.plotly_chart(fig)
    
