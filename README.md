# Geek.io

> All geek data in an API


## Routes

### Games

To get all game data:

```sh
/game/
```

To get data from a specified game by id parameter:

```sh
/game/:id
```

```sh
/game/?id=10
```

To get game data filtering by specified category (e.g: rpg, action...):

```sh
/game/category/:category
```

## Development:

- Have python and pip installed
- Turn on your [virtualenv](http://virtualenv.readthedocs.org/en/latest/) (optional and recommended)
- Install requirements:

```sh
pip install -r requirements
```

- Start the server:

```sh
python manage.py runserver
```

## Data Source:

- [IGN](http://www.ign.com)
- [IMDB](http://www.imdb.com/)


# About:

Created by [Raphael Amorim](https://github.com/raphamorim).

Current license is **MIT**.


