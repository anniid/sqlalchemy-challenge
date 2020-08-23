import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

#Setup
engine=create_engine("sqlite:///hawaii.sqlite")
base=automap_base()
    #reflect tables
base.prepare(engine, reflect=True)
measurement=base.classes.measurement
station=base.classes.station
    #start session
session=Session(engine)

    #flask
app=Flask(__name__)

#routes

@app.route("/") #home
def welcome():
    return(
        f"Hawaii Climate Analysis App<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():


@app.route("/api/v1.0/stations")
def stations():

@app.route("/api/v1.0/tobs")
def temps():



@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None,end=None):