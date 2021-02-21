from movies import Movies
mov = Movies()

def test_movies_route(app, client):
    response = client.get('/movies/')
    assert response.status_code == 200

test_movies = [
     {
        "id": "45204234-adfd-45cb-a505-a8e7a676b114",
        "title": "My Neighbors the Yamadas",
        "people": [
            "https://ghibliapi.herokuapp.com/people/"
        ],
        "url": "https://ghibliapi.herokuapp.com/films/45204234-adfd-45cb-a505-a8e7a676b114"
    }
]

test_people = [
    {
        "id": "fc196c4f-0201-4ed2-9add-c6403f7c4d32",
        "name": "Haru",
        "films": [
        "https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3",
        "https://ghibliapi.herokuapp.com/films/90b72513-afd4-4570-84de-a56c312fdf81"
        ]
    }

]


expected_output = [
    {
        "id": "45204234-adfd-45cb-a505-a8e7a676b114",
        "title": "My Neighbors the Yamadas",
        "people": [],
        "url": "https://ghibliapi.herokuapp.com/films/45204234-adfd-45cb-a505-a8e7a676b114"
    }
]


def test_people_field():
    result = mov.people_field(test_movies, test_people)
    assert result == expected_output