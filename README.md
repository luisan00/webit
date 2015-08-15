# Webit
Webit is a combination of Python 2.X scripts that generates a complete  web solution . It displays Bitcoin node information which is accessed through rpc.

By default, it accesses the installed node in the same device where it is carried out (127.0.0.1). The parameters, host, port, password and user can be personalized within the settings.py file under the section, rpc Connection:

rpc Connection

	host_rpc= '127.0.0.1'
	port_rpc=8332
	user_rpc=''
	pass_rpc=''

Webit can be installed in several devices such as PC-desktop, laptop,  Server, PC-card type (Raspberry, BeagleBone, etc and similars)

# Requirements
For its proper operation, Webit requires the following Python libraries: 

	bitcoinrpc - <https://github.com/jgarzik/python-bitcoinrpc>

	Tornado Web Server - <https://pypi.python.org/pypi/tornado>
	
	PyGeoIP - <https://github.com/appliedsec/pygeoip>
	
# Installing and Running webit

Installing in linux is as simple as:

	/# cd ~
	/# git clone https://github.com/luisan00/webit.git

And run server.py as follow:

	/# python server.py



This code is licensed under The MIT License (MIT)
Copyright (c) 2015 luisan00
