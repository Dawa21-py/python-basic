person = {
    "name": "Ram",
    "age": 2,
    "gender": "male",
    "address": "hyd",
    "phone": 9876543210,
    "hobbies": [
        "singing",
        "dancing",
    ],
    "fav_movies": [
        "3 idiots",
        "3 idiots 2",
        "3 idiots 3",
    ],
    "friends": [
          {
            "name": "Shyam",
            "age": 3,
            "gender": "male",
            "address": "hyd",
            "phone": 9876543210,
            "hobbies": [
                "singing",
                "dancing",
            ],
            "fav_movies": [
                "3 idiots",
                "3 idiots 2",
                "3 idiots 3",
            ],
        },
    ]
}
print(person["friends"])
print(person["friends"][0]["name"])