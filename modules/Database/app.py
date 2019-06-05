'''
    Database connection functionality.

    2019 Benjamin Kellenberger
'''

class Database():

    def __init__(self, config):
        self.config = config

        # get DB parameters
        self.host = config.getProperty(self, 'host')
        self.port = config.getProperty(self, 'port')
        self.user = config.getProperty(self, 'user')
        self.password = config.getProperty(self, 'password')

        self._createConnection()


    def _createConnection(self):
        try:
            self.conn = psycopg2.connect(database=self.host,
                                        user=self.user,
                                        password=self.password)
        except:
            print('Error connecting to database {}:{} with username {}.'.format(
                self.host, self.port, self.user
            ))
            #TODO: next steps


    def runServer(self):
        ''' Dummy function for compatibility reasons '''
        return

    
    def execute(self, sql):
        #TODO: return values, separate sql from data, etc.
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()