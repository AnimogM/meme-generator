# Meme Generator Project

## Overview

Meme Generator which is the second project of the Intermediate Python Nanodegree. The task was to build a python application to generate random memes from user inputs through a command line and web interface. The inputs include quote, author, and image.


## Getting Started

### Flask Web Interface

- Clone the repo with <code>git clone https://github.com/AnimogM/meme-generator.git</code>
- Use pipenv to create a virtual environment and install the dependencies in the requirements.txt file with <code>pipenv install -r requirements.txt</code>
- Activate your virtual environment with <code>pipenv shell</code> and Run `python app.py` on the terminal.
- Click the link to access the app [http://localhost:5000](http://localhost:5000).

### Command Line Interface

- Run `python meme.py` on the terminal, and pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  Resulting in a command like the following: python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]
