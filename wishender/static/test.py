blabla = {
    "Listen": [
        {"Liste 01": {
             "Ball": "12.5 CHF",
             "DVD": "7 CHF"
                    },
        }
    ]
}

# for id, data, in blabla["Listen"]:
# print(id)
# print(data)


for data in blabla["Listen"]:
    print(data.keys())
    for data in data.values():
       print(data)
