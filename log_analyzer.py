import psycopg2 #importing postgresql lib from connecting to DB

class Analyzer:
    def __init__(self, DB_NAME):
        self.dbname = DB_NAME
        self.connection = None

    # stablish connection to database named news
    def get_connection(self):
        self.connection = psycopg2.connect(dbname=self.dbname)

    # define func that return 3 most popular articles
    def get_top_articles(self):
        # this query return 3 most popualr articles
        # join is based on partial string matching
        self.query = '''
        SELECT articles.title, count(*) as num
        FROM log
        JOIN articles ON log.path = concat('/article/', articles.slug)
        WHERE log.path like '/article/%'
        GROUP BY articles.title
        ORDER BY num DESC limit 3;'''
        # create a cursor and execute the query
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query)
        self.results = self.cursor.fetchall()
        # print our top 3 articles with their views
        print "###################### TOP 3 ARTICLES ######################"
        print "Most Popular article is\n '{}' -- {} Views".format(
            self.results[0][0],int(self.results[0][1])
            )
        print "############################################################"
        print "Second most Popular article is\n '{}' -- {} Views".format(
            self.results[1][0],int(self.results[1][1])
            )
        print "############################################################"
        print "Third most Popular article is\n '{}' -- {} Views".format(
            self.results[2][0],int(self.results[2][1])
            )


# create an instance of Analyzer
analyzer = Analyzer('news')
# stablish a connection to news database
analyzer.get_connection()
# run get_top_articles method
analyzer.get_top_articles()
