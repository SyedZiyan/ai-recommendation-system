print("🎬 AI Recommendation System")

recommendations = {
    "action": [
        "John Wick",
        "Mad Max: Fury Road",
        "The Dark Knight"
    ],
    "comedy": [
        "3 Idiots",
        "The Hangover",
        "Jumanji"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle"
    ]
}

genre = input(
    "Enter your favorite genre (action/comedy/sci-fi/horror): "
).lower()

if genre in recommendations:
    print("\nRecommended Movies:")
    for movie in recommendations[genre]:
        print("-", movie)
else:
    print("Sorry, no recommendations available.")
