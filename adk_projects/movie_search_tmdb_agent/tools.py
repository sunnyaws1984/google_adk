from typing import Dict, Any
import os
import requests
from dotenv import load_dotenv

BASE_URL = "https://api.themoviedb.org/3"
MOVIE_DETAILS_ENDPOINT = "/movie/{movie_id}"

load_dotenv()
ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")

def get_movie_details(movie_id: int) -> Dict[str, Any]:
    """
    Fetch details of a movie from TMDB given its movie ID.
    
    Args:
        movie_id (int): The TMDB movie ID.

    Returns:
        dict: Parsed JSON response containing movie details, or an error object if the request fails.
    """
    url = f"{BASE_URL}{MOVIE_DETAILS_ENDPOINT.format(movie_id=movie_id)}?api_key={ACCESS_TOKEN}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        movie_data = response.json()

        return {
            "title": movie_data.get("title"),
            "overview": movie_data.get("overview"),
            "release_date": movie_data.get("release_date"),
            "runtime": movie_data.get("runtime"),
            "status": movie_data.get("status"),
            "original_language": movie_data.get("original_language"),
            "spoken_languages": [lang.get("english_name") for lang in movie_data.get("spoken_languages", [])],
            "popularity": movie_data.get("popularity"),
            "vote_average": movie_data.get("vote_average"),
            "vote_count": movie_data.get("vote_count"),
            "budget": movie_data.get("budget"),
            "revenue": movie_data.get("revenue"),
            "production_companies": [c.get("name") for c in movie_data.get("production_companies", [])],
            "production_countries": [c.get("name") for c in movie_data.get("production_countries", [])],
            "genres": [g.get("name") for g in movie_data.get("genres", [])],
            "homepage": movie_data.get("homepage"),
            "imdb_id": movie_data.get("imdb_id")
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
