import os
import django
import json
from django.core.exceptions import ValidationError

def populate_movies():
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app.settings')
    django.setup()

    # Import the Movie model after Django setup
    from movies.models import Movie

    json_file_path = 'movies.json'  # Update the file path if needed

    if not os.path.exists(json_file_path):
        print(f"Error: File '{json_file_path}' does not exist.")
        return

    with open(json_file_path) as f:
        try:
            movies_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")
            return

    for movie_data in movies_data:
        try:
            Movie.objects.create(
                name=movie_data.get('name'),
                description=movie_data.get('description'),
                imgPath=movie_data.get('imgPath'),
                duration=movie_data.get('duration'),
                genre=movie_data.get('genre'),
                language=movie_data.get('language'),
                mpaaRating=movie_data.get('mpaaRating'),
                userRating=movie_data.get('userRating')
            )
        except ValidationError as e:
            print(f"Error creating movie: {e}")

if __name__ == '__main__':
    populate_movies()
