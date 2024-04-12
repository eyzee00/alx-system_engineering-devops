#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests

def top_ten(subreddit):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set headers to mimic a browser request (Reddit API requires a User-Agent)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates a redirect (300-399), or if not successful (200)
        if 300 <= response.status_code < 400:
            print(None)
            return
        elif response.status_code != 200:
            print(None)
            return

        # Load the JSON data from the response
        data = response.json()
        
        # Access the list of posts
        posts = data['data']['children']
        
        # Print the titles of the posts
        for post in posts:
            print(post['data']['title'])
    
    except requests.RequestException as e:
        # Handle exceptions that occur during the request
        print(None)
