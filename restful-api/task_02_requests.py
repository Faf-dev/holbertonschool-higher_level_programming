#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    fetch posts from jsonplaceholder then print only the tile of each post
    """

    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        print("Status Code: {}".format(r.status_code))
        all_post = r.json()

        for post in all_post:
            print(post['title'])
    else:
        print("impossible de récupérer les posts")


def fetch_and_save_posts():
    """
    fetch posts from jsonplaceholder then save all
    the posts (unless the userId) in a csv file
    """

    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        all_post = r.json()

        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in all_post
        ]

        try:
            with open("posts.csv", "w", encoding="utf-8") as csvf:
                w = csv.DictWriter(csvf, fieldnames=["id", "title", "body"])
                w.writeheader()
                w.writerows(data)
            return True
        except FileNotFoundError:
            return False
