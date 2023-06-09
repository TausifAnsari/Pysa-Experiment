# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.utils.decorators import classonlymethod

class ContextMixin:
    extra_context = None
    def get_context_data(self, **kwargs): ...

class View:
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
        "head",
        "options",
        "trace",
    ]
    def __init__(self, **kwargs): ...
    @classonlymethod
    def as_view(cls, **initkwargs): ...
    def setup(self, request, *args, **kwargs): ...
    def dispatch(self, request, *args, **kwargs): ...
    def http_method_not_allowed(
        self, request, *args, **kwargs
    ) -> HttpResponseNotAllowed: ...
    def options(self, request, *args, **kwargs) -> HttpResponse: ...

class TemplateResponseMixin:
    template_name = None
    template_engine = None
    response_class = TemplateResponse
    content_type = None
    def render_to_response(self, context, **response_kwargs): ...
    def get_template_names(self): ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs) -> HttpResponse: ...

class RedirectView(View):
    permanent = False
    url = None
    pattern_name = None
    query_string = False
    def get_redirect_url(self, *args, **kwargs) -> str: ...
    def get(self, request, *args, **kwargs) -> HttpResponse: ...
    def head(self, request, *args, **kwargs) -> HttpResponse: ...
    def post(self, request, *args, **kwargs) -> HttpResponse: ...
    def options(self, request, *args, **kwargs) -> HttpResponse: ...
    def delete(self, request, *args, **kwargs) -> HttpResponse: ...
    def put(self, request, *args, **kwargs) -> HttpResponse: ...
    def patch(self, request, *args, **kwargs) -> HttpResponse: ...
