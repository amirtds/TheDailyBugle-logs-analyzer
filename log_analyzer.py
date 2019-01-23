import psycopg2 #importing postgresql lib from connecting to DB
import datetime

class Analyzer:
    def __init__(self, DB_NAME):
        self.dbname = DB_NAME
        self.connection = None

    # stablish connection to database named news
    def get_connection(self):
        self.connection = psycopg2.connect(dbname=self.dbname)

    # define func that returns 3 most popular articles
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
        print "\n###################### TOP 3 ARTICLES ######################"
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

    # get most popular authors, we find them based on the most popular articles
    def get_top_authors(self):
        # this query return most popualr authors based on their articles views
        self.query = '''
        SELECT authors.name, count(articles.title) as num
    	FROM log
    	JOIN articles ON log.path = concat('/article/', articles.slug)
    	left join authors on articles.author = authors.id
    	WHERE log.path like '/article/%'
    	GROUP BY authors.name
    	ORDER BY num DESC;'''
        # create a cursor and execute the query
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query)
        self.results = self.cursor.fetchall()
        # print our top 3 articles with their views
        print "\n###################### TOP AUTHORS ######################"
        for author,views in self.results:
            print "############################################################"
            print "{} -- {} Views".format(author, views)

    def get_evil_day(self):
        self.query = '''
        SELECT AllRequests.date,
        (OnlyErrors.errors * 100.00)/AllRequests.requets
        AS ErrorsPercentage
        FROM (SELECT CAST(time AS date) AS date ,
        COUNT(*) as requets FROM log GROUP BY date) AllRequests
        LEFT JOIN (SELECT CAST(time AS date) AS errorsdate,
        COUNT(*) AS errors FROM log WHERE status LIKE '4%'
        OR status LIKE '5%' GROUP BY errorsdate order by errors ) OnlyErrors
        ON (AllRequests.date = OnlyErrors.errorsdate)
        ORDER BY ErrorsPercentage desc;'''
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query)
        self.results = self.cursor.fetchall()
        print "\n################## Days Error went over 1% ##################"
        for date, percentage in self.results:
            if percentage > 1 :
                print date.strftime("%b %d, %Y"), "--", "%.2f" % percentage
                print "############################################################"
    def get_close_connection(self):
        self.connection.close()

# create an instance of Analyzer
analyzer = Analyzer('news')

# stablish a connection to news database
analyzer.get_connection()

# run get_top_articles method
analyzer.get_top_articles()

# run get_top_authors method
analyzer.get_top_authors()

# run get_top_authors method
analyzer.get_evil_day()

# close the connection
analyzer.get_close_connection()
