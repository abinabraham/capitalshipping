from django import template
from apps.general.models import (HeaderConfig, 
        FooterOurService, Address)

register = template.Library()



@register.simple_tag(name="header_list")   # noqa: C901 too complex
def get_header(depth=None, parent=None):
    """
    Gets an annotated list from a tree branch.

    Borrows heavily from treebeard's get_annotated_list
    """
    # 'depth' is the backwards-compatible name for the template tag,
    # 'max_depth' is the better variable name.
    
    header = HeaderConfig.objects.all()[0]
    return header



@register.simple_tag(name="footer_services")   # noqa: C901 too complex
def get_footer_services(depth=None, parent=None):
    """
    Gets an annotated list from a tree branch.

    Borrows heavily from treebeard's get_annotated_list
    """
    # 'depth' is the backwards-compatible name for the template tag,
    # 'max_depth' is the better variable name.
    
    footer_services = FooterOurService.objects.all()
    return footer_services

@register.simple_tag(name="address")   # noqa: C901 too complex
def get_address(depth=None, parent=None):
    """
    Gets an annotated list from a tree branch.

    Borrows heavily from treebeard's get_annotated_list
    """
    # 'depth' is the backwards-compatible name for the template tag,
    # 'max_depth' is the better variable name.
    
    address = Address.objects.all()[0]
    return address