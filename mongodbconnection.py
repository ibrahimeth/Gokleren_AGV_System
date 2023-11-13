from os import stat
from pymongo import MongoClient

class DbConnect(object):
    def __init__(self) -> None:
        super(DbConnect, self).__init__()
        self.cluster = MongoClient("mongodb+srv://<userName>:<PAssword>@cluster0.2eskv.mongodb.net/?retryWrites=true&w=majority")
        self.Database = self.cluster["<YOURCLOSTER>"]
        self.colleciton = self.Database["<YOURCOLECTION>"]
    def control(self, which_info) :
        infom = self.colleciton.find({{which_info}}).sort(-1).limit(1)
        return infom
