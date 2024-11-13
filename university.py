
university_object1 = {
    "id": 1,
    "name": "University of the Philippines",
    "location": "Quezon City",
    "established_year": 1908,
    "type": "Public",
    "website": "www.up.edu.ph"
}


university_object2 = {
    "id": 2,
    "name": "Ateneo de Manila University",
    "location": "Quezon City",
    "established_year": 1859,
    "type": "Private",
    "website": "www.ateneo.edu"
}


university_object3 = {
    "id": 3,
    "name": "De La Salle University",
    "location": "Manila",
    "established_year": 1911,
    "type": "Private",
    "website": "www.dlsu.edu.ph"
}


university_object4 = {
    "id": 4,
    "name": "University of Santo Tomas",
    "location": "Manila",
    "established_year": 1611,
    "type": "Private",
    "website": "www.ust.edu.ph"
}


university_object5 = {
    "id": 5,
    "name": "Polytechnic University of the Philippines",
    "location": "Manila",
    "established_year": 1904,
    "type": "Public",
    "website": "www.pup.edu.ph"
}


universities = [university_object1, university_object2, university_object3, university_object4, university_object5]


for university in universities:
    print(f"ID: {university['id']}, Name: {university['name']}, Location: {university['location']}, Established Year: {university['established_year']}, Type: {university['type']}, Website: {university['website']}")


    