from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()

TEMPLATE = template.Template('{% if is_amp %}<figure>{% endif %}<{{ tag_name }}{% if class %} class="{{ class }}"{% endif %}{% if src %} src="{{ src }}"{% endif %}{% if width %} width="{{ width }}"{% endif %}{% if height %} height="{{ height }}"{% endif %}{% if alt %} alt="{{ alt }}"{% endif %}>{% if is_amp %}</figure>{% endif %}')

VALID_TAGS = [
    'img',
    'embed',
    'video',
]

@register.simple_tag(takes_context=True)
def amp_tag(context, tag_name, *args, **kwargs):
    """
    ```
    {% amp_tag 'img' src='images/path.png' %}
    ```

    Outputs:
    ```
    <img class="blt" src="{% static 'images/benjamin_turner.png' %}" alt="Kite Hill at Gas Works Park, Seattle">
    ```
    """
    is_amp = context.get('is_amp')

    src = kwargs.get('src')
    srcset = kwargs.get('srcset')

    if not src or srcset:
        raise template.TemplateSyntaxError('amp_tag requires a src argument')

    src = staticfiles_storage.url(src)

    height= kwargs.get('height')
    width = kwargs.get('width')

    if is_amp:
        if tag_name == 'img':
            tag_name = 'amp-img'

    context = template.Context({
        'is_amp': is_amp,
        'alt': kwargs.get('alt'),
        'class': kwargs.get('class'),
        'height': height,
        'src': src,
        'tag_name': tag_name,
        'width': width,
    })

    return TEMPLATE.render(context)
