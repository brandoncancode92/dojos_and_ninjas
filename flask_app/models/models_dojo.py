from flask_app.config.mysqlconnection import connectToMySQL
from .models_ninja import Ninja

db = "dojos_and_ninjas"
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # gets all the data in Dojos from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []

        # "d" is a representation of data
        for d in results:
            dojos.append(cls(d))
        return dojos

    # Saves new data in Dojos in the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # result comes back as an id
        result = connectToMySQL(db).query_db(query, data)
        return result

    # Gets all ninjas from a certain Dojo in the database
    @classmethod
    def get_one_ninja(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo


