from cassandra.cluster import Cluster

cluster = Cluster(['cassandra-node1.example.com','cassandra-node2.example.com','cassandra-node3.example.com','cassandra-node4.example.com','cassandra-node5.example.com'])

session = cluster.connect('killrvideo')

result = session.execute("select * from videos_by_tag")

for row in result:
    print(row)
