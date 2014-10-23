from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajaxprojex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pokemon.views.profile', name='profile'),
    url(r'^all_pokemon/$', 'pokemon.views.all_pokemon', name='all_pokemon'),
    url(r'^team/(?P<team_id>\w+)/view/$', 'pokemon.views.view_team', name='view_team'),
    url(r'^pokemon_data_dump/$', 'pokemon.views.pokemon_data_dump', name='pokemon_data_dump'),
    url(r'^pokemon_info/(?P<pokemon_id>\w+)/$', 'pokemon.views.pokemon_info', name='pokemon_info'),
    url(r'^new_pokemon/$', 'pokemon.views.new_pokemon', name='new_pokemon'),
    url(r'^new_team/$', 'pokemon.views.new_team', name='new_team'),
    url(r'^random/$', 'pokemon.views.random', name='random'),
    url(r'^register/$', 'pokemon.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)