# Pokemon Map

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Subject area

Website for help with the game [Pokemon GO](https://www.pokemongo.com/en-us/). This is a game about catching [Pokemon](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

The essence of the game is that Pokemon periodically appear on the map for a certain period of time. Each player can catch a Pokemon and add to their personal collection.

There can be several individuals of the same Pokemon on the map at once: for example, 3 Bulbasaur. Each individual can be caught by several players at once. If a player catches an individual Pokémon, it disappears for him, but remains for others.

The game has an evolution mechanic. Pokémon of one species can "evolve" into another. So, for example, Bulbasaur turns into Ivysaur, which turns into Venusaur.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### How to start

To run the site you will need Python version 3.

Download the code from GitHub. Then install dependencies

```sh
pip install -r requirements.txt
```

Start the development server

```sh
python3 manage.py runserver
```

### Environment Variables

Some of the project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in the following format: `VARIABLE=value`.

There are 2 variables available:
- `DEBUG` - debug mode. Set to True to see debugging information in case of an error.
- `SECRET_KEY` — secret key of the project

## Project goals

The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).