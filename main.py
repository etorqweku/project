from app import app,db 
from app.models import Agent,Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Agent':Agent,'Post':Post}