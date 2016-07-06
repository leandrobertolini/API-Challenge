
from properties.utils import get_provinces_from_xy, get_provinces_from_all_cordinates
from rest_framework.test import APITestCase


class GetPropertiesForCordianatesApiTestCase(APITestCase):

    def test_get_provinces_from_xy(self):
        provinces = get_provinces_from_xy(x=100, y=400)
        assert len(provinces) == 1
        assert provinces == ['Scavy']

        provinces = get_provinces_from_xy(x=200, y=800)
        assert len(provinces) == 1
        assert provinces == ['Gode']

        provinces = get_provinces_from_xy(x=600, y=600)
        assert len(provinces) == 2
        assert 'Gode' in provinces
        assert 'Ruja' in provinces

        provinces = get_provinces_from_xy(x=700, y=200)
        assert len(provinces) == 1
        assert 'Groola' in provinces

        provinces = get_provinces_from_xy(x=900, y=400)
        assert len(provinces) == 1
        assert 'Nova' in provinces

        provinces = get_provinces_from_xy(x=1100, y=1000)
        assert len(provinces) == 2
        assert 'Jaby' in provinces
        assert 'Ruja' in provinces

    def test_get_provinces_from_all_cordinates(self):
        provinces = get_provinces_from_all_cordinates(ax=100, ay=200, bx=600, by=600)
        assert len(provinces) == 2
        assert 'Scavy' in provinces
        assert 'Gode' in provinces

        provinces = get_provinces_from_all_cordinates(ax=1000, ay=500, bx=600, by=600)
        assert len(provinces) == 5
        assert 'Scavy' in provinces
        assert 'Gode' in provinces
        assert 'Ruja' in provinces
        assert 'Nova' in provinces
        assert 'Groola' in provinces

        provinces = get_provinces_from_all_cordinates(ax=600, ay=200, bx=600, by=200)
        assert len(provinces) == 2
        assert 'Groola' in provinces
        assert 'Scavy' in provinces
