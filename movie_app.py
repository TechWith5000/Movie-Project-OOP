from istorage import IStorage

class MovieApp:
    def __init__(self, storage):
        """Initialize the MovieApp with a storage implementation."""

        self._storage = storage


    def _command_list_movies(self):
        """List all movies in the database."""

        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for title, details in movies.items():
                print(f"{title}: {details['rating']}")

    def _command_movie_stats(self):
        """Display movie statistics."""

        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return

        avg_rating = sum(movie['rating'] for movie in movies.values()) / len(movies)
        print(f"Average rating: {avg_rating:.2f}")
        print(f"Number of movies: {len(movies)}")

    def _command_add_movie(self):
        """Add a new movie to the storage."""
        title = input("Enter the title: ")
        year = int(input("Enter the year: "))
        rating = float(input("Enter a rating: "))
        poster = input("Enter poster url string: ")
        movies = self._storage.list_movies()

        if movies:
            try:
                self._storage.add_movie(
                    title, year, rating, poster
                )
                print(f"Movie '{title}' added successfully.")
            except TypeError as e:
                print(f"Error adding movie: {e}")
        else:
            print("Movie could not be found.")

    def _command_delete_movie(self):
        """Delete a movie from the storage."""
        title = input("Enter the title of the movie to delete: ")
        try:
            if self._storage.delete_movie(title):
                print(f"Movie '{title}' deleted successfully.")
            else:
                print(f"Movie '{title}' not found.")
        except TypeError as e:
            print(f"Error deleting movie: {e}")

    def _command_update_movie(self):
        """Update the rating of a movie in the storage."""
        title = input("Enter the title of the movie to update: ")
        try:
            rating = float(input("Enter the new rating (0-10): "))
            if self._storage.update_movie(title, rating):
                print(f"Movie '{title}' updated successfully.")
            else:
                print(f"Movie '{title}' not found.")
        except ValueError:
            print("Invalid rating. Please enter a number.")
        except TypeError as e:
            print(f"Error updating movie: {e}")

    def _generate_website(self):
        ...

    def run(self):
        """Run the main application loop."""

        commands = {
            "1": ("List movies", self._command_list_movies),
            "2": ("Add movie", self._command_add_movie),
            "3": ("Delete movie", self._command_delete_movie),
            "4": ("Update movie", self._command_update_movie),
            "5": ("Movie statistics", self._command_movie_stats),
            "6": ("Generate website", self._generate_website),
        }

        while True:
            print("\n== Movie App ==")
            for key, (description, _) in commands.items():
                print(f"{key}. {description}")
            print("0. Exit")

            choice = input("Enter your choice: ").lower()
            if choice == '0':  # Check for '0' to exit
                print("Goodbye!")
                break
            elif choice in commands:
                commands[choice][1]()
            else:
                print("Invalid choice. Please try again.")
