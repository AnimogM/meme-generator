"""This is the main app to be served via flask."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        if Ingestor.parse(file) is not None:
            quotes.append(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quotes_list = random.choice(quotes)
    quote = random.choice(quotes_list)
    if quote and img:
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    else:
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "This is a default quote", "Stanley Dukor")
        return render_template('meme.html', path=path)



@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    path = None
    try:
        img = requests.get(image_url)
        img_files = f'tmp/{random.randint(0, 100000000)}.jpg'
        open(img_files, 'wb').write(img.content)
    except:
        print("problem loading image")
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "This is a default quote", "Stanley Dukor")
    else:
        path = meme.make_meme(img_files, body, author)
        os.remove(img_files)
    finally:
        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
