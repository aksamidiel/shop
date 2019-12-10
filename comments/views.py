from django.shortcuts import render
from django.views.generic.edit import CreateView
from comments.models import CommentProduct
from comments.forms import CommentCreateForm
from django.urls import reverse_lazy


class CommentCreate(CreateView):
    model = CommentProduct
    template_name = 'escooters/escooter_detail.html'
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse_lazy('escooters-detail-view', kwargs={'pk': self.object.commented_order.pk})
