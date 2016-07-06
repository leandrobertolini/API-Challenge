
from . import BaseApiTestCase
from properties.models import Property


class GetPropertiesApiTestCase(BaseApiTestCase):

    def test_with_zero_properties(self):
        response = self.client.get('/api/v1/properties/200/')
        assert response.status_code == 404

    def test_returning_property(self):
        obj = Property.objects.create(title='teste', description='teste',
                                      bed=1, bath=3, price=10.00,
                                      squareMeters=25, cordinate_x=20,
                                      cordinate_y=40, provinces=['Guda'])
        obj.save()

        response = self.client.get('/api/v1/properties/{id}/'.format(id=obj.id))
        assert response.status_code == 200

    def test_with_many_property(self):
        obj = Property.objects.create(title='teste', description='teste',
                                      bed=1, bath=3, price=10.00,
                                      squareMeters=25, cordinate_x=20,
                                      cordinate_y=40, provinces=['Guda'])
        obj.save()

        obj = Property.objects.create(title='teste abc', description='teste abc',
                                      bed=2, bath=3, price=10.00,
                                      squareMeters=48, cordinate_x=200,
                                      cordinate_y=180, provinces=['Guda', 'lelo'])
        obj.save()

        obj = Property.objects.create(title='teste abgg', description='abgg',
                                      bed=4, bath=1, price=210.00,
                                      squareMeters=210, cordinate_x=20,
                                      cordinate_y=400, provinces=['Guda'])
        obj.save()

        response = self.client.get('/api/v1/properties/2/')
        assert response.status_code == 200
        assert response.json()['bed'] == 2
        assert response.json()['bath'] == 3
        assert response.json()['title'] == 'teste abc'
        assert response.json()['provinces'] == "['Guda', 'lelo']"


class RegisterPropertiesApiTestCase(BaseApiTestCase):

    def test_whithout_parameters(self):
        response = self.client.post('/api/v1/properties')
        assert response.status_code == 400

    def test_with_invalid_bed(self):
        payload = {'cordinate_y': 100, 'cordinate_x': 250,
                   'bed': 6, 'title': 'teste',
                   'price': 10.00, 'description': 'teste',
                   'bath': 1, 'squareMeters': 30}
        response = self.client.post('/api/v1/properties', payload)

        assert response.status_code == 400
        assert response.json()['bed'] == 'The bed must be between 1 and 5.'

    def test_with_invalid_bath(self):
        payload = {'cordinate_y': 100, 'cordinate_x': 250,
                   'bed': 4, 'title': 'teste',
                   'price': 10.00, 'description': 'teste',
                   'bath': 0, 'squareMeters': 30}
        response = self.client.post('/api/v1/properties', payload)

        assert response.status_code == 400
        assert response.json()['bath'] == 'The bath must be between 1 and 4.'

    def test_with_invalid_cordinate_y(self):
        payload = {'cordinate_y': 10000, 'cordinate_x': 250,
                   'bed': 4, 'title': 'teste',
                   'price': 10.00, 'description': 'teste',
                   'bath': 1, 'squareMeters': 30}
        response = self.client.post('/api/v1/properties', payload)

        assert response.status_code == 400
        assert response.json()['cordinate_y'] == 'The cordinate_y must be between 0 and 1000.'

    def test_with_invalid_cordinate_x(self):
        payload = {'cordinate_y': 100, 'cordinate_x': 2500,
                   'bed': 4, 'title': 'teste',
                   'price': 10.00, 'description': 'teste',
                   'bath': 1, 'squareMeters': 30}
        response = self.client.post('/api/v1/properties', payload)

        assert response.status_code == 400
        assert response.json()['cordinate_x'] == 'The cordinate_x must be between 0 and 1400.'

    def test_should_register_new_property(self):
        payload = {'cordinate_y': 100, 'cordinate_x': 250,
                   'bed': 4, 'title': 'teste',
                   'price': 10.00, 'description': 'teste',
                   'bath': 1, 'squareMeters': 30}
        response = self.client.post('/api/v1/properties', payload)

        assert response.status_code == 201
        assert response.json()['title'] == 'teste'
        assert response.json()['id']
        assert response.json()['bed'] == 4


class GetPropertiesForCordianatesApiTestCase(BaseApiTestCase):

    def test_without_properties(self):
        response = self.client.get('/api/v1/properties/cordinates/10/20/30/40/')
        assert response.status_code == 404
        assert response.json() == {u'foundProperties': 0, u'properties': []}

    def test_get_properties_for_many_provinces(self):
        obj = Property.objects.create(title='teste', description='teste',
                                      bed=1, bath=3, price=10.00,
                                      squareMeters=25, cordinate_x=200,
                                      cordinate_y=400, provinces=['Scavy'])
        obj.save()

        obj = Property.objects.create(title='teste abc', description='teste abc',
                                      bed=2, bath=3, price=10.00,
                                      squareMeters=48, cordinate_x=900,
                                      cordinate_y=180, provinces=['Gode'])
        obj.save()

        obj = Property.objects.create(title='teste abgg', description='abgg',
                                      bed=4, bath=1, price=210.00,
                                      squareMeters=210, cordinate_x=600,
                                      cordinate_y=100, provinces=['Groola', 'Scavy'])
        obj.save()

        response = self.client.get('/api/v1/properties/cordinates/100/200/400/600/')
        assert response.status_code == 200
        assert response.json()['foundProperties'] == 3

        response = self.client.get('/api/v1/properties/cordinates/100/600/400/200/')
        assert response.json()['foundProperties'] == 0

        response = self.client.get('/api/v1/properties/cordinates/100/200/400/200/')
        assert response.json()['foundProperties'] == 2
        assert 'Scavy' in response.json()['properties'][0]['provinces']
        assert 'Scavy' in response.json()['properties'][1]['provinces']

        response = self.client.get('/api/v1/properties/cordinates/400/800/600/600/')
        assert response.json()['foundProperties'] == 1
        assert 'Gode' in response.json()['properties'][0]['provinces']
