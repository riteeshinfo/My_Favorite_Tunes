# My_Favorite_Tunes
# My_Favorite_Tunes Catalog Project

This Django project allows you to manage and display a catalog of songs and artists. It includes features such as adding new songs, viewing a list of all songs, and displaying details for each song.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python (version 3.6 or higher)
- Django

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/riteeshinfo/My_Favorite_Tunes.git
## Navigate to the project directory:
cd FavoriteTune
## Create a virtual environment:
venv\Scripts\activate
## Apply Migration
~python manage.py makemigration
~python manage.py migrate
## Run server
python manage.py runserver
## Usage
1.Access the Django admin interface at http://localhost:8000/admin/ to add artists and songs to the catalog.
2.View the list of all songs at http://localhost:8000/list/.
3.Click on a song to view its details.
