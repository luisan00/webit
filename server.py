#!/usr/bin/env python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from node import nowis
from settings import Server_port
from sqlite import query_db
from sqlite import refreshdb


refreshdb()

define("port", default = Server_port, help="run on the given port", type=int)
   
class MainHandler(tornado.web.RequestHandler): 
        
    def get(self):
        nodeinfo = query_db('nodeinfo')
        lastblock = query_db('lastblock')    
        peers = query_db('peers')
        self.render('./documents/static/index.html', title="Webit", nodeinfo = nodeinfo, lastblock = lastblock, peers = peers)
        

def main():
    tornado.options.absolute_import
    application = tornado.web.Application([
                                           (r"/", MainHandler),
                                           (r'/(.*)', tornado.web.StaticFileHandler,{'path':'./documents/static/'})],
                                            settings = dict(template_path=os.path.join(os.path.dirname(__file__), "./templates"),),)
                        
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print 'Tornado WebServer listening on port ' + str(options.port) + '\t\t\t\t' + nowis() + ' UTC'
    main()