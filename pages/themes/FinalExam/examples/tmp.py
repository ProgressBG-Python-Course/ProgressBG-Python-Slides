import requests
import redis
import json

# Initialize the Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def get_external_data(url):
    cache_key = f"url_cache:{url}"
    try:
        # Attempt to fetch fresh data
        response = requests.get(url, timeout=5)  # 5-second timeout
        response.raise_for_status()

        # Cache the fresh data with an expiration time (e.g., 3600 seconds)
        redis_client.setex(cache_key, 3600, response.text)

        return response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
        # On error, fallback to cached data if available
        cached_response = redis_client.get(cache_key)
        if cached_response is not None:
            return json.loads(cached_response)  # Parse the JSON data from the cache
        else:
            # If no cache is available, re-raise the exception or handle it as needed
            print(f"Failed to fetch data and no cache available: {e}")
            raise

# Example usage
url = "https://jsonplaceholder.typicode.com/posts"
data = get_external_data(url)
print(data)
