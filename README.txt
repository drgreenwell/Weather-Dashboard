# Overview

The purpose of this software is to allows users to manage and view weather information dynamically via a web interface, leveraging MongoDB for data storage and retrieval seamlessly integrated with Flask operations. Here's how to use the program:

1. Setup: Ensure Python, Flask, and required packages (pymongo, requests) are installed.

2. Run: Execute the Flask application (python app.py or as configured) to start the web server.

3. Interface: Access the web interface via a browser. The main page (/) shows weather data for previously selected cities. Add a city by submitting a form with its name. The program fetches weather data from OpenWeatherMap API and stores it in MongoDB.

4. Update and Delete: Use buttons or forms to update preferences (/update_preference) by adding new cities or delete existing ones (/delete_preference). These actions update the MongoDB collections (preferences and weather_data) accordingly.

The software has error handling capabilities where, if weather data isn't available for a city, appropriate error messages are displayed.

[Weather Dashboard Demo Video](https://www.youtube.com/watch?v=OLftec-4oX0)

# Cloud Database

The database used for this software is MongoDB.

The structure of the database involved two tables: preferences (which is a collection of user-inputted cities from the dashboard) and weather_data (which is a collection of stored weather information fetched from the OpenWeatherMap API for each city inputted in preferences). Both of these tables contained the data used by the dashboard to display information for the end user.

# Development Environment

This software was developed using Python and Flask.

Flask is a Python web framework used to build web applications. Meanwhile Python was used in the creation of the routes.py, main.py, and config.py that were used to pull the correct data from the database and display it on the dashboard.

# Useful Websites

- [Shayan's "Creating Weather Forecast App in Python using OpenWeatherMaps and MongoDB"](https://www.youtube.com/watch?v=8rV9k2tVWWI)
- [NeuralNine's "MongoDB in Python - NoSQL Document Database"](https://www.youtube.com/watch?v=3wNvKybVyaI)

# Future Work

- Add the ability for users to get a weekly weather forecast for each city inputted into the database.
- Create a user-friendly was to export the information found in the database for personal use.
- Impliment a log in system so that different users can store and recall their own unique list of preferred cities from the database.
