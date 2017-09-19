from google import search
import search.utilities as util
import search.query as qu


# Class including functions for OSINT collection using search engines.
class SearchEngines(qu.Query):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Top level domain search
    __TLD__ = "com"
    # Number of results we want back
    __NUM_RESULTS__ = 8
    # Last result to retrieve.  Use none if you want to search forever.
    __STOP__ = 1
    # Lapse to wait between HTTP requests.
    __PAUSE__ = 2

    # returns google search results.
    def googleSearch(self):
        for result in search(self.getQuery, tld=SearchEngines.__TLD__, num=SearchEngines.__NUM_RESULTS__,
                             stop=SearchEngines.__STOP__, pause=SearchEngines.__PAUSE__):
            print(result)
        print()

    # returns duckduckgo searhable link.
    def ddGoSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        ddGoLink = 'https://duckduckgo.com/?q=' + parsedQuery
        print(ddGoLink)
        print()

    # returns a baidu searchable link.
    def baiduSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        baiduLink = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + parsedQuery
        print(baiduLink)
        print()

    # returns a link in bing search engine to search.
    def bingSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        bingLink = 'https://www.bing.com/search?q=' + parsedQuery
        print(bingLink)
        print()

    # returns a link in excite search engine to search - specifically news, latest posts about queries -.
    def exciteNewsSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        exciteNewsLink = 'http://msxml.excite.com/search/news?q=' + parsedQuery + '&fcoid=411&fcop=left&om_nextpage=True&fpid=2'
        print(exciteNewsLink)
        print()

    # returns a link in fact bites search engine to search very old posts about search term.
    def oldArticlesSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        oldArticlesLink = 'http://www.factbites.com/topics/' + parsedQuery
        print(oldArticlesLink)
        print()

    # returns a link in qwant search engine collecting search, media, and social.
    def qwantSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        qwantLink = 'https://www.qwant.com/?q=' + parsedQuery + '&t=all'
        print(qwantLink)
        print()

    # returns a link in clustering websites that provide search to many places.
    def clusteringSearchEngines(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        carrotLink = 'http://search.carrot2.org/stable/search?source=web&view=folders&skin=fancy-compact&query=' + parsedQuery
        cluzLink = 'http://www.cluuz.com/Default.aspx?list=y&yahoo=y&q=' + parsedQuery
        print(carrotLink)
        print(cluzLink)
        print()

    # Executes all of the above functions.
    def searchEngineAllSearches(self):
        print("\n---- SEARCH ENGINES ----")

        print("Google search:")
        self.googleSearch()

        print("DuckDuckGo search:")
        self.ddGoSearch()

        print("Baidu search:")
        self.baiduSearch()

        print("Bing search:")
        self.bingSearch()

        print("Qwant search:")
        self.qwantSearch()

        print("Clustering multi search:")
        self.clusteringSearchEngines()

        print("Excite news search:")
        self.exciteNewsSearch()

        print("Fact bites news search:")
        self.oldArticlesSearch()


# Class responsible for people search engines' search.
class PeopleSearchEngines(SearchEngines):

    def __init__(self, query):
        qu.Query.__init__(self, query)

    # Performs a search in www.pipl.com to capture the social media not captured above.
    def peopleSearch(self):
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery

        parse411 = self.__411parse__()
        link411Website = 'http://www.411.com/name/' + parse411

        print(piplLink)
        print(link411Website)
        print()

    # This function performs search to the optional location in www.pipl.com.
    def piplSearchLocation(self, flag):
        parsedLocation = PeopleSearchEngines.__parseLocation__(self, flag)
        parsedQuery = util.Utilities.parseQuery(self.getQuery)
        piplLink = 'https://pipl.com/search/?q=' + parsedQuery + '&l=' + parsedLocation
        print(piplLink)
        print()

    # Executes all of the above functions.
    def peopleEngineAllSearches(self):
        print("\n---- PEOPLE SEARCH ENGINES ----")

        print("Note: We suggest to add a location to make your search more specific.")
        print("To do so, please use: <name> -i <location> -l")
        print("\nSearch links in multiple people search engines:")
        self.peopleSearch()

        print("Search in pipl search engine with location:")
        self.piplSearchLocation('-i')

    # Parses the query to return the location by splitting it.
    def __parseLocation__(self, flag):
        first = str(flag)
        last = ' -l'
        try:
            stringQuery = self.getQuery
            start = stringQuery.index(first) + len(first)
            end = stringQuery.index(last, start)
            parsedQuery = self.getQuery[start:end]
            subQuery = util.Utilities.substituteSpaces(parsedQuery)
            return subQuery
        except ValueError:
            return ""

    # 411 People search website has a very unique matching of keywords using '-'.
    def __411parse__(self):
        q = util.Utilities.parseQuery(self.getQuery)
        numSpaces = self.getQuery.count(' ')
        return q.replace('+', '-', numSpaces)
