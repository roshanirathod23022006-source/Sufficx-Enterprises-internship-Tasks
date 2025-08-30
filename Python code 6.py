# Simple Emoji Translator

# Dictionary to map words to emojis
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😡",
    "laugh": "😂",
    "fire": "🔥",
    "cool": "😎",
    "food": "🍔",
    "dog": "🐶",
    "cat": "🐱",
    "sun": "☀️",
    "star": "⭐"
}

# Take user input
text = input("Enter a sentence: ").lower()

# Translate words into emojis
translated = ""
for word in text.split():
    translated += emoji_dict.get(word, word) + " "

print("\nEmoji Translation: ", translated.strip())
