restaurant_object1 = {
    "id": 1,
    "name": "Vikings Luxury Buffet",
    "location": "Pasay City",
    "cuisine_type": "Buffet",
    "established_year": 2011,
    "website_or_contact": "www.vikings.ph"
}


restaurant_object2 = {
    "id": 2,
    "name": "Antonio's Restaurant",
    "location": "Tagaytay",
    "cuisine_type": "Fine Dining",
    "established_year": 2002,
    "website_or_contact": "www.antoniosrestaurant.ph"
}


restaurant_object3 = {
    "id": 3,
    "name": "Mesa Filipino Moderne",
    "location": "Makati City",
    "cuisine_type": "Filipino",
    "established_year": 2009,
    "website_or_contact": "www.mesa.ph"
}


restaurant_object4 = {
    "id": 4,
    "name": "Manam Comfort Filipino",
    "location": "Quezon City",
    "cuisine_type": "Filipino",
    "established_year": 2013,
    "website_or_contact": "www.manam.ph"
}


restaurant_object5 = {
    "id": 5,
    "name": "Ramen Nagi",
    "location": "Various Locations",
    "cuisine_type": "Japanese",
    "established_year": 2013,
    "website_or_contact": "www.ramennagi.com.ph"
}


restaurants = [restaurant_object1, restaurant_object2, restaurant_object3, restaurant_object4, restaurant_object5]


for restaurant in restaurants:
    print(f"ID: {restaurant['id']}, Name: {restaurant['name']}, Location: {restaurant['location']}, Cuisine Type: {restaurant['cuisine_type']}, Established Year: {restaurant['established_year']}, Website/Contact: {restaurant['website_or_contact']}")