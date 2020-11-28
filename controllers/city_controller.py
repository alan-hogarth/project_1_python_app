from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/index.html", cities = cities)


# @cities_blueprint.route("/cities/<id>")
# def show(id):
#     city = city_repository.select(id)
#     city_users = city_repository.users(city)
#     return render_template("cities/show.html", city=city, users=city_users)