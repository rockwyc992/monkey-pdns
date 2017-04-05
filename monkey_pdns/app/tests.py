from django.test import TestCase
from django.contrib.auth.models import User
from .views import hello
from .models import Zone, Sub_Zone, Record, Record_Type

class View_hello_tests(TestCase):

    def test_hello(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World!')

class Record_Type_Test(TestCase):

    def setUp(self):
        Record_Type.objects.create(name="A")

    def test_record_type(self):
        created_a = Record_Type.objects.get(name="A")
        self.assertEqual(str(created_a), "A")


class Zone_Test(TestCase):

    def setUp(self):
        Zone.objects.create(name="test.domain.com.")

    def test_zone(self):
        created_zone = Zone.objects.get(name="test.domain.com.")
        self.assertEqual(str(created_zone), "test.domain.com.")

class Sub_Zone_Test(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test")
        self.zone = Zone.objects.create(name="test.domain.com.")
        Sub_Zone.objects.create(owner=self.user, prefix="new", super_zone=self.zone)

    def test_sub_zone(self):
        created_sub_zone = Sub_Zone.objects.get(owner=self.user, prefix="new", super_zone=self.zone)
        self.assertEqual(str(created_sub_zone), "new.test.domain.com.")

class Record_Test(TestCase):

    def setUp(self):
        self.record = Record_Type.objects.create(name="A")
        self.user = User.objects.create_user(username="test_user", password="test")
        self.zone = Zone.objects.create(name="test.domain.com.")
        self.sub_zone = Sub_Zone.objects.create(owner=self.user, prefix="new", super_zone=self.zone)
        Record.objects.create(prefix="www", type=self.record, zone=self.sub_zone, context="140.115.50.58")

    def test_record(self):
        created_record = Record.objects.get(zone=self.sub_zone)
        self.assertEqual(str(created_record), "www.new.test.domain.com. A 140.115.50.58")
