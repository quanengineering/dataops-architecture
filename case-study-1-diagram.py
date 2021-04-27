from diagrams import Cluster, Diagram
from diagrams.onprem.database import PostgreSQL, Mongodb
from diagrams.onprem.queue import Kafka
from diagrams.programming.language import Go

with Diagram("Case Study 1", show=False):
    mongodb = Mongodb("mongodb")

    with Cluster("data collector"):
        data_collectors = [
            Go("collector1"),
            Go("collector2"),
            Go("collector3")]

    kafka = Kafka("stream")

    with Cluster("data transformer"):
        data_transformers = [
            Go("transformer1"),
            Go("transformer2"),
            Go("transformer3")]

    postgresql = PostgreSQL("postgresql")

    mongodb >> data_collectors
    data_collectors >> kafka
    kafka >> data_transformers
    data_transformers >> postgresql
