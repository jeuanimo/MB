"""
Views for the main application
"""
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse


class HomeView(TemplateView):
    """
    Home page view using TemplateView
    """
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Welcome to My Django Project',
            'message': 'Your Django project is set up and ready to go!',
        })
        return context


class AboutView(TemplateView):
    """
    About page view using TemplateView
    """
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About Us',
            'description': 'Learn more about our Django project and what we do.',
            'features': [
                {
                    'title': 'Modern Framework',
                    'description': 'Built with Django, a high-level Python web framework.',
                    'icon': 'bi-code-slash'
                },
                {
                    'title': 'Responsive Design',
                    'description': 'Mobile-first design with Bootstrap for all devices.',
                    'icon': 'bi-phone'
                },
                {
                    'title': 'Secure & Scalable',
                    'description': 'Enterprise-grade security and scalability features.',
                    'icon': 'bi-shield-check'
                }
            ]
        })
        return context


class HealthCheckView(View):
    """
    Simple health check endpoint using View
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK', status=200)


# Keep function-based views for backward compatibility (optional)
def index(request):
    """
    Home page view (function-based - for compatibility)
    """
    view = HomeView.as_view()
    return view(request)


def about(request):
    """
    About page view (function-based - for compatibility)
    """
    view = AboutView.as_view()
    return view(request)


def health_check(request):
    """
    Simple health check endpoint (function-based - for compatibility)
    """
    view = HealthCheckView.as_view()
    return view(request)