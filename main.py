# Nesting 
capitals={
  "France":"Paris",
  "Germany":"Berlin",

}

# Nesting a list in a dictionary 
travel_log={
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stutgart"],
} 
# Nest a Dictionary in Dictionary 
travel_log={
  "France":{"cities_visited":["Paris", "Lille", "Dijon"],"number_of_visits":12},
  "Germany":{"cities_visited":["Berlin", "Hamburg", "Stutgart"],"number_of_visits":5},
  
} 
# Nesting a dictionary in a list  
travel_log=[
 {
   "Country": "France",
 "cities_visited":["Paris", "Lille", "Dijon"],
 "number_of_visits":12
 },
 {
   "Country": "Germany",
   "cities_visited":["Berlin", "Hamburg", "Stutgart"],"number_of_visits":5
  },
]

# print(travel_log)

def add_new_country(country_visited,cities_visited,number_of_visits):
  new_country={}
  new_country["Country"]=country_visited
  new_country["cities_visited"]=cities_visited 
  new_country["number_of_visits"]=number_of_visits 
  travel_log.append(new_country)


add_new_country("Russia",["Moscow","Saint Petesburgh"],2) 
print(travel_log)