from django.test import TestCase
from rest_framework.test import APIClient
from service.models import UserProfile
from rest_framework.authtoken.models import Token

# Create your tests here.
class MatchUnittestCases(TestCase):
    @classmethod
    def setUpClass(cls):
        user = UserProfile.objects.create_user(username="user1",password="user1")
        cls.client = APIClient()
        #cls.client.login(username="user1",password="user1")
        tk = Token(user=user)
        tk.save()
        token = tk.key
        cls.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    @classmethod
    def tearDownClass(cls):
        print("logout")

    def setUp(self):
        url = "api/country/"
        c1 =  self.client.post(url,json={"name":"India"})
        c2 = self.client.post(url,json={"name":"Australia"})
        url = "api/player/"
        data = {"name":"Rohit","age":32,"gender":"male"}
        self.client.post(url,json=data)
        data = {"name":"kohli","age":33,"gender":"male"}
        self.client.post(url,json=data)
        data = {"name":"pandya","age":34,"gender":"male"}
        self.client.post(url,json=data)
    def teardown(self):
        urls = ["api/country/","api/player/"]
        for url in urls:
            c1 =  self.client.get(url)
            data = c1.json()
            for d in data:
                self.client.delete("%s%s/"%(url,d["id"]))
        
    def test_matchcreate_p(self):
        url = "/match/"
        data = {"countries":["India","Australia"],
        "players":["Rohit","kohli","pandya"]},
        resp = self.client.post(url)
        self.assertTrue(200, resp.status_code)
    def test_matchcreate_n(self):
        url = "/match/"
        data = {"countries":["India","Australia"],
        "players":["Rohit1","kohli","pandya"]},
        resp = self.client.post(url)
        self.assertTrue(400, resp.status_code)
    def test_matchcreate_n1(self):
        url = "api/match/"
        data = {"countries":["India1","Australia"],
        "players":["Rohit","kohli","pandya"]},
        resp = self.client.post(url)
        self.assertTrue(400, resp.status_code)
    def test_matchcreate_n2(self):
        url = "api/match/"
        data = {"countries":[],
        "players":["Rohit","kohli","pandya"]},
        resp = self.client.post(url)
        self.assertTrue(400, resp.status_code)
    def test_matchcreate_n3(self):
        url = "api/match/"
        data = {"countries":["India1","Australia"],
        "players":[]},
        resp = self.client.post(url)
        self.assertTrue(400, resp.status_code)