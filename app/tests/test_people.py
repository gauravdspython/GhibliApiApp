from people import People
peo = People()

test_data = [
    {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Ashitaka",
        "age": "late teens",
        "films": [
            "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"
    }
]

def test_filmPeopleID():
    result = peo.filmPeopleID(test_data)
    assert result == {
        "0440483e-ca0e-4120-8c50-4c8cd9b965d6" : ["Ashitaka"]
    }

def test_filmPeopleID_empty():
    result = peo.filmPeopleID([])
    assert result == {}


