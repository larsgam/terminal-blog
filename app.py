from database import Database
from models.post import Post

__author__ = 'larsg'

Database.initialize()

post = Post.from_blog('123')

print(post)