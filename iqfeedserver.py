buys=0
sells=0

bestbid = 0
bestask = 0


import socket
import datetime

TCP_IP = '127.0.0.1'
#incoming port to connect to IQfeed
TCP_PORT_IN = 5009
#outgoing port to connect to the trading algorithm
TCP_PORT_OUT = 30000

BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sout.bind((TCP_IP, TCP_PORT_OUT))
sout.listen(1)
connout, addr = sout.accept()
print ('Connection address:', addr)

s.connect((TCP_IP, TCP_PORT_IN))
now = datetime.datetime.now()
s.send(bytes('t@NQZ16\n','ascii'))

s.send(bytes('w@NQZ16\n','ascii'))
incomplete = ''
while True:
    datafull = (s.recv(BUFFER_SIZE)).decode('utf-8')
    datafull = str(incomplete+datafull).split('\n')
    incomplete = datafull.pop()

    for data in datafull:
        data = str(data)
        #print(data)
        if len(data)>0:
            if data[0]=='Q': #represents a quote
                data = data.split(',')
                if data[17][-1]=='t':
                    # get trade update last and quantity (volume)
                    last = float(data[3])
                    quant = float(data[7])
                    if last==bestbid:
                        sells = sells+quant
                    if last==bestask:
                        buys = buys+quant
                bestbid = float(data[10])
                bestask = float(data[11])
                # build a text message to send to the trader and send it over TCP connout
                message =bytes(str(bestbid)+','+str(bestask)+','+str(buys)+','+str(sells)+'\n','ascii')
                connout.send(message)
            if data[0]=='T':
                #time stamp, print it
                print(data)
    now = datetime.datetime.now()




