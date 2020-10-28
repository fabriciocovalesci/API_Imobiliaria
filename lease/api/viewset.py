from rest_framework.viewsets import ModelViewSet

from lease.models import Lease
from lease.api.serializers import LeaseSerializers


class LeaseViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializers
