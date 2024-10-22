from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from habits.models import Habits
from habits.paginators import ListViewPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


# Create your views here.
class HabitCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        owner = serializer.save()
        owner.user = self.request.user
        owner.save()


class HabitListApiView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = ListViewPaginator

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitPublicListApiView(ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitSerializer


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
