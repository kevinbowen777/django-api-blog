from django.test import TestCase

from accounts.tests.factories import UserFactory

from .factories import PostFactory

# from ..models import Post


class PostTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory()

    def test__str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    """
    def test_get_absolute_url(self):
        url = self.post.get_absolute_url()
        assert url == f"/posts/{self.post.id}/"
    """


"""
class BlogTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="blogreader", password="T3stP@s5123"
        )

        cls.post = Post.objects.create(
            author=cls.user, title="Blog title", body="Nice Body content..."
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "blogreader")
        self.assertEqual(title, "Blog title")
        self.assertEqual(body, "Nice Body content...")

    def test__str__(self):
        post = Post.objects.get(id=1)
        assert post.__str__() == post.title
        assert str(post) == post.title

    def test_api_listview(self):
        self.client.login(username="blogreader", password="T3stP@s5123")
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        # self.assertContains(response, self.post)

    def test_api_logged_out_deny_listview_access(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_detailview(self):
        self.client.login(username="blogreader", password="T3stP@s5123")
        response = self.client.get(
            reverse("post_detail", kwargs={"pk": self.post.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, "Nice Body content...")
"""
