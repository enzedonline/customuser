from datetime import timedelta

import factory
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site as DjangoSite
from django.utils import timezone
from wagtail.core.models import Page

from ..models import *
from userauth.models import *


class ThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Theme

    name = factory.Sequence(lambda n: 'Theme number {0}'.format(n))

class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    # override the _create method, to establish parent-child relationship between pages
    @classmethod
    def _create(cls, model_class, *args, **kwargs):

        try:
            parent = kwargs.pop('parent')
        except KeyError:
            # no parent, appending page to root
            parent = Page.get_first_root_node()

        page = model_class(*args, **kwargs)
        parent.add_child(instance=page)

        return page

class HomePageFactory(PageFactory):
    class Meta:
        model = HomePage

    title = factory.Sequence(lambda n: 'Home page {0}'.format(n))

class ThemePageFactory(PageFactory):
    class Meta:
        model = ThemePage

    title = factory.Sequence(lambda n: 'Theme page {0}'.format(n))

class ThemeIndexPageFactory(PageFactory):
    class Meta:
        model = ThemeIndexPage

    title = factory.Sequence(lambda n: 'Theme Index page {0}'.format(n))

class ArticleIndexPageFactory(PageFactory):
    class Meta:
        model = ArticleIndexPage

    title = factory.Sequence(lambda n: 'Article Index page {0}'.format(n))

class ArticlePageFactory(PageFactory):
    class Meta:
        model = ArticlePage

    title = factory.Sequence(lambda n: 'Article page {0}'.format(n))
    first_published_at = factory.Sequence(lambda n: timezone.now() - timedelta(days=365-n))

    @factory.post_generation
    def themes(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for theme in extracted:
                self.themes.add(theme)

class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    title = factory.Sequence(lambda n: 'Menu {0}'.format(n))

class MenuItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MenuItem

    menu = factory.SubFactory(MenuFactory)
    
class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: 'Username{0}'.format(n))
    password = factory.Sequence(lambda n: 'Password{0}'.format(n))

class CustomCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomComment

    content_type = ContentType.objects.get_for_model(ArticlePage)
    site = DjangoSite.objects.get_current()
    page = factory.SubFactory(ArticlePageFactory)
    user = factory.SubFactory(CustomUserFactory)
    comment = factory.Sequence(lambda n: 'Comment {0}'.format(n))