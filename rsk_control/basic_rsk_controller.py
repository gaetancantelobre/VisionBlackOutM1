import rsk

with rsk.Client() as client:
    client.green1.kick(wait_ready = False)