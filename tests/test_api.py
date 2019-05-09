async def test_health_check(client):
    resp = await client.get('/healthcheck/')
    assert resp.status == 200
    result = await resp.json()
    assert 'date' in result
