import subprocess
from datetime import datetime

services = [
    'account',
    'admin',
    'alert',
    'analytics',
    'c2-attribution',
    'category',
    'cert',
    'config',
    'confront-counts',
    'devicegeo',
    'dns',
    'dns-log-report',
    'dynamicdns',
    'ipinfo',
    'malware',
    'os_indicators',
    'passivedns',
    'passivehash',
    'protect-agent',
    'protect-count',
    'protect-data',
    'protect-decision',
    'protect-reputation',
    'screenshot',
    'search',
    'sinkhole',
    'userdata',
    'whois'
]

command_template = 'pushd /Users/sarah/src/{}; git log src/main/resources/application.yml'
date_start = 'Date:   '
date_end = '\\n\\n'
date_format = '%a %b %d %H:%M:%S %Y %z'
config_changes_made = datetime.strptime('Thu Jun 22 12:49:45 2023 -0700', date_format)

for service in services:
    command = command_template.format(service)
    output = str(subprocess.run(command, shell=True, capture_output=True).stdout)
    # print(output)

    # Find date in output
    date_start_offset = output.find(date_start) + len(date_start)
    date_end_offset = (output[date_start_offset:]).find(date_end) + date_start_offset
    last_config_update = datetime.strptime(output[date_start_offset:date_end_offset], date_format)
    # print('Config for {} last updated {}'.format(repo, last_config_update))

    if last_config_update > config_changes_made:
        print('Update config for {} (last updated {}, config migration {})'.format(service, last_config_update,
                                                                                   config_changes_made))


