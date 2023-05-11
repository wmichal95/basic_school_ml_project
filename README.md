# Project for the "advanced programming in python" classes

### Application is trying to predict the quality of red wine based on physicochemical properties.

## Endpoints

1. `GET /ui` - swagger user interface
2. `PUT /wine_predict` endpoint takes 11 physicochemical properties and trying to predict the quality

## Setup

The application uses pip package installer for Python, there are 2 files in the project:
- requirements.in - a file in which the used libraries are defined along with the version.
- requirements.txt - a file generated automatically based on requirements.in.

To add a new library, enter the name and version and then use the `pip-compile requirements.in` command

To install the libraries used in the project, use the `pip install -r requirements.txt` command

After installing the necessary libraries, we can run the project. We use the `flask run` command