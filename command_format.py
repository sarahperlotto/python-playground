objects = """
_confluent-ksql-default__command_topic
default_ksql_processing_log
dev_beacon_c2
dev_beacon_email
dev_device_geo
dev_device_geo_nearby
dev_dns_resolution_whois_answer
dev_indicator
dev_os_indicators
dev_sinkhole
dev_whois
dev_whois_related_nameserver
dev_whois_related_pii
device_geo_missing
device_geo_nearby_device_missing
prd_device_geo
prd_device_geo_nearby
prd_device_geo_nearby_device
prd_dns_resolution_answer
prd_dns_resolution_ddns
prd_dns_resolution_ddns_answer
prd_dns_resolution_indicator
prd_dns_resolution_whois
prd_dns_resolution_whois_answer
prd_indicator
prd_iot_indicator
prd_os_indicators
prd_sinkhole
prd_test
prd_whois
prd_whois_related_nameserver
prd_whois_related_pii
sanity-check
""".split()
commands = ['/opt/kafka_2.12-2.2.0/bin/kafka-topics.sh --bootstrap-server 10.50.10.10:9092 --delete --topic {}'.format(o) for o in objects]

print(*commands, sep='\n')
