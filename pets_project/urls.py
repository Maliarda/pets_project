from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from pets.views import PetViewSet, UserViewSet

from rest_framework import permissions, routers


router = routers.DefaultRouter()
router.register(r"pets", PetViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

schema_view = get_schema_view(
    openapi.Info(
        title="Pets API",
        default_version="v1",
        description="Documentation for the Pets project",
        # terms_of_service="URL страницы с пользовательским соглашением",
        contact=openapi.Contact(email="mayefimenko@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
