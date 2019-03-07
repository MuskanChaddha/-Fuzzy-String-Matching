from fuzzywuzzy import process

with open(r"d:\indian_cities_data.txt","r") as f:
    cities=f.read().split('\n')


def get_cities(query,database,limit=5):
    return process.extract(query=query,choices=database,limit=limit)

print("Enter city name")
cname = input()
r_cities=get_cities(cname,cities)
rank = r_cities[0][1]
if rank == 100:
    print(r_cities[0])
else:
    print(r_cities)
