from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
            """ sqlalchemy database connection """
        #O Py entende o __ como privado
            def __init__(self):
                self.__connection_string = "sqlite:///storage.db"
                self.session = None

            def get_engine(self):
                """Return connection Engine
                :parram - None
                :return - engine connection to Database
                """
                engine = create_engine(self.__connection_string)
                return engine #py precisa identar certo
            


        #Criamos a conexao com o banco de dados, no caso o sqlalchemy. Importamos uma engine do proprio banco e uma classe pra conecta-la
        # uma funcao construtor com a string de conexao e uma var recebendo o status
        # uma funcao q vai receber a criacao da engine(com parametro da conexao_string), retornando a propria var engine.

            def __enter__(self):
                engine = create_engine(self.__connection_string)
                session_maker = sessionmaker()
                self.session = session_maker(bind=engine)
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                self.session.close() # pylint: disable=no-member





