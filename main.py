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

print(travel_log)

