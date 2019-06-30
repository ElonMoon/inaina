def contexts(request):
    base_url = '{scheme}://{http_host}'.format(
        scheme=request.scheme,
        http_host=request.META['HTTP_HOST']
    )
    path_url = '{base_url}{path_url}'.format(
        base_url=base_url,
        path_url=request.path,
    )
    context = {
        'base_url': base_url,
        'path_url': path_url,
    }
    return context
