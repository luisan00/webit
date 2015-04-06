# webit
Webit is a combination of Python 2.X scripts that generate a complete  web solution . It displays Bitcoin node information which is accessed through rpc.

By default, it accesses the installed node in the same device where it is carried out (127.0.0.1). The parameters, host, port, password and user can be personalized within the settings.py file under the section, rpc Connection:

rpc Connection

	host_rpc= '127.0.0.1'
	port_rpc=8332
	user_rpc=''
	pass_rpc=''

# Requirements
For its proper operation, Webit requires the following Python libraries: 

	bitcoinrpc - https://github.com/jgarzik/python-bitcoinrpc

	Tornado Web Server - https://pypi.python.org/pypi/tornado
	
# Runing webit

Run server.py as follow:

	./server.py



