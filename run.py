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
# Pydantic model
class QueryParameters(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    team: Optional[str]
    age: Optional[int]


class RequestBody(BaseModel):
    first_name: str
    last_name: str
    team: str
    age: Optional[int]


################################################################################
# Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return str(datetime.now())


@app.route("/player", methods=["GET"])
@validate()
def get_player(query: QueryParameters):
    return query


@app.route("/player", methods=["POST"])
@validate()
def create_player(body: RequestBody):
    output = f'Creating player :: Name: {body.first_name} {body.last_name}, Team: {body.team}, Age: {body.age}'
    return output


################################################################################
# Main
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
