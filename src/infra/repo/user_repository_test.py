#from faker import Faker
#from sqlalchemy import text
#from src.infra.config import DBConnectionHandler
#from .user_repository import UserRepository

#faker = Faker()
#user_repository = UserRepository()
#db_connection_handler = DBConnectionHandler()

#def test_insert_user():
#    """Should Insert User"""
#    name = faker.name()
#    password = faker.word()
#    engine = db_connection_handler.get_engine()
#    #SQL Commands
#    new_user = user_repository.insert_user(name, password)

    #Em hipotese alguma descomente isso ;-; 

    #query_user = None
    #with engine.connect() as connection:
    #    query_user = connection.execute(text("SELECT * FROM users WHERE id='{}'".format(new_user.id))).fetchone()
#
 #       query_user = engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))
    
  #  assert new_user.id == query_user.id 
   # assert new_user.name == query_user.name
    #assert new_user.password == query_user.password
    

