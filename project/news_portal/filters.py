from django_filters import FilterSet
from .models import Post
from django.contrib.admin import register
from django_filters import FilterSet, CharFilter, DateFilter


class NewsFilter(FilterSet):
    title_filter = CharFilter(field_name='headline', lookup_expr='icontains', label='По названию')
    author_filter = CharFilter(field_name='author__user__username', lookup_expr='icontains', label='По автору')
    time_filter = DateFilter(field_name='publication_date_and_time', lookup_expr='gt', label='Позднее даты (yyyy-mm-dd)')

    class Meta:
        model = Post
        fields = ('title_filter', 'author_filter', 'time_filter')


@register
def url_qs_filter(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url
