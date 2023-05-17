# Arara Azul CRUD Web App (Work in Progress)

## Introduction

This README file provides an overview of the Arara Azul CRUD web application, which is being developed to support an NGO dedicated to protecting endangered bird species in Brazil. The application is built using Python and the Django library.

The source code for the application can be found on GitHub at: [https://github.com/senajoaop/araraazul-crud](https://github.com/senajoaop/araraazul-crud)

## Purpose

The Arara Azul CRUD web app aims to streamline the management and tracking of data related to endangered bird species and their conservation efforts. It provides basic CRUD (Create, Read, Update, Delete) functionality, allowing users to perform the following operations on the data:

- **Create**: Users can create new bird species records and sightings.
- **Read**: Users can view existing bird species records and sightings.
- **Update**: Users can update the information of bird species records and sightings.
- **Delete**: Users can delete bird species records and sightings.

## Features

The application is currently in its initial stages of development and includes the following features:

- **Authentication**: Users can create accounts and authenticate themselves to access the application.
- **Bird Species Management**: Users can create, view, update, and delete bird species records, including information such as species name, description, habitat, population status, and conservation measures.
- **Sightings Tracking**: Users can record bird sightings, including the date, location, and any additional observations.
- **User Roles**: Different user roles (such as administrators and regular users) can be assigned to control access and permissions within the application.
- **Search and Filtering**: The application provides search and filtering capabilities to easily locate specific bird species or sightings based on various criteria.

## Installation

To run the Arara Azul CRUD web app locally, follow these steps:

1. Clone the repository using the following command:

   ```
   git clone https://github.com/senajoaop/araraazul-crud.git
   ```

2. Change into the project directory:

   ```
   cd araraazul-crud
   ```

3. Create and activate a virtual environment (recommended) to isolate project dependencies:

   ```
   python3 -m venv env
   source env/bin/activate  # for Linux/Mac
   env\Scripts\activate  # for Windows
   ```

4. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

5. Perform database migrations:

   ```
   python manage.py migrate
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Contributing

Contributions to the Arara Azul CRUD web app are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

To contribute code changes, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request on the main repository.

Thank you for your interest in the Arara Azul CRUD web app! Together, we can make a difference in protecting endangered bird species in Brazil.
