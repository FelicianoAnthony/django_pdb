from rest_framework import mixins, generics
from .models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404

class StatusListView(
    generics.ListAPIView, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin):

    # this overrides settings.py authentication make you not have to pass token to view this 


    queryset = Status.objects.all() 
    serializer_class = StatusSerializer

    def get_queryset(self):
        """
        query your actual dataabse from an endpoint -- status/?q=2
        """
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        #import pdb; pdb.set_trace()
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
        #import pdb; pdb.set_trace()
        #return Status.objects.filter(id=3)

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        


        #import pdb; pdb.set_trace()
        obj=None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
        return obj
        #import pdb; pdb.set_trace()
        #return Status.objects.filter(id=3)


    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    def delete(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        return self.destroy(request, *args, **kwargs)