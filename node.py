from datetime import datetime
from  bitcoinrpc.authproxy import AuthServiceProxy
import settings

# rpc Connection Settings
host_rpc = settings.RPC_host
port_rpc =settings.RPC_port
user_rpc =settings.RPC_user
pass_rpc =settings.RPC_pass

def basic_auth():
    rpcconnection = AuthServiceProxy("http://%s:%s@%s:%s"%(user_rpc,pass_rpc, host_rpc, port_rpc))
    return rpcconnection

def get_bestblockhash():
    rpcconnection = basic_auth()
    bestblockhash =  rpcconnection.getbestblockhash()
    return bestblockhash  
    
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

def peer_info():
    rpcconnection=basic_auth()
    list_peer = rpcconnection.getpeerinfo()
    return list_peer

def nowis():
    tpnow=datetime.utcnow()
    timenow = tpnow.strftime('%Y-%m-%d %H:%M:%S')
    return timenow
