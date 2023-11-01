import json
import kafka

topic = 'test'
env = 'dev'
bootstrap_servers = [
    '0.kafka.prd.cloud.hyas.local:9093',
    '1.kafka.prd.cloud.hyas.local:9093',
    '2.kafka.prd.cloud.hyas.local:9093'
]

# Create consumer
kafka_consumer = kafka.KafkaConsumer(
    topic,
    auto_offset_reset='earliest',
    bootstrap_servers=bootstrap_servers,
    # api_version=(1, 3, 5),
    # api_version=(0, 10, 1),
    # api_version_auto_timeout_ms=60000,
    consumer_timeout_ms=60000,
    enable_auto_commit=False,
    group_id='alerting_{}_{}'.format(env, topic),
    security_protocol='SSL',
    ssl_cafile='/home/hyas/ssl/kafka.crt',
    ssl_check_hostname=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
print('Consumer successfully created! {}'.format(dir(kafka_consumer)))
