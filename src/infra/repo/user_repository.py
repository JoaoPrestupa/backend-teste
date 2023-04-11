# pylint: disable=E1101

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





