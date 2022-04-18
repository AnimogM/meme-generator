# Meme Generator Project

## Overview

Meme Generator which is the second project of the Intermediate Python Nanodegree. The task was to build a python application to generate random memes from user inputs through a command line and web interface. The inputs include quote, author, and image.


## Getting Started

### Flask Web Interface

- Run `python app.py` on the terminal.
- Access the webpage via this url [http://localhost:5000](http://localhost:5000).

### Command Line Interface

- Run `python meme.py` on the terminal, and pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  Resulting in a command like the following: python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]
