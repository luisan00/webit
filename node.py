import os
from datetime import datetime
from  bitcoinrpc.authproxy import AuthServiceProxy

# rpc Connection
host_rpc= '127.0.0.1'
port_rpc=8332
user_rpc=''
pass_rpc=''

def basic_auth():
    rpcconnection = AuthServiceProxy("http://%s:%s@%s:%s"%(user_rpc,pass_rpc, host_rpc, port_rpc))
    return rpcconnection

def get_hash(n):
    rpcconnection= basic_auth()
    lastblock=rpcconnection.getblockhash(n)
    return lastblock

def get_block(h):
    rpcconnection= basic_auth()
    block = rpcconnection.getblock(h)
    return block

def node_info():
    rpcconnection=basic_auth()
    return rpcconnection.getinfo()

# General nformation about the bitcoin node.
status_rpc = node_info()
blocks = str(status_rpc['blocks'])
lastblock = get_hash(status_rpc['blocks'])
connections = str(status_rpc['connections'])
difficulty = str(status_rpc['difficulty'])
soft_ver = str(status_rpc['version'])
prot_ver = str(status_rpc['protocolversion'])
systemhost = os.name
systemtime = str(datetime.today())

# Information of last block processed.
printblock = get_block(lastblock)
hashblock = str(printblock['hash'])
heightblock = str(printblock['height'])
sizeblock = str(printblock['size']) + ' bytes'
timeblock = str(datetime.fromtimestamp(printblock['time']))
txcount = str(len(printblock['tx']))






