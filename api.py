import hashlib
import psycopg2
import pprint

api_keys = [
]

query = """
select ua.email, r.name, ak.key
from api_key ak
join user_account ua on ak.owner_id = ua.id
join user_role ur on ua.id = ur.user_id
join role r on ur.role_id = r.id
where ak.key = '{}';
"""

api_objs = []

for k in api_keys:
    api_objs.append({
        'api_key': k,
        'encrypted_key': hashlib.sha256(k.encode()).hexdigest()
    })
# encrypted_keys = [hashlib.sha256(key.encode()).hexdigest() for key in api_keys]

# Connect to dev db
conn = psycopg2.connect(
    host="",
    port=,
    database="",
    user="",
    password="")
cursor = conn.cursor()

for o in api_objs:
    o_query = query.format(o['encrypted_key'])
    cursor.execute(o_query)
    data = cursor.fetchall()
    o['email'] = data[0][0]
    o['roles'] = [d[1] for d in data]

pprint.pprint(api_objs)

my_query = """
select ua.email, r.name
from user_account ua
join user_role ur on ua.id = ur.user_id
join role r on ur.role_id = r.id
where ua.email like 'sarah.perlotto%'
order by ua.email;
"""

cursor.execute(my_query)
data = cursor.fetchall()

my_roles = {}
for d in data:
    perms = my_roles.get(d[0], [])
    perms.append(d[1])
    my_roles[d[0]] = perms

pprint.pprint(my_roles)

conn.close()
