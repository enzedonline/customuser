from django.utils import translation
from django.urls import reverse

from django.conf import settings
from django.test import Client, RequestFactory, TestCase
from wagtail.core.models import Page, Site
from wagtailtrans.models import Language, TranslatablePage

from .factories import (ArticleIndexPageFactory, ArticlePageFactory,
                        HomePageFactory)
from ..views import *                        


class TestChangeLanguageViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.factory = RequestFactory()
        cls.site = Site.objects.create(is_default_site=True, root_page=Page.get_first_root_node())
        cls.homepage = HomePageFactory()
        cls.articleindexpage = ArticleIndexPageFactory(parent=cls.homepage)
        cls.articlepage1 = ArticlePageFactory(parent=cls.articleindexpage)
        cls.foreign_language_code = [code for code, lang in settings.LANGUAGES if code != settings.LANGUAGES[0][0]][0]
        # note: Wagtailtrans automatically creates a language tree for every language that is defined
        cls.foreign_language = Language.objects.get_or_create(code=cls.foreign_language_code)[0]
        cls.foreign_articlepage1 = TranslatablePage.objects.get(language=cls.foreign_language,
                                                              canonical_page=cls.articlepage1)

    def test_change_language_without_previous_page(self):
        translation.activate(settings.LANGUAGES[0][0])
        set_language_url = reverse('set_language_from_url', kwargs={'language_code': self.foreign_language_code})
        response = self.client.get(set_language_url)
        expected_url = '/' + self.foreign_language_code + '/'
        self.assertEquals(response.url, expected_url)

    def test_change_language_of_login_url(self):
        # get the url from the get_language_from_url view and make a request object
        url = reverse('set_language_from_url', kwargs={'language_code': self.foreign_language_code})
        request = self.factory.get(url)

        # manually set the HTTP_REFERER value to login url  
        request.META['HTTP_REFERER'] = '/' + settings.LANGUAGES[0][0] + '/accounts/login/'
        translation.activate(settings.LANGUAGES[0][0])
        response = set_language_from_url(request, self.foreign_language_code)
        expected_url = '/' + self.foreign_language_code + '/accounts/login/'
        self.assertEquals(response.url, expected_url)

    def test_change_language_from_canonical_page(self):
        # get the url, make a request object and set the HTTP_REFERER
        url = reverse('set_language_from_url', kwargs={'language_code': self.foreign_language_code})
        request = self.factory.get(url)
        request.META['HTTP_REFERER'] = str(self.articlepage1.url)
        translation.activate(settings.LANGUAGES[0][0])
        response = set_language_from_url(request, self.foreign_language_code)
        self.assertEqual(response.url, self.foreign_articlepage1.url)