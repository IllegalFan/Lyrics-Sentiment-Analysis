import billboard
import json
import lyricsgenius


def get_song_lyrics(title, artist):
    genius = lyricsgenius.Genius("zs5xO7TXWZJmNrreRWmBX9nMPDjw4GeT3C1dd_bNUF_0UysfPgyYw0SgFUUXTotE")
    index = artist.lower().find("featuring")
    if index != -1:
        artist = artist.lower()[:index]
    artist = genius.search_artist(artist, max_songs=0, sort="title")
    if artist is not None:
        song = artist.song(title)
    else:
        song = None
    if song is not None:
        index = song.lyrics.find("Lyrics")
        if index != -1:
            lyrics = song.lyrics[index + len("Lyrics"):]
        else:
            lyrics = song.lyrics
    else:
        lyrics = "None"
    return lyrics


def get_top_songs_by_year(start_year=1990, end_year=2023, output_file="top_pop_songs.json"):
    songs_by_year = {}
    for year in range(start_year, end_year + 1):
        chart_date = f"{year}-06-01"  # Using January 1st of each year as a reference date
        try:
            chart = billboard.ChartData('hot-100', date=chart_date)
            songs = []
            for song in chart:
                lyrics = get_song_lyrics(song.title, song.artist)
                songs.append({
                    'title': song.title,
                    'artist': song.artist,
                    'lyrics': lyrics,
                    'rank': song.rank
                })
            songs_by_year[year] = songs
        except Exception as e:
            print(f"Error fetching data for {year}: {e}")
    with open(output_file, 'w') as f:
        json.dump(songs_by_year, f, indent=4)
    print(f"Data saved to {output_file}")


if __name__ == "__main__":
    list = [2019,2018,2017,2016]
    for year in list:
        startyear = year
        endyear = year
        get_top_songs_by_year(startyear,endyear,f"Hot_100_06_01/{startyear}_hot_100.json")
