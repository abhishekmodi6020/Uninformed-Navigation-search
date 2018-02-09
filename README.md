# Uninformed-Navigation-search
Implements Uniform Cost Search algorithm that can find an optimal route between any two cities.
Program name is find_route.py and it will take three command line arguments as follows:

  find_route input_filename origin_city destination_city

Argument input_filename is the name of a text file such as input1.txt, that describes road connections between cities in some part of the world.
The input file has each line containing three items.
1)  city name
2)  city name
3)  distance in kilometers between the 2 cities

eg: Birmingham London 117


The last line contains the items "END OF INPUT", and that is how the program can detect that it has reached the end of the file.

Each city name will be a single word (for example, we will use New_York instead of New York), consisting of upper and lowercase letters and possibly underscores.
The code is case-sensitive.
