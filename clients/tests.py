from django.test import TestCase
from common.models import *
from clients.models import Account
from django.contrib.auth.models import User


# Create your tests here.


class AccountCreateTest(object):
    def setUp(self):
        self.country = Country.objects.create(
            iso_3166_1_a2="IN", iso_3166_1_a3="IND", iso_3166_1_numeric="01", printable_name="INDIA", name="INDIA", is_shipping_country="True")
        self.address = Address.objects.create(
            street="KPHB", city="HYDERABAD", state="ANDHRA PRADESH", postcode="500073", country=Country.objects.get(pk=1))
        self.account = Account.objects.create(
            name="Uday", email="udayteja@micropyramid.com", phone="8333855552", billing_address=self.address,
            shipping_address=self.address, website="www.uday.com", account_type="PARTNER",
            sis_code="UDAYMP2016", industry="SOFTWARE", description="Yes.. Testing Done")
        self.user = User.objects.create(username='uday')
        self.user.set_password('uday2293')
        self.user.save()
        self.client.login(username='uday', password='uday2293')


class clientsCreateUrlTestCase(AccountCreateTest, TestCase):
    def test_account_create_url(self):
        response = self.client.get('/clients/create/', {
            'name': "Uday", 'email': "udayteja@micropyramid.com", 'phone': "", 'billing_address': self.address,
            'shipping_address': self.address, 'website': "www.uday.com", 'account_type': "PARTNER",
            'sis_code': "UDAYMP2016", 'industry': "SOFTWARE", 'description': "Yes.. Testing Done"})
        self.assertEqual(response.status_code, 200)

    def test_account_create_html(self):
        response = self.client.get('/clients/create/', {
            'name': "Uday", 'email': "udayteja@micropyramid.com", 'phone': "", 'billing_address': self.address,
            'shipping_address': self.address, 'website': "www.uday.com", 'account_type': "PARTNER",
            'sis_code': "UDAYMP2016", 'industry': "SOFTWARE", 'description': "Yes.. Testing Done"})
        self.assertTemplateUsed(response, 'clients/create_account.html')


class AccountCreateTestCase(AccountCreateTest, TestCase):
    def test_account_create(self):
        self.assertEqual(self.account.id, 1)


class clientsListTestCase(AccountCreateTest, TestCase):
    def test_clients_list(self):
        self.clients = Account.objects.all()
        response = self.client.get('/clients/list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clients/clients.html')


class clientsCountTestCase(AccountCreateTest, TestCase):
    def test_clients_list_count(self):
        count = Account.objects.all().count()
        self.assertEqual(count, 1)


class clientsViewTestCase(AccountCreateTest, TestCase):
    def test_clients_view(self):
        self.clients = Account.objects.all()
        response = self.client.get('/clients/1/view/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['ac'].id, 1)
        self.assertTemplateUsed(response, 'clients/view_account.html')


class clientsRemoveTestCase(AccountCreateTest, TestCase):
    def test_clients_remove(self):
        # self.account_del = Account.objects.filter(id=1).delete()
        response = self.client.get('/clients/1/delete/')
        self.assertEqual(response['location'], '/clients/list/')

    def test_clients_remove_status(self):
        Account.objects.filter(id=self.account.id).delete()
        response = self.client.get('/clients/list/')
        self.assertEqual(response.status_code, 200)


class clientsUpdateUrlTestCase(AccountCreateTest, TestCase):
    def test_clients_update(self):
        response = self.client.get('/clients/1/edit/', {
            'name': "Uday", 'email': "udayteja@micropyramid.com", 'phone': "8333855552", 'billing_address': self.address,
            'shipping_address': self.address, 'website': "www.uday.com", 'account_type': "PARTNER",
            'sis_code': "UDAYMP2016", 'industry': "SOFTWARE", 'description': "Yes.. Testing Done"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clients/create_account.html')

    def test_clients_update_status(self):
        response = self.client.get('/clients/1/edit/')
        self.assertEqual(response.status_code, 200)

    def tst_clients_update_html(self):
        response = self.client.get('/clients/1/edit/')
        self.assertTemplateUsed(response, 'clients/create_account.html')


class AccountCreateEmptyFormTestCase(AccountCreateTest, TestCase):

    def test_account_creation_invalid_data(self):
        data = {'name': "", 'email': "", 'phone': "", 'billing_address': self.address, 'shipping_address': self.address,
                'website': "", 'account_type': "", 'sis_code': "", 'industry': "", 'description': ""}
        response = self.client.post('/clients/create/', data)
        self.assertEqual(response.status_code, 200)
