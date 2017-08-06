import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)

print(octets)

city = 'São Paulo'
print(city.encode('utf_8'))

print(city.encode('utf_16'))

print(city.encode('iso8859_1'))

print(city.encode('cp437'))

city = 'São Paulo'

print(city.encode('cp437', errors='ignore'))

print(city.encode('cp437', errors='replace'))

print(city.encode('cp437', errors='xmlcharrefreplace'))

octet = b'Montr\xe9al'
print(octet.decode('cp1252'))

print(octet.decode('iso8859_7'))

print(octet.decode('koi8_r'))

print(octet.decode('utf_8'))

