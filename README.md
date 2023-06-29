# Capstone
ALTSchool final year project

URL Shortener Documentation
Introduction
The URL Shortener is a web application that allows users to shorten long URLs into shorter, more manageable links. It provides an easy way to share and track clicks on the shortened URLs.

Features
Shorten URLs: Users can enter a long URL and generate a shortened version of it.
Redirect to Original URLs: Shortened URLs will redirect users to the original long URLs when accessed.
Analytics Tracking: The application tracks the number of clicks each shortened URL receives and provides analytics on the referring websites.

Technologies Used
The URL Shortener application is built using the following technologies:

Python: Backend programming language
Flask: Web framework for building the application
SQLite: Relational database for storing URL data
SQLAlchemy: Object-relational mapping library for working with the database
HTML only
Installation and Setup
Clone the repository from GitHub: URL Shortener Repository
Install Python 3.x on your machine.
Create a virtual environment and activate it.
Install the required Python packages by running pip install -r requirements.txt.
Set up the database by running the necessary migrations using Flask-Migrate.
Start the application by running python server.py.
Access the application through your web browser at http://localhost:5000.

Usage

Shortening a URL
Open the URL Shortener application in your web browser.
Enter the long URL you want to shorten into the input field.
Click the "Shorten" button.
A shortened URL will be generated and displayed on the page.
Accessing the Original URL
Copy the shortened URL.
Open a new tab or window in your web browser.
Paste the shortened URL into the address bar.
Press Enter or Go.
You will be redirected to the original, long URL.

Analytics Tracking

On the URL Shortener application, click the "Analytics" button next to a shortened URL.
Analytics for the selected URL will be displayed, including the number of clicks and the referring websites.


API Reference
The URL Shortener application provides a RESTful API for programmatically interacting with the service. Here are the available API endpoints:

POST /api/shorten: Shorten a URL. Accepts a JSON payload with the long URL and returns the shortened URL.
GET /api/analytics/{short_url}: Get analytics for a shortened URL. Returns the number of clicks and the referring websites.


Conclusion
The URL Shortener is a simple yet powerful application that provides URL shortening functionality with analytics tracking. It offers a user-friendly interface and RESTful API for seamless integration into other applications. With this documentation, you should be able to understand and utilize the features of the URL Shortener effectively.
