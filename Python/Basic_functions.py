#How to connect to database
# How to connect to database, insert, delete, update, and search
# db base must be started for the script to work correct
from pymongo import MongoClient


def find_function(data):
    # return everything in database
    stud = data.find()

    print 'INSERT & FIND'
    for student_ in stud:
        print student_

    print 'Refined search'
    # returns only what is specified: all entity with last name Dock
    last_name_dock = data.find({'last_name': 'Dock'})
    for student_ in last_name_dock:
        print student_

    print 'Access single value'
    for student_ in last_name_dock:
        print student_['name']

    print 'Find a single item'
    # returns the first entity that matches the find condition
    person = data.find_one({'last_name': 'Dock'})
    for a_person in person:
        print a_person


def insert_function(data):

    # looks into the for a collection called student otherwise it will create
    # it automatically
    student = db.student

    # insertion simply follows, if you are missing certain fields it is OK
    student.insert({'name': 'Bob',
                    'last_name': 'Dill',
                    'year': 'Junior'})
    student.insert({'name': 'Josh',
                    'last_name': 'Dock',
                    'year': 'Freshman'})
    student.insert({'name': 'Dave',
                    'last_name': 'Dock',
                    'year': 'Freshman'})
    student.insert({'name': 'Max',
                    'last_name': 'hat'})
    # Inserting in bulks
    user_profiles = [
         {'last_name': 'Pika', 'name': 'Luke'},
         {'last_name': 'Todd', 'name': 'Ziltoid'}]
    result = data.insert_many(user_profiles)


def delete_function(data):
    # Delete a single item
    print 'Deleting BOB'
    dock = data.find({'name': 'Bob'})
    dock.remove(dock)


def clear_database(data):
    # iterate over the database and delete each item
    for item in data.find():
        item.remove(item)
    print 'Database has been cleared!'


def update_function(data):
    student = data.find_one({'name': 'Max'})
    student['year'] = 'Freshman'
    data.save(student)

    print 'Update records'
    for student_ in data.find():
        print student_
    

if __name__ == "__main__":
    
    # MongoClient check if test database: aggreation_example
    # exist otherwise it will create the database automatically
    db = MongoClient().aggreation_example

    # looks into the for a collection called student otherwise it will create
    # it automatically
    students = db.student

    insert_function(students)
    find_function(students)
    update_function(students)
    delete_function(students)

    # Should not run this function normally, only meant for this tutorial
    # so that you may run this code several time with out seeing multiple
    # of the same inserts.
    clear_database(students)






