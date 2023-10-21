from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from.models import Worker, Store, Visit
from.serializers import WorkerSerializer, StoreSerializer, VisitSerializer


class StoreAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.worker = Worker.objects.create(name='John Doe', phone_number='1234567890')
        self.store = Store.objects.create(name='Store 1', worker=self.worker)
        self.visit = Visit.objects.create(store=self.store, latitude=1.0, longitude=1.0)

    def test_create_store(self):
        url = '/stores/'
        data = {'name': 'Store 2', 'worker': self.worker.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Store.objects.count(), 2)

    def test_retrieve_store(self):
        url = f'/stores/{self.store.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.store.name)
        self.assertEqual(response.data['worker'], self.store.worker.pk)

    def test_update_store(self):
        url = f'/stores/{self.store.pk}/'
        data = {'name': 'Store 2', 'worker': self.worker.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.store.refresh_from_db()
        self.assertEqual(self.store.name, 'Store 2')
        self.assertEqual(self.store.worker, self.worker)

    def test_delete_store(self):
        url = f'/stores/{self.store.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Store.objects.count(), 0)

        # Проверяем, что посещения, связанные с удаляемой торговой точкой, также удаляются
        self.assertEqual(Visit.objects.count(), 0)


# тест для просмотра и поиска посещений
class VisitAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.worker = Worker.objects.create(name='John Doe', phone_number='1234567890')
        self.store = Store.objects.create(name='Store 1', worker=self.worker)
        self.visit = Visit.objects.create(store=self.store, latitude=1.0, longitude=1.0)

    def test_list_visits(self):
        url = '/visits/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_visits_by_worker_name(self):
        url = f'/visits/?worker_name={self.worker.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_visits_by_store_name(self):
        url = f'/visits/?store_name={self.store.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

# тест для создания, редактирования и удаления посещений
class VisitAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.worker = Worker.objects.create(name='John Doe', phone_number='1234567890')
        self.store = Store.objects.create(name='Store 1', worker=self.worker)
        self.visit = Visit.objects.create(store=self.store, latitude=1.0, longitude=1.0)

    def test_create_visit(self):
        url = '/visits/'
        data = {'store': self.store.pk, 'latitude': 2.0, 'longitude': 2.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Visit.objects.count(), 2)

    def test_retrieve_visit(self):
        url = f'/visits/{self.visit.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['store'], self.visit.store.pk)
        self.assertEqual(response.data['latitude'], self.visit.latitude)
        self.assertEqual(response.data['longitude'], self.visit.longitude)

    def test_update_visit(self):
        url = f'/visits/{self.visit.pk}/'
        data = {'store': self.store.pk, 'latitude': 2.0, 'longitude': 2.0}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.visit.refresh_from_db()
        self.assertEqual(self.visit.store, self.store)
        self.assertEqual(self.visit.latitude, 2.0)
        self.assertEqual(self.visit.longitude, 2.0)

    def test_delete_visit(self):
        url = f'/visits/{self.visit.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Visit.objects.count(), 0)
