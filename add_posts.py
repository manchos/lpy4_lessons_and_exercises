import csv
import datetime

from db import User, Post, db_session

posts_list = []
u = User

with open('files/blog.csv', 'r', encoding = 'utf-8') as f:
    fields = ['title', 'image', 'published', 'content', 'email', 'first_name', 'last_name']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        row['published'] = datetime.datetime.strptime(row['published'], '%d.%m.%Y %H:%M')
        author = u.query.filter(User.email == row['email']).first()
        row['user_id'] = author.id
        print(author)
        posts_list.append(row)
print(posts_list)

for post_data in posts_list:
    post = Post(post_data['title'], post_data['image'], post_data['published'], post_data['content'], post_data['user_id'])
    db_session.add(post)

db_session.commit()
