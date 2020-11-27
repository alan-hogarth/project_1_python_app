from db.run_sql import run_sql
from models.city import City
from models.country import Country
from models.visit import Visit
from models.user import User

import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

def save(visit):
    sql = "INSERT INTO visits ( user_id, city_id, country_id, to_visit ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [visit.user.id, visit.city.id, visit.country.id, visit.to_visit]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        city = city_repository.select(row['city_id'])
        country = country_repository.select(row['country_id'])
        visit = Visit(user, city, country, row['to_visit'], row['id'])
        visits.append(visit)
    return visits

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)