import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (15, 10)

matches = pd.read_csv(r"week4_project2\matches.csv")
deliveries = pd.read_csv(r"week4_project2\deliveries.csv")

matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)
matches['date'] = pd.to_datetime(matches['date'])

# Matches per season
matches_per_season = matches['season'].value_counts().sort_index()

plt.plot(matches_per_season.index, matches_per_season.values, marker='o')
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.title("Matches Played Per Season in IPL")
plt.savefig("matches_per_season.png", bbox_inches="tight")
plt.show()

# Top teams by wins
team_wins = matches['winner'].value_counts().head(10)

sns.barplot(x=team_wins.values, y=team_wins.index)
plt.xlabel("Total Wins")
plt.ylabel("Team")
plt.title("Top 10 Most Successful IPL Teams")
plt.savefig("top_teams_wins.png", bbox_inches="tight")
plt.show()

# Top run scorers
top_batsmen = (
    deliveries.groupby('batsman')['batsman_runs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(x=top_batsmen.values, y=top_batsmen.index)
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.title("Top 10 Run Scorers in IPL")
plt.savefig("top_run_scorers.png", bbox_inches="tight")
plt.show()

# Top strike rate batsmen
balls_faced = deliveries.groupby('batsman')['ball'].count()
runs_scored = deliveries.groupby('batsman')['batsman_runs'].sum()

strike_rate = (runs_scored / balls_faced * 100)
strike_rate = strike_rate[balls_faced > 500].sort_values(ascending=False).head(10)

sns.barplot(x=strike_rate.values, y=strike_rate.index)
plt.xlabel("Strike Rate")
plt.ylabel("Batsman")
plt.title("Top 10 Batsmen by Strike Rate")
plt.savefig("strike_rate.png", bbox_inches="tight")
plt.show()

# Top wicket takers
valid_wickets = deliveries[
    deliveries['dismissal_kind'].notnull() &
    ~deliveries['dismissal_kind'].isin(['run out', 'retired hurt'])
]

top_bowlers = valid_wickets['bowler'].value_counts().head(10)

sns.barplot(x=top_bowlers.values, y=top_bowlers.index)
plt.xlabel("Wickets Taken")
plt.ylabel("Bowler")
plt.title("Top 10 Wicket Takers in IPL")
plt.savefig("top_wicket_takers.png", bbox_inches="tight")
plt.show()

# Total runs per season
season_runs = (
    deliveries.merge(matches[['id', 'season']],
                     left_on='match_id',
                     right_on='id')
    .groupby('season')['total_runs']
    .sum()
)

plt.plot(season_runs.index, season_runs.values, marker='o')
plt.xlabel("Season")
plt.ylabel("Total Runs")
plt.title("Total Runs Scored Per Season")
plt.savefig("total_runs_per_season.png", bbox_inches="tight")
plt.show()

# Win percentage
matches_played = matches['team1'].value_counts() + matches['team2'].value_counts()
wins = matches['winner'].value_counts()

win_percentage = (wins / matches_played * 100).dropna().sort_values(ascending=False).head(10)

sns.barplot(x=win_percentage.values, y=win_percentage.index)
plt.xlabel("Win Percentage")
plt.ylabel("Team")
plt.title("Top Teams by Win Percentage")
plt.savefig("win_percentage.png", bbox_inches="tight")
plt.show()
