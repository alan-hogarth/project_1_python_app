from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visit import Visit
import repositories.visit_repository as visit_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

trips_blueprint = Blueprint("trips", __name__)

@trips_blueprint.route("/trips")
def trips():
    trips = visit_repository.select_all() 
    return render_template("trips/index.html", trips = trips)

@trips_blueprint.route("/trips/new", methods=['GET'])
def new_trip():
    users = user_repository.select_all()
    city = city_repository.select_all()
    country = country_repository.select_all()
    return render_template("trips/new.html", users = users, city = city, country = country)

@trips_blueprint.route("/trips",  methods=['POST'])
def create_task():
    user_id = request.form['user_id']
    city_id = request.form['city_id']
    country_id = request.form['country_id']
    to_visit = request.form['to_visit']
    user = user_repository.select(user_id)
    city = city_repository.select(city_id)
    country = country_repository.select(country_id)
    visit = Visit(user, city, country, to_visit)
    visit_repository.save(visit)
    return redirect('/trips')