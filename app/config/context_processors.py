from django.contrib.sites.shortcuts import get_current_site


def contexts(request):
    site = get_current_site(request)
    base_url = f'https://{site.domain}'
    path_url = f'{base_url}{request.path}'
    context = {
        'base_url': base_url,
        'path_url': path_url,
    }
    return context
