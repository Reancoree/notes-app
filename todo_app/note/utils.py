class DataMixin:
    title = None
    h1 = None

    def get_mixin_context(self, context, **kwargs):
        context['title'] = self.title
        context['h1'] = self.h1
        context.update(**kwargs)
        return context
