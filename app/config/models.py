from django.db import models
from django.utils import timezone

__all__ = [
    'models',
    'BaseModel',
]


class BaseManager(models.Manager):
    def _get_compare_queryset(self, instance, compare_field='pk', sort='ascending'):
        order_query = '{sort}{field}'.format(
            sort='' if sort == 'ascending' else '-',
            field=compare_field
        )
        compare_value = getattr(instance, compare_field)
        sort_query = 'lt' if sort == 'ascending' else 'gt'
        filter_query = {
            '{compare_field}__{sort_query}'.format(
                compare_field=compare_field,
                sort_query=sort_query
            ): compare_value,
        }
        return self.get_queryset().order_by(order_query).filter(**filter_query)

    def get_index(self, instance, compare_field='pk', sort='ascending'):
        """
        ModelClass의 objects를 compare_field를 기준으로 정렬하여,
        인자로 주어진 instance가 정렬기준 몇 번째에 해당하는지 리턴
        index이므로 0부터 시작하며, 1부터 시작하는 값이 필요할경우 +1 하여 사용
        :param instance: 기준이 되는 인스턴스
        :param compare_field: 정렬기준이 되는 필드명
        :param sort: 오름/내림차순(기본: ascending, 내림차순: descending)
        :return: 몇 번째인지 나타내는 index
        """
        return self._get_compare_queryset(instance, compare_field, sort).count()

    def get_range_queryset(self, instance, compare_field='pk', sort='ascending', range=3):
        index = self.get_index(instance, compare_field, sort)
        return self._get_compare_queryset(instance, compare_field, sort)[index-range:index+range+1]


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = BaseManager()

    class Meta:
        abstract = True
