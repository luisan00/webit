# webit

Webit inicialmente es un conjunto de scripts en Python que generan un archivo index.html completo, mostrando informaci�n de un nodo Bitcoin al que accederemos mediante rpc.

Por defecto accede al nodo instalado en la misma m�quina en el que es ejecutado(127.0.0.1).Los parametros host, port, password y user pueden ser personalizados en el archivo node.py en la secci�n rpc Connection:

# rpc Connection
host_rpc= ''
port_rpc=8332
user_rpc=''
pass_rpc=''

