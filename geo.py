import geoip2.database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

file = open('finalsql.txt', "r", encoding="UTF-8")
lines = file.readlines()

for line in lines:
    line = line.strip()
    iso_code1 = reader.country(line).country.iso_code
    iso_code2 = reader.country(line).country.name
    print(iso_code1, iso_code2)