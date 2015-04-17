import sqlite3
from datetime import datetime
import threading
import node
import settings 
import GeoIP

dbname = settings.Database_path + settings.Database_name

def createdb():# Create database
    conn= sqlite3.connect(dbname)
    conn.commit()
    conn.close()
    
def trunc(tab):# Truncate tables in database
    conn= sqlite3.connect(dbname)
    cursordb = conn.cursor()
    sql='DROP TABLE IF EXISTS ' + tab
    cursordb.execute(sql)
    conn.commit()
    cursordb.close()
    conn.close()
    if tab == 'nodeinfo':
        createnodeinfo()      
    elif tab == 'peers':
        createpeers()
    elif tab == 'lastblock':
        createlastblock()
    else:
        print('[Error] - No se pudo truncar la tabla ' + tab + ' en la base de datos ' + dbname + ' --- ' + str(datetime.now()))
                
def createnodeinfo():# **** Create tables in database ****
    conn= sqlite3.connect(dbname)
    cursordb=conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS nodeinfo 
    (height INT(16), hash TEXT(16),conn INT(4), diff INT(32), protover INT(8), appver INT(8), time DATETIME)'''
    cursordb.execute(sql)
    conn.commit()
    cursordb.close()
    conn.close()

def createpeers():# **** Create tables in database ****
    conn= sqlite3.connect(dbname)
    cursordb=conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS peers 
    (i INT(8), ident INT(64), addr TEXT(16), Fflag TEXT(6), subver TEXT(16), version INT(8), pingtime INT(8), Brecv INT(64), Bsent INT(64))'''
    cursordb.execute(sql)
    conn.commit()
    cursordb.close()
    conn.close()

def createlastblock():# **** Create tables in database ****
    conn= sqlite3.connect(dbname)
    cursordb=conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS lastblock 
    (height INT(16), hash TEXT(64),  difficulty INT(32), previousblockhash TEXT(64), size INT(32), time INT(16), txcount INT(16))'''
    cursordb.execute(sql)
    conn.commit()
    cursordb.close()
    conn.close()

def dumppeers():# **** Dump new data to database ****
    trunc('peers') # Truncate the table.
    conn = sqlite3.connect(dbname)
    cursordb = conn.cursor()
    list_peers = node.peer_info()
    for i in range(len(list_peers)):
        ident = list_peers[i]['id']
        addr = list_peers[i]['addr']
        subver = list_peers[i]['subver']
        version = list_peers[i]['version']
        pingtime = list_peers[i]['pingtime']
        Brecv = list_peers[i]['bytesrecv']
        Bsent = list_peers[i]['bytessent']
        Fflag = GeoIP.find_country(addr)
        arg =(i+1, ident, addr, Fflag, subver ,version ,int(pingtime*1000),Brecv ,Bsent)
        sql ='''INSERT INTO peers (i, ident, addr, Fflag, subver, version, pingtime, Brecv, Bsent)
                VALUES (?,?,?,?,?,?,?,?,?)''' 
        cursordb.execute(sql,arg)
    conn.commit()
    cursordb.close()
    conn.close()
    
def dumplastblock():# **** Dump new data to database ****
    trunc('lastblock') # Truncate the table.
    conn = sqlite3.connect(dbname)
    cursordb = conn.cursor()
    lastblock = node.get_block(node.get_bestblockhash())
    Bheight = lastblock['height']
    Bhash = lastblock['hash']
    Bdiff = lastblock['difficulty']
    Bprev = lastblock['previousblockhash']
    Bsize = lastblock['size']
    Btime = datetime.fromtimestamp(lastblock['time'])
    BtxCount = len(lastblock['tx'])
    arg =(Bheight, Bhash, int(Bdiff), Bprev, Bsize, Btime, BtxCount)
    sql = '''INSERT INTO lastblock (height, hash, difficulty, previousblockhash, size, time, txcount)
            VALUES (?,?,?,?,?,?,?)'''
    cursordb.execute(sql,arg)
    conn.commit()
    cursordb.close()
    conn.close()
    
def dumpnodeinfo():# **** Dump new data to database ****
    trunc('nodeinfo')
    conn = sqlite3.connect(dbname)
    cursordb = conn.cursor()
    node_info = node.node_info()
    last_block = node_info['blocks']
    last_hash = node.get_hash(last_block)
    peers = node_info['connections']
    difficulty = node_info['difficulty']
    protover = node_info['protocolversion']
    appver = node_info['version']
    servertime = node.nowis()
    arg = (int(last_block), last_hash, int(peers), int(difficulty), int(protover), int(appver), servertime)
    sql = '''INSERT INTO nodeinfo (height, hash, conn, diff, protover, appver, time)
            VALUES (?,?,?,?,?,?,?)'''
    cursordb.execute(sql,arg)
    conn.commit()
    cursordb.close()
    conn.close()
    
def query_db(tab):
        conn = sqlite3.connect(dbname)
        cursordb = conn.cursor()
        sql='SELECT * FROM ' + tab 
        cursordb.execute(sql)
        if tab== 'peers':
            rows = cursordb.fetchall()
        elif tab == 'nodeinfo':
            rows = cursordb.fetchone()
        elif tab == 'lastblock':
            rows = cursordb.fetchone()
        else:
            rows = '[error]'
        cursordb.close()
        conn.close()
        return rows

def query_address():
    conn = sqlite3.connect(dbname)
    cursordb = conn.cursor()
    sql='SELECT addr FROM peers'
    cursordb.execute(sql)
    addresses=cursordb.fetchall()
    cursordb.close()
    conn.close()
    return addresses
    

def refreshdb():
    dumpnodeinfo()
    dumplastblock()
    dumppeers()
    threading.Timer(settings.Interval * 60, refreshdb).start()
