    ##程序启动入口 
##flask shell上下文管理
from app import app,db
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'sa':sa,'so':so,'db':db,'User':User,'Post':Post}