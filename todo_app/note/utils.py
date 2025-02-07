from django.views import View


class DataMixin(View):
    title = None
    h1 = None

    def get_mixin_context(self, context, **kwargs):
        context['title'] = self.title
        context['h1'] = self.h1
        context.update(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)
