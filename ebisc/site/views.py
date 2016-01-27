# -*- coding: utf-8 -*-

import os

import django.shortcuts
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.core.urlresolvers import reverse


# -----------------------------------------------------------------------------
# Menu

class Menu(object):

    @staticmethod
    def active(item, path):
        if item == '/':
            return path == item
        else:
            return path.startswith(unicode(item))

    def __init__(self, items, path):
        self.menu = ({'path': item[0], 'title': item[1], 'active': Menu.active(item[0], path)} for item in items)

    def __iter__(self):
        return self.menu


# -----------------------------------------------------------------------------
# Document

def get_menu(request):

    path = request.path

    if request.user.has_perm('auth.can_view_executive_dashboard'):
        MENU = (
            (reverse('search:search'), 'Cell Line Catalogue'),
            (reverse('executive:dashboard'), 'Executive Dashboard'),
        )
    else:
        MENU = (
            (reverse('search:search'), 'Cell Line Catalogue'),
        )

    return Menu(MENU, path)


def document(request, path):

    path = 'site/' + path
    return render(request, os.path.join(path.encode('ascii', 'ignore'), 'index.html'))


def render(request, path, context={}):

    menu = get_menu(request)

    context.update({
        'path': path,
        'menu': menu,
    })

    try:
        return django.shortcuts.render(request, path, context)
    except TemplateDoesNotExist:
        raise Http404


# -----------------------------------------------------------------------------
