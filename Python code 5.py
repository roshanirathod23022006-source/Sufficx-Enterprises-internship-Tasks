import random

# Dictionary of moods with sample YouTube links
music_links = {
    "happy": [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy - Pharrell
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  # Gangnam Style
        "https://www.youtube.com/watch?v=JGwWNGJdvx8"   # Shape of You
    ],
    "sad": [
        "https://www.youtube.com/watch?v=hLQl3WQQoQ0",  # Someone Like You
        "https://www.youtube.com/watch?v=RgKAFK5djSk",  # See You Again
        "https://www.youtube.com/watch?v=uelHwf8o7_U"   # Love The Way You Lie
    ],
    "focus": [
        "https://www.youtube.com/watch?v=wp43OdtAAkM",  # Instrumental
        "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lofi Hip Hop Radio
        "https://www.youtube.com/watch?v=DWcJFNfaw9c"   # Chill beats
    ]
}

# Ask user for mood
mood = input("Enter your mood (happy / sad / focus): ").lower()

# Recommend music
if mood in music_links:
    print("Here’s a song for you 🎶:", random.choice(music_links[mood]))
else:
    print("Sorry, mood not found. Try: happy, sad, or focus.")
