from app.planets.models import Planet

def test_planets_renders_planets(client):
    #Page loads and renders cookies
    new_planet = Planet(slug='pluto', name='Pluto', diameter=2376.6)
    new_planet.save()

    response = client.get('/planets')

    assert b'Earth' in response.data


# Test not working due to a failure to import "app" 
# -> to make it work go over the testing chapter in codecookies


