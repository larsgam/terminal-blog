from database import Database
from models.blog import Blog

__author__ = 'larsg'

Database.initialize()

blog = Blog(author='Jose',
            title='Sample title',
            description='Sample Description')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())