from istorage import IStorage
import json


class StorageJson(IStorage):
    '''Allows movies data to be stored in json format'''
    def __init__(self, file_path: str):
        """Initialize JSON storage.

                Args:
                    file_path (str): Path to the JSON file."""

        self.file_path = file_path

    def list_movies(self):
        """List all movies in the database.

                Returns: A dictionary of movies."""

        try:
            with open(self.file_path, "r") as fileobj:
                data = json.loads(fileobj.read())
                return data

        except FileNotFoundError:
            return {}

    def add_movie(self, title: str, year: int, rating: float, poster: str):
        """Add a movie to the json storage.

                Args:
                    title (str): Movie title.
                    year (int): Movie release year.
                    rating (float): Movie rating.
                    poster (str): Movie poster URL.

                Raises:
                    TypeError: If any argument is of the wrong type."""

        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer.")
        if not isinstance(rating, (float, int)):  # Allow both float and int for ratings
            raise TypeError("Rating must be a float or an integer.")
        if not isinstance(poster, str):
            raise TypeError("Poster must be a string.")

        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title: str):
        """Delete a movie from the database.

                Args:
                    title (str): Title of the movie to delete.

                Returns:
                    bool: True if the movie was deleted, False otherwise.

                Raises:
                    TypeError: If title is not a string."""

        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            return True
        return False

    def update_movie(self, title: str, rating: float):
        """Updates a movie rating. Loads the information from the JSON file, updates the movie,
            and saves it.

                Args:
                    title (str): The title of the movie to update.
                    rating (float): The new rating of the movie.

                Returns:
                    bool: True if the movie was updated, False otherwise.

                Raises:
                    TypeError: If title is not a string or rating is not a float."""

        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(rating, (float, int)):
            raise TypeError("Rating must be a float or an integer.")

        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
            return True
        return False

    def _save_movies(self, movies):
        """Save the movies to the JSON file.

        Args:
            movies: The movies to save.
        """
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)