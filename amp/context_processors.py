def base_template(request):
    return {
        'base_template': 'base_amp.html' if request.is_amp else 'base.html',
        'is_amp': request.is_amp,
    }
