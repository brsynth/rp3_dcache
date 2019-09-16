"""
Cache manager: handle connection and queries to the cache DB
"""

import logging
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from .Utils import default_config


class Manager(object):
    """
    Cache manager: handle connection and queries to the cache DB
    """

    def __init__(
            self, host=None, port=None, username=None, password=None,
            database=None, collection=None, replace=False):
        """
        Cache manager.
        
        The default values are defined in the conf/default.yaml file. Init method
        parameters override the default.
        
        :returns  manager: cache manager
        """
        # Settings
        config = default_config()['db']
        self.host = config['host'] if host is None else host
        self.port = config['port'] if port is None else port
        self.username = config['username'] if username is None else username
        self.password = config['password'] if password is None else password
        self.db_name = config['database'] if database is None else database
        self.cl_name = config['collection'] if collection is None else collection
        self.replace = config['replace'] if replace is None else replace

        # Living objects
        self.client = None
        self.database = None
        self.collection = None
    
    def connect(self):
        """
        Set up the connection with the Mongo DB collection
        """
        self.client = MongoClient(host=self.host, port=self.port, username=self.username, password=self.password)
        self.database = self.client[self.db_name] 
        self.collection = self.database[self.cl_name]
        
    def insert(self, document):
        """
        Insert a document.
        
        The operation is abored by default if the document already exists. The
        insertion is enforced if the replace option of the Manager is set to True. 
        
        :returns  feedback: the MongoClient insert_one reply
        """
        try:
            if self.replace:
                return self.collection.replace_one(filter={"_id": document["_id"]}, replacement=document, upsert=True)
            else:
                return self.collection.insert_one(document)
        except DuplicateKeyError:
            logging.debug('Duplicated key "{}" detected when inserting result, storing skipped'.format(document["_id"]))
            return None
    
    def find(self, document_id):
        """
        Find a document
        
        :returns   document: .. .. .
        """
        return self.collection.find_one({"_id": document_id})
