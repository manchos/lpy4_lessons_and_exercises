from db import User, db_session

authors = [
    {
        'first_name': 'Василий',
        'last_name' :  'Петров',
        'email' : 'vasyataexample.com1'
    },
    {
        'first_name':  'Маша',
        'last_name' :  'Иванова',
        'email' :  'mari@example.com'
    },
    {
        'first_name':  'Полуэкт',
        'last_name':  'Невструев',
        'email':  'p@example-com1'
    }
]

for a in authors:
    author = User(a['first_name'], a['last_name'], a['email'])
    db_session.add(author)

db_session.commit()