# Menghitung jarak diantara 2 titik pada sebuah bola
import math as m

latitude_a = input("Latitude A: ")
longitude_a = input("Longitude A: ")

latitude_b = input("Latitude B: ")
longitude_b = input("Longitude B: ")

longitude_a = float(longitude_a)
latitude_a = float(latitude_a)
longitude_b = float(longitude_b)
latitude_b = float(latitude_b)


# Convert degrees into radians
rad_lat_a = m.radians(latitude_a)
rad_long_a = m.radians(longitude_a)

rad_lat_b = m.radians(latitude_b)
rad_long_b = m.radians(longitude_b)


# Difference in latitude and longitude
diff_lat = rad_lat_b - rad_lat_a
diff_long = rad_long_b - rad_long_a


# Calculate a
a = (m.sin(diff_lat / 2)) ** 2 + m.cos(rad_lat_a) * m.cos(rad_lat_b) * (m.sin(diff_long / 2)) ** 2

# Calculate c
c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

# Calculate distance
d = 6371 * c

# Hasil jarak
print("Hasil jarak: ", d, "km")