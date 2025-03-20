#!/usr/bin/python3
"""Create a flask app that renders an html template"""
from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data.get('items', [])
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    products = []

    if source not in ["json", "csv"]:
        return render_template('product_display.html', error="Wrong source")

    if source == "json":
        try:
            with open("products.json", 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error="Wrong source")

    if source == "csv":
        try:
            with open("products.csv", 'r') as f:
                data = csv.DictReader(f)
                for row in data:
                    products.append(row)
        except FileNotFoundError:
            return render_template('product_display.html', error="Wrong source")
    
    if id:
        products = [product for product in products if id == str(product["id"])]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
