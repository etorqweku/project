from flask_admin.contrib.sqla import ModelView
from app import admin,db
from app.models import Agent,Client,Post
from flask_admin import BaseView,expose

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/analytics_index.html')
    
admin.add_view(ModelView(Agent,db.session))
admin.add_view(ModelView(Client,db.session))
admin.add_view(ModelView(Post,db.session))
admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))