def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
    medal_tally=medal_tally.groupby("NOC")[['Gold','Silver','Bronze']].sum().sort_values("Gold",ascending=False).reset_index()
    medal_tally['total']=medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally

#medal_tally is countrys medals in total


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')

    country=df['region'].dropna().values.unique().tolist()
    country.sort()
    country.insert(0,'Overall')


    return years,country



def fetch_medal_tally(df,year,country):
    medal_df=df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
    flag=0
    if year == 'Overall' and country == 'Overall':
        temp_df=medal_df
    if year == 'Overall' and country != 'Overall':
        flag=1
        temp_df=medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df=medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df=medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x=temp_df.groupby("Year")[['Gold','Silver','Bronze']].sum().sort_values("Year").reset_index()
    else:
        x=temp_df.groupby("region")[['Gold','Silver','Bronze']].sum().sort_values("Gold",ascending=False).reset_index()
    x['total']=x['Gold'] + x['Silver'] + x['Bronze']
    

    return x
    
def fetch_overall_analysis(df):
    editions=df['Year'].unique().shape[0] - 1
    cites=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"]).shape[0]
    nations=df['region'].unique().shape[0]


    return editions,cites,sports,events,athletes,nations


def participating_nations_over_time(df):
    nations_over_time=df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.rename(columns={'index': 'Year', 'count': 'No of countries'}, inplace=True)


    return nations_over_time

def events_over_time(df):
    events_over_time=df.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index().sort_values('Year')
    events_over_time=events_over_time.rename(columns={'count':'No of events'})

    return events_over_time

def athletes_over_time(df):
    athletes_over_time=df.drop_duplicates(['Year','Name'])['Year'].value_counts().reset_index().sort_values('Year')
    athletes_over_time=athletes_over_time.rename(columns={'count':'No of athletes'})

    return athletes_over_time



#finding top athlets from sport given by input
def find_top(dd,sport):
    if sport != 'Overall':
        temp_df=dd[dd['Sport'] == sport]
    else:
        temp_df=dd
    temp_df = temp_df.dropna(subset=["Medal"])
    top_athletes = (
        temp_df["Name"].value_counts().reset_index().head(15).merge(dd,on='Name',how='left')[['Name','count','Sport','region','ID']].drop_duplicates()
    )
    top_athletes.rename(columns={'count':'Medals'},inplace=True)
    return top_athletes




def countrywise_yearmedal(df, country):
    # 1. Drop rows without medals
    temp_df = df.dropna(subset=["Medal"])

    # 2. Drop duplicate team/event rows so team members aren't overcounted  ...this is solving the problem of multiple team members of same team giving same medal output
    temp_df = temp_df.drop_duplicates(
        subset=[
            "Team",
            "NOC",
            "Games",
            "Year",
            "City",
            "Sport",
            "Event",
            "Medal",
        ]
    )

    # 3. Filter by country
    temp_df = temp_df[temp_df["region"] == country]

    # 4. Group by Year and SUM the actual medal columns instead of counting rows
    new_df = (
        temp_df.groupby("Year")[["Gold", "Silver", "Bronze"]]
        .sum()
        .reset_index()
    )

    # 5. Calculate total
    new_df["total"] = (
        new_df["Gold"] + new_df["Silver"] + new_df["Bronze"]
    )

    return new_df



def heatmap_year_sport(df,country):
    temp_df=df.dropna(subset=['Medal'])
    temp_df=temp_df.drop_duplicates(subset=[
            "Team",
            "NOC",
            "Games",
            "Year",
            "City",
            "Sport",
            "Event",
            "Medal",
        ])
    new_df=temp_df[temp_df['region'] == country]

    return new_df





#finding top athlets from sport given by input
def find_top_bycountry(dd,country):
    if country != 'Overall':
        temp_df=dd[dd['region'] == country]
    else:
        temp_df=dd
    temp_df = temp_df.dropna(subset=["Medal"])
    top_athletes = (
        temp_df["Name"].value_counts().reset_index().head(10).merge(dd,on='Name',how='left')[['Name','count','Sport','ID']].drop_duplicates()
    )
    top_athletes.rename(columns={'count':'Medals'},inplace=True)
    return top_athletes


def age_distribution_by_sport(df):
    athlete_df=df.drop_duplicates(subset=['Name','region'])
    #which age gets u a gold medal in each sport
    x = []
    name = []
    famous_sports = [
        'Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
        'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
        'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
        'Water Polo', 'Hockey', 'Rowing', 'Fencing',
        'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
        'Tennis', 'Golf', 'Softball', 'Archery',
        'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
        'Rhythmic Gymnastics', 'Rugby Sevens',
        'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey'
    ]

    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport] #that sport
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()) #age w gold medal
        name.append(sport) 


    return x,name




def weight_v_height(df,sport):
    athlete_df=df.drop_duplicates(subset=['Name','region'])
    athlete_df['Medal'].fillna('No medal',inplace=True)
    temp_df=athlete_df[athlete_df['Sport']== sport]

    return temp_df   


def male_female_wrtyear(df):
    athlete_df=df.drop_duplicates(subset=['Name','region'])
    men=athlete_df[athlete_df['Sex']=='M'].groupby('Year')['Name'].count().reset_index()
    women=athlete_df[athlete_df['Sex']=='F'].groupby('Year')['Name'].count().reset_index()
    final=men.merge(women,on='Year',how='left')
    final.rename(columns={"Name_x":"Male","Name_y":"Female"},inplace=True)


    return final
