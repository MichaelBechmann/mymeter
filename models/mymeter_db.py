# -*- coding: utf-8 -*-
if 0: 
    from gluon import DAL
    
import config
from gluon.tools import Auth

db = DAL(config.db_connection_string)


auth = Auth(db)
auth.define_tables()



