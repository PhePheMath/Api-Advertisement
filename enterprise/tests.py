from django.test import Client, TestCase


class ProductViewSetTestCase(TestCase):
    def setUp(cls):
        cls.response_unlogged = 'componentes/singles/core/Home.html', 200
        cls.response_without_perm_GET = '403.html', 403
        cls.response_without_perm_POST = '403.html', 403
        cls.response_policial_GET = '403.html', 403
        cls.response_policial_POST = '403.html', 403
        cls.response_superior_GET = 'componentes/shares/SelectUserPerm.html', 200
        cls.response_superior_POST = 'componentes/shares/PermForUser.html', 200

    def test_unlogged_GET(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, self.response_unlogged[1])
        self.assertTemplateUsed(response, self.response_unlogged[0])

    def test_unlogged_POST(self):
        response = self.client.post(self.url, self.context, follow=True)
        self.assertEqual(response.status_code, self.response_unlogged[1])
        self.assertTemplateUsed(response, self.response_unlogged[0])

    def test_logged_without_permission_GET(self):
        self.client.login(username=self.usuario.username, password=self.password)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, self.response_without_perm_GET[1])
        self.assertTemplateUsed(response, self.response_without_perm_GET[0])

    def test_logged_without_permission_POST(self):
        self.client.login(username=self.usuario.username, password=self.password)
        response = self.client.post(self.url, self.context, follow=True)
        self.assertEqual(response.status_code, self.response_without_perm_POST[1])
        self.assertTemplateUsed(response, self.response_without_perm_POST[0])

    def test_logged_with_policial_permission_GET(self):
        self.client.login(username=self.policial.username, password=self.password)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, self.response_policial_GET[1])
        self.assertTemplateUsed(response, self.response_policial_GET[0])

    def test_logged_with_policial_permission_POST(self):
        self.client.login(username=self.policial.username, password=self.password)
        response = self.client.post(self.url, self.context, follow=True)
        self.assertEqual(response.status_code, self.response_policial_POST[1])
        self.assertTemplateUsed(response, self.response_policial_POST[0])

    def test_logged_with_superior_permission_GET(self):
        self.client.login(username=self.superior.username, password=self.password)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, self.response_superior_GET[1])
        self.assertTemplateUsed(response, self.response_superior_GET[0])

    def test_logged_with_superior_permission_POST(self):
        self.client.login(username=self.superior.username, password=self.password)
        response = self.client.post(self.url, self.context, follow=True)
        self.assertEqual(response.status_code, self.response_superior_POST[1])
        self.assertTemplateUsed(response, self.response_superior_POST[0])
