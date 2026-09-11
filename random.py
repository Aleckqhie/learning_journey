# Define the dictionary
favorite_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "action"
}

# Retrieve the genre using .get()
book_genre = favorite_book.get("genre")

print("Genre:", book_genre)
