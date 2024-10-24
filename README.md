# Udacity Meme generator Project

## Overview
The Meme Generator is a versatile tool designed to effortlessly create memes - images overlaid with quotes. Memes can be either randomly generated from a collection of images and quotes stored in the application's _data directory or tailored to specific user input. The application can be operated via command line interface (CLI) or through a web browser using the Flask app.

## Prerequisites
* Python 3.10 or higher
* xpdf installed in os or pdftotext CLI utility

## Installation
Install dependencies

```bash
  pip install -r requirements.txt
```
 
### CLI
The script `meme.py` creates a meme and prints the path to the generated image. 

It has three optional parameters:
* `path` - path to the base image
* `body` - body of the quote
* `author` - author of the quote (required if body is provided)

Example usage:
* Generate a random meme: `python meme.py`
* Generate a meme from the user input: `python meme.py --path <path/to/file> --body <body> --author <author>`
* Display help: `python meme.py --help`

### Flask app
1. run the application
2. Generate memes at random of from the user input using the GUI in the web browser
## Modules
### QuoteEngine
Sub-package for extracting quotes from a variety of file types. The package consists of the following single-class modules:
* `ingestor_interface` - Interface for classes capable of extracting quotes from files.
* `pdf_ingestor` - Realizes the ingestor interface for pdf input files. Utilizes the `pdftotext` CLI utility via `subprocess` to extract the quotes.
* `docx_ingestor` - Realizes the ingestor interface for docx input files. Utilizes the `python-docx` package to extract the quotes.
* `txt_ingestor` - Realizes the ingestor interface for txt input files.
* `csv_ingestor` - Realizes the ingestor interface for csv input files. Utilizes the `pandas` package to extract the quotes.
* `ingestor` - Encapsulates all the ingestors to provide one interface to extract quotes from any of the supported file type.
* `quote_model` - quote model used by the ingestors.


### MemeGenerator
This module is used for generating memes. The package consists of a single-class module `meme_generator`. The module utilizes the Python Imaging Library `Pillow` to generate memes and is dependant on the `QuoteEngine` package for extraction of quotes from input files.



