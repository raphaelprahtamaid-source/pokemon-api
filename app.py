from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("pokemon_indonesia_cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

@app.route("/")
def home():
    return {
        "message": "Pokemon Indonesia API"
    }

@app.route("/cards")
def get_cards():
    return jsonify(cards[:100])

@app.route("/cards/<int:card_id>")
def get_card(card_id):
    for card in cards:
        if card.get("id") == card_id:
            return jsonify(card)

    return {"error": "Card not found"}, 404

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port
    )
