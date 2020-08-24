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
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation") #precipitation page
def precipitation():
    last_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation= session.query(measurement.date,measurement.prcp).filter(measurement.date >= last_year).all()
    precip_dict={date:prcp for date, prcp in precipitation}
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations") #station page
def stations():
    stations_query=session.query(station.station).all()
    stations_list=list(np.ravel(stations_query))
    return jsonify(stations_list=stations_list)
@app.route("/api/v1.0/tobs") #temperature page
def temps():
    last_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= last_year).all()
    temps_list=list(np.ravel(results))
    return jsonify(temps_list=temps_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None,end=None):
    #select statement
    select=[func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]

    if not end:
        results1=session.query(*select).filter(measurement.date >= start).all()
        temps_list1=list(np.ravel(results1))
        return jsonify(temps_list1)

    results2= session.query(*select).filter(measurement.date >=start).filter(measurement.date <= end).all()
    temps_list2=list(np.ravel(results2))
    return jsonify(temps_list2=temps_list2)

if __name__=='__main__':
    app.run()