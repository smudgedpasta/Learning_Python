CaveStory_Characters = ["Quote", "Curly", "Toroko", "Arthur", "Sue", "Misery", "Balrog"]

for item in CaveStory_Characters:
    print(f"One of the characters from Cave Story is {item}")
    if item == "Arthur": # < If this item does not exist, the break statement won't execute
        break # < This prevents the else statement and everything else on the list from executing
else:
    print("This else comes after the for loop.")

More_CaveStory_Characters = {
    "Kazuma": "Sakamoto",
    "Momorin": "Sakamoto",
    "King": "the Mimiga",
    "Jack": "the Mimiga",
    "Jenka": "the Witch",
    "Ballos": "the Potato Head"
}

for key in More_CaveStory_Characters:
  print(key, "-", More_CaveStory_Characters[key])