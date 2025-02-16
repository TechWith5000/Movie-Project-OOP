from movie_app import MovieApp
from storage.storage_csv import StorageCsv


def main():
    """
    Initialize and run the Movie Database Application.

    This function creates a JSON storage instance and a MovieApp instance,
    then runs the application.
    """
    # Define the path to the storage file
    file_path = 'data/movies.csv'

    # Create a StorageJSON instance
    try:
        storage = StorageCsv(file_path)
        movie_app = MovieApp(storage)
        movie_app.run()
    except Exception as e:
        print(f"Error initializing the application: {e}")

if __name__ == "__main__":
    main()