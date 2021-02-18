from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    #url(r'^sitemap.xml$', sitemap),
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include('allauth.urls')), # Creates urls like yourwebsite.com/accounts/login/
    url(r'^accounts/', include('userauth.urls')),
    url(r'^language/', include('cms.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
]