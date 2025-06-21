#!/usr/bin/env python3
"""
Module: task_02_requests
Provides functions to fetch data from an API and save it to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post["title"])
    except requests.exceptions.RequestException as e:
        print(f"[RequestException] {e}")


def fetch_and_save_posts():
    """Fetch posts and save them as CSV file with id, title, and body."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
                writer.writeheader()
                for post in posts:
                    writer.writerow({
                        "id": post["id"],
                        "title": post["title"],
                        "body": post["body"]
                    })
    except requests.exceptions.RequestException as e:
        print(f"[RequestException] {e}")
