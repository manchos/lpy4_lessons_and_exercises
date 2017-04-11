
from db import User, Post




if __name__ == "__main__":
    me = User('Михаил', 'Корнеев', 'mike@python.ru')
    print(me.email)
    # db_session.add(me)


    me.email = 'korneevm@gmail.com'
    # db_session.commit()

    u = User

    print(u.query.all())
    print(u.query.filter(User.first_name == 'Михаил').first())
    print(u.query.filter(User.first_name.like('М%')).all())

    print(u.query.order_by(User.email).all()) #  По возрастанию (от а до я)

    print("По убыванию: %s" % u.query.order_by(User.email.desc()).all()) # По убыванию (от я до а)

    print("С фамилией с 'ов': %s" % u.query.filter(u.last_name.like('%ов%')).order_by(u.first_name).all())

    p = Post
    blog_post = p.query.get(1)
    print(blog_post.author)