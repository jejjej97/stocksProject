# userdb table
# email(str), pwd(str), name(str)

class detailstocksvo:
    def __init__(self,url, sign, name, code, price, p_eve_price, eve_price_rate, eve_price, m_price, h_price, l_price, trace, trace_price, day_graph, week_graph, month_graph):
        self.url = url;
        self.sign = sign;
        self.name = name;
        self.code = code;
        self.price = price;
        self.p_eve_price = p_eve_price;
        self.eve_price_rate = eve_price_rate;
        self.eve_price = eve_price;
        self.m_price = m_price;
        self.h_price = h_price;
        self.l_price = l_price;
        self.trace = trace;
        self.trace_price = trace_price;
        self.day_graph = day_graph;
        self.week_graph = week_graph;
        self.month_graph = month_graph;

    def geturl(self):
        return self.url
    def getsign(self):
        return self.sign
    def getname(self):
        return self.name
    def getcode(self):
        return self.code
    def getprice(self):
        return self.price
    def getp_eve_price(self):
        return self.p_eve_price
    def geteve_price_rate(self):
        return self.eve_price_rate
    def geteve_price(self):
        return self.eve_price
    def getm_price(self):
        return self.m_price
    def geth_price(self):
        return self.h_price
    def getl_price(self):
        return self.l_price
    def gettrace(self):
        return self.trace
    def gettrace_price(self):
        return self.trace_price
    def getday_graph(self):
        return self.day_graph
    def getweek_graph(self):
        return self.week_graph
    def getmonth_graph(self):
        return self.month_graph

    def seturl(self, url):
        self.url = url
    def setsign(self, sign):
        self.sign = sign
    def setname(self, name):
        self.name = name
    def setcode(self, code):
        self.code = code
    def setprice(self, price):
        self.price = price
    def setp_eve_price(self, p_eve_price):
        self.p_eve_price = p_eve_price
    def seteve_price_rate(self, eve_price_rate):
        self.eve_price_rate = eve_price_rate
    def seteve_price(self, eve_price):
        self.eve_price = eve_price
    def setm_price(self, m_price):
        self.m_price = m_price
    def seth_price(self, h_price):
        self.h_price = h_price
    def setl_price(self, l_price):
        self.l_price = l_price
    def settrace(self, trace):
        self.trace = trace
    def settrace_price(self, trace_price):
        self.trace_price = trace_price
    def setday_graph(self, day_graph):
        self.day_graph = day_graph
    def setweek_graph(self, week_graph):
        self.week_graph = week_graph
    def setmonth_graph(self, month_graph):
        self.month_graph = month_graph


    def pr(self):
        return f'{self.url}',f'{self.sign}',f'{self.name}',f'{self.code}',f'{self.price}',f'{self.p_eve_price}',f'{self.eve_price_rate}',f'{self.eve_price}',f'{self.m_price}',f'{self.h_price}',f'{self.l_price}',f'{self.trace}',f'{self.trace_price}',f'{self.day_graph}',f'{self.week_graph}',f'{self.month_graph}'
