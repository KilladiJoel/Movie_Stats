import pandas as pd

url = "https://raw.githubusercontent.com/namithar99/task-2-dataset/refs/heads/main/movies_info%20(1).csv"

data = pd.read_csv(url)

print(f"The total number of movies mentioned in the dataset is {len(data)}")

all_genres = set()

for i in data['genres']:
    for j in i[1:-1].split(','):
        all_genres.add(j.strip(" '"))

print(f"The total number of unique genres mentioned in the dataset is {len(all_genres)}")

genres_count = {}

for i in data['genres']:
    for j in i[1:-1].split(','):
        clean_g = j.strip(" '")
        if clean_g in genres_count:
            genres_count[clean_g] += 1
        else:
            genres_count[clean_g] = 1

print("All genres and the total number of movies associated with them:")
for i in genres_count:
    print(f"{i} - {genres_count[i]}")

longest_l = 0
longest_w = ""

for i in data['overview']:
    if type(i) == str:
        if longest_l < len(i):
            longest_l = len(i)
            longest_w = i

print(f"\nThe longest description found is of the length {longest_l} and it is:\n{longest_w}")

idx_with_love = []

for i in range(len(data)):
    if 'love' in data['original_title'][i]:
        idx_with_love.append(i)

print("\nAll movie titles with the word 'love' in them and their overviews:\n")
for i in idx_with_love:
    print(f"Movie title: {data['original_title'][i]}\nMovie overview:\n{data['overview'][i]}\n\n-----------------------\n")