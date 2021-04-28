from diagrams import Diagram
from diagrams.onprem.database import PostgreSQL, Mongodb
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.programming.language import Go

with Diagram("Change data capture", show=False):
    mongodb = Mongodb("mongodb")
    data_collector = Server("Debezium server")
    kafka = Kafka("stream")
    transformer = Go("transformer")
    postgresql = PostgreSQL("postgresql")

    mongodb >> data_collector
    data_collector >> kafka
    kafka >> transformer
    transformer >> postgresql
