import tkinter as tk
from tkinter import scrolledtext, Entry, Button

import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    neutral_words = ["okay", "average", "neutral", "normal", "standard", 'decent', 'gets the job']

    words = word_tokenize(text.lower())

    if sentiment_score >= 0.05:
        sentiment = 'Positive'
        if any(word in neutral_words for word in words):
            sentiment = 'Neutral'
    elif sentiment_score <= -0.05:
        sentiment = 'Negative'
        if any(word in neutral_words for word in words):
            sentiment = 'Neutral'
    else:
        sentiment = 'Neutral'

    return sentiment

# Function to handle user input
def handle_user_input():
    user_input = user_entry.get()
    result = analyze_sentiment_vader(user_input)

    # Display the sentiment result
    result_label.config(text=f"Sentiment: {result}")

    # Clear the user input field
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Configure window size and position it at the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Configure window background color for dark mode
root.configure(bg="#121212")  # Use a dark background color

# Add a big heading at the top in center with different font and dark mode color
heading_label = tk.Label(root, text="Sentiment Analysis Tool", bg="#121212", fg="white", font=("Comic Sans MS", 36, "bold"))
heading_label.pack(pady=20)

# Create an entry widget for user input with dark mode color and larger font
user_entry = Entry(root, width=100, font=("Courier", 16), bg="#2E2E2E", fg="white")
user_entry.pack(pady=10)

# Create a button to analyze sentiment with dark mode color
analyze_button = Button(root, text="Analyze Sentiment", command=handle_user_input, font=("Brush Script MT", 28), bg="#E4405F", fg="black")
analyze_button.pack(pady=10)

# Create a label to display the sentiment result with dark mode color and larger font
result_label = tk.Label(root, text="Sentiment: ", bg="#121212", fg="white", font=("Brush Script MT", 24))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
