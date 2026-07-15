def test_list_authors_endpoint(client):
    response = client.get("/api/authors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)