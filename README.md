# Pokémon Indonesia API

A free API for Pokémon Trading Card Game cards released in Indonesia.

This project crawls data from the official Pokémon Card Game Indonesia card search and provides a simple REST API for developers, collectors, and fan projects.

## Features

* Search Indonesian Pokémon cards
* Card IDs
* Card names
* HP
* Regulation marks
* Collector numbers
* Card images
* JSON API endpoints
* Open-source

## API Endpoints

### Get API Information

GET /

Example response:

```json
{
  "message": "Pokemon Indonesia API"
}
```

### Get Cards

GET /cards

Returns a list of cards.

### Get Card by ID

GET /cards/{id}

Example:

```
/cards/18272
```

Example response:

```json
{
  "id": 18272,
  "name": "Oddish <Erika>",
  "hp": "60",
  "collectorNumber": "001/123",
  "regulation": "J"
}
```

## Tech Stack

* Python
* Flask
* BeautifulSoup4
* Requests
* JSON Database
* Render

## Installation

```bash
git clone https://github.com/raphaelprahtamaid-source/pokemon-api.git
cd pokemon-api

pip install -r requirements.txt

python app.py
```

## Deploying

This API can be deployed on Render.

Start command:

```bash
gunicorn app:app
```

## Disclaimer

This project is a fan-made API and is not affiliated with, endorsed by, or sponsored by Pokémon, Nintendo, Creatures Inc., GAME FREAK, or The Pokémon Company.

Pokémon and Pokémon card artwork are trademarks of their respective owners.

## License

MIT License

