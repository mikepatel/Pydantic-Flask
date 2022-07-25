"""
Michael Patel
July 2022

Project description:

File description:

"""
################################################################################
# Imports
from datetime import datetime
from flask import Flask
from flask_pydantic import validate
from pydantic import BaseModel
from typing import Optional


################################################################################
# Pydantic models
class Player(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    team: Optional[str]


class Input(BaseModel):
    input: Player


class Output(BaseModel):
    output: Player


################################################################################
# Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return str(datetime.now())


@app.route("/player", methods=["GET"])
@validate()
def get_player(query: Player):
    output = f'Getting player: {query.json()}'
    return output


@app.route("/player", methods=["POST"])
@validate()
def create_player(body: Player):
    output = f'Creating a new player called {body.first_name} {body.last_name} who plays for the {body.team}'
    return output


################################################################################
# Main
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
