#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))
    else:
        print(f"Error fetching posts: {response.status_code}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts_data = response.json()
        structured_posts = [
            {'id': post.get('id'), 'title': post.get('title'), 'body': post.get('body')}
            for post in posts_data
        ]
        csv_file = 'posts.csv'
        fieldnames = ['id', 'title', 'body']

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
        print(f"Posts saved to {csv_file}")
    else:
        print(f"Error fetching posts for saving: {response.status_code}")
