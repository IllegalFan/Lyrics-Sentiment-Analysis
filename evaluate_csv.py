import pandas as pd
import matplotlib.pyplot as plt

def plot_lyrics_count_by_year(csv_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(csv_file)

    # Step 2: Group by year and count the number of lyrics entries (non-empty lyrics)
    df['lyrics'] = df['lyrics'].fillna('')  # Handle missing lyrics by filling with empty strings
    df['lyrics_length'] = df['lyrics'].apply(lambda x: len(x.strip()))  # Calculate the length of lyrics

    # Filter out entries where lyrics are empty
    df_non_empty_lyrics = df[df['lyrics_length'] > 0]

    # Group by year and count the number of rows (entries with lyrics) for each year
    lyrics_count_by_year = df_non_empty_lyrics.groupby('year').size()

    # Step 3: Plot the result
    plt.figure(figsize=(10, 6))
    lyrics_count_by_year.plot(kind='bar', color='skyblue')

    # Add titles and labels
    plt.title('Number of Lyrics Entries per Year', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Entries', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Path to your CSV file
    csv_file = 'output_winter.csv'

    # Call the function to analyze and plot the data
    plot_lyrics_count_by_year(csv_file)
