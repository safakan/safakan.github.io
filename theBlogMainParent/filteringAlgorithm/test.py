## write a class that is called categories with the following restrictions:
## these will be categories for a blog posts.
## it will be possible to add a new category and to get all the categories.

class Categories:
    def __init__(self):
        self.categories = []


## write a blog post class with the following restrictions:
## these will hold all the meta data and content of the blog posts I'll write around various topics
    
class BlogPost:
    def __init__(self, title, author, date, labels, content, description, category):
        self.title = title
        self.author = author
        self.date = date
        self.labels = labels
        self.content = content
        self.description = description
        self.category = category
        


