# Content of app_name/wagtail_hooks.py
from compressor.css import CssCompressor
from django.templatetags.static import static
from wagtail import hooks
from django.conf import settings
from django.utils.html import format_html


@hooks.register("insert_global_admin_css")
def import_fontawesome_stylesheet():
    elem = '<link rel="stylesheet" type="text/x-scss" href="{}scss/fontawesome.scss">'.format(
        settings.STATIC_URL
    )
    compressor = CssCompressor("css", content=elem)
    output = ""
    for s in compressor.hunks():
        output += s
    return format_html(output)

@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/js/admin/easymde_custom.js to the admin."""
    return format_html('<script src="{}"></script>', static("js/easymde_custom.js"))