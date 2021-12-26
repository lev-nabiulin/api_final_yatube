from rest_framework import mixins, viewsets

class CustomGetOrPostViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    pass
