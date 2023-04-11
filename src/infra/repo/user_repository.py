# pylint: disable=E1101
from typing import List
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
        """ Class to manage user repository """

            

        @classmethod  #cls == self / com classmethod        #um indicativo pra outros devs q sao strings
        def insert_user(cls, name: str, password: str) -> Users: # -> É OQ VAI RETORNAR
            """
            Insert data in user entity
            :param - name: person name
                - password: user password
            :return tuple with new user
            """

    #para o erro do pylint sumir, tem q comentar na parte de cima do codigo ( pylint: disable=E1101 )
            with DBConnectionHandler() as db_connection:
                try:
                    new_user = UsersModels(name=name, password=password)
                    db_connection.session.add(new_user)

                    db_connection.session.commit()
                    return Users(id=new_user.id, name=new_user.name, password=new_user.password)
                except:
                    db_connection.session.rollback()
                    raise
                finally:
                    db_connection.session.close()
            return none
        
        @classmethod
        def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
             """
            Select data in user entity
            :param - user_id: id of the registry
                    -name: user name
            return - List with Users selected
             """
                    
        try:
            query_data = None
            #se tiver user id e nao name     
            if user_id and not name:
                with DBConnectionHandler() as db_connection: #Abre a conexao
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id).one() #joga em data a query(percorrendo).filtrar por ().devolva um
                    query_data = [data]   #quando faz um select com query assim, é bom retornar com listas
            elif not user_id and name:      
                with DBConnectionHandler() as db_connetion:
                    data = db_connection.session.query(UsersModel).filter_by(name=name).one()
                    query_data = [data]
            elif user_id and name:
                with DBConnectionHandler() as db_connection: #pode ser qualquer var, só usada pra instanciar, a session ja e padrao do bd
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id, name=name).one()
        except:
            db_connection.session.rollback()           
            raise
        finally:
            db_connection.close() 
                    





