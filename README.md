# Movie Stats

A Python script that reads and analyzes a movies dataset from an online CSV file. It starts by loading the data using pandas, then counts the total number of movies in the dataset. From there, it goes through each movie's genre list and finds all the unique genres available, along with how many movies belong to each one.

The script also scans through every movie's overview or description and finds the longest one, printing it out along with its character count. Finally, it searches through all the movie titles and picks out any that contain the word "love", then prints both the title and the full overview for each one.

It's a straightforward script that runs from top to bottom with no menus or user input required, just clean and simple output printed to the console.

## Requirements

- Python 3
- pandas (`pip install pandas`)

## Usage

```bash
python movie_stats.py
```

## What it prints

1. Total number of movies in the dataset
2. Total number of unique genres
3. Count of movies per genre
4. The longest movie overview/description and its length
5. All movie titles containing the word "love", along with their overviews
