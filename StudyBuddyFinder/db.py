import os
import oracledb

from .objects.user import User

class Database:
    def __init__(self):
        self.__user = os.environ['DBUSER']
        self.__password = os.environ['DWPWD']
        self.__host = "198.168.52.211"
        self.__port = 1521
        self.__service_name = 'pdbora19c.dawsoncollege.qc.ca'
        self.__conn = oracledb.connect(
            user=self.__user,
            password=self.__password,
            host=self.__host,
            port=self.__port,
            service_name=self.__service_name
        )
        self.__conn.autocommit = True

    def close(self):
        if self.__conn:
            self.__conn.close()
        self.__conn = None

    def __get_cursor(self):
        for i in range(3):
            try:
                return self.__conn.cursor()
            except Exception as e:
                self.__reconnect()

    def __reconnect(self):
        try:
            self.close()
        except oracledb.Error as e:
            pass
        self.__conn = self.__connect()

    def __connect(self):
        return oracledb.connect(
            user=os.environ['DBUSER'], 
            password=os.environ['DBPWD'],
            host="198.168.52.211", 
            port=1521, 
            service_name="pdbora19c.dawsoncollege.qc.ca"
        )

    # functions for CRUD ops
    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError('User must be a User')