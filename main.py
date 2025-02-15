from movie_app import MovieApp
from storage_json import StorageJson


def main():
    """
    Initialize and run the Movie Database Application.

    This function creates a JSON storage instance and a MovieApp instance,
    then runs the application.
    """
    # Define the path to the JSON file
    json_file_path = 'data.json'

    # Create a StorageJSON instance
    try:
        storage = StorageJson(json_file_path)
        movie_app = MovieApp(storage)
        movie_app.run()
    except Exception as e:
        print(f"Error initializing the application: {e}")

if __name__ == "__main__":
    main()