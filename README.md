# webit

Webit inicialmente es un conjunto de scripts en Python 2.X para generar un archivo index.html completo, mostrando información de un nodo Bitcoin al que accede mediante rpc.

Por defecto accede al nodo instalado en la misma máquina en el que es ejecutado(127.0.0.1).Los parametros host, port, password y user pueden ser personalizados en el archivo node.py en la sección rpc Connection:

rpc Connection

host_rpc= '127.0.0.1'
port_rpc=8332
user_rpc=''
pass_rpc=''

#Dependencias

Webit requiere para su funcionamiento de las siguientes librerias Python:

bitcoinrpc - https://github.com/jgarzik/python-bitcoinrpc
