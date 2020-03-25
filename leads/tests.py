import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from leads.models import Lead
from leads.serializers import LeadSerializer


class LeadListCreateTestCase(APITestCase):
    url = reverse('leads:list')

    def test_create_lead(self):
        response = self.client.post(self.url, {'first_name': 'Test',
                                               'last_name': 'User',
                                               'email': 'test@user.com',
                                               'is_contacted': True,
                                               'notes': 'This is test user notes'})
        self.assertEqual(201, response.status_code)

    def test_leads_list(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class LeadDetailTestCase(APITestCase):

    def setUp(self):
        'setup for list/update/delete api test cases'
        self.lead = Lead.objects.create(first_name='Detail',
                                        last_name='Test',
                                        email='detail@user.com',
                                        is_contacted=True,
                                        notes='This is detai apis testcase')
        self.url = reverse('leads:detail', kwargs={"pk": self.lead.pk})

    def test_lead_list(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        lead_serializer_data = LeadSerializer(instance=self.lead).data
        response_data = json.loads(response.content)
        self.assertEqual(response_data, lead_serializer_data)

    def test_lead_update(self):
        response = self.client.patch(self.url, {'first_name': 'testing'})
        response_data = json.loads(response.content)
        lead = Lead.objects.get(id=self.lead.id)
        self.assertEqual(lead.first_name, response_data.get('first_name'))

    def test_lead_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(200, response.status_code)
