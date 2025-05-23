# Advanced Weather App

An enhanced weather application built with **Flask** that supports persistent storage of weather queries with full CRUD (Create, Read, Update, Delete) functionality. This app allows users to query weather data for different locations and date ranges, stores these queries in a database, and provides options to update or delete stored records. It also includes additional API integrations and robust error handling.

---

## Features

### Core Features
- **Create**: Users can enter a location (city, zip code, etc.) and a date range to fetch weather data and store it in the database.
- **Read**: View previously stored weather queries and their results.
- **Update**: Modify saved weather records with validations on input.
- **Delete**: Remove stored weather queries from the database.

### Additional Functionalities (Optional)

- Data export options in multiple formats like JSON, CSV, XML, and PDF.
- Input validation for location and date ranges with fuzzy matching support.

---

## Technologies Used

- **Flask** - Web framework
- **SQLite** - Database for persistence (can be replaced with other SQL or NoSQL databases)
- **SQLAlchemy** - ORM for database operations
- **Requests** - For external API calls (OpenWeatherMap, Google Maps, etc.)
- **Jinja2** - Templating engine for rendering dynamic HTML
- HTML/CSS/JavaScript for frontend UI and interactivity
