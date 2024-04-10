import rsk

while (1):
    with rsk.Client(host='127.0.0.1', key='') as client:
        client.robots['green'][1].kick()
