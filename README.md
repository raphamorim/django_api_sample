# Geek.io

> All geek data in an API


## Routes

### Games

To get all game data:

``sh
/game/
``

To get data from a specified game by id parameter:

``sh
/game/:id
``

``sh
/game/?id=10
``

To get game data filtering by specified category (e.g: rpg, action...):

``sh
/game/category/:category
``

## Data Source:

- [IGN](http://www.ign.com) 
- [IMDB](http://www.imdb.com/)

## Development:

- Have pip installed
- Turn on your virtualenv (optional and recommended)
- Install requirements:

``sh
pip install -r requirements
``

- Start the server:

``sh
python manage.py runserver
``

or

``sh
./manage.py runserver
``

And for more options information:

``sh
python manage.py --help
``
 
## About:

Created by [Raphael Amorim](https://github.com/raphamorim).

Current license is **MIT**.


