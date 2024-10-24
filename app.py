"""Flask application file."""

import os
import random

import requests
from flask import Flask, abort, render_template, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = [f for f in os.listdir(images_path) if len(f.split(".")) > 1]
    imgs = [images_path + img for img in imgs]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get("image_url")
    file_extension = image_url.split(".")[-1]
    if file_extension not in meme.allowed_extensions:
        allowed_types = ", ".join(meme.allowed_extensions)
        abort(400, f"Wrong file type. Allowed file types: {allowed_types}.")
    r = requests.get(image_url, allow_redirects=True)
    if r.status_code == 200:
        tmp = f"./temp_{random.randint(0, 1000000)}.png"
        with open(tmp, "wb") as img_f:
            img_f.write(r.content)
    else:
        abort(400, f"Unable to download file from {image_url}.")

    quote = request.form.get("body", "")
    author = request.form.get("author", "")

    path = meme.make_meme(tmp, quote, author)

    os.remove(tmp)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
