import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NetFlix.csv")
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

def extract_minutes(value):
    try:
        return int(str(value).split()[0])
    except:
        return None

df['duration_min'] = df['duration'].apply(extract_minutes)
df['genres'] = df['genres'].fillna("")
genres_split = df['genres'].str.split(', ')
all_genres = genres_split.explode()
type_counts = df['type'].value_counts()

plt.figure()
type_counts.plot(kind='bar')
plt.title("Content Count by Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("content_by_type.png")
plt.close()

yearly = (
    df.dropna(subset=['release_year'])
      .astype({'release_year': int})
      .groupby('release_year')
      .size()
)

plt.figure()
yearly.plot()
plt.title("Netflix Content Growth Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_growth.png")
plt.close()

top_genres = all_genres.value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.close()

movie_runtime = df[df['type'] == 'Movie']['duration_min'].dropna()

plt.figure()
movie_runtime.plot(kind='hist', bins=30)
plt.title("Movie Runtime Distribution (Minutes)")
plt.xlabel("Duration (min)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("runtime_distribution.png")
plt.close()

top_years = yearly.sort_values(ascending=False).head(10)

summary = {
    "Total Titles": len(df),
    "Movies": type_counts.get('Movie', 0),
    "TV Shows": type_counts.get('TV Show', 0),
    "Most Common Genre": top_genres.index[0],
    "Year with Most Content": top_years.index[0]
}

print("\n----- Netflix EDA Summary -----")
for k, v in summary.items():
    print(f"{k}: {v}")
