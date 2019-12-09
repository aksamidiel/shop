from django.urls import path
from comments.views import *

urlpatterns = [
    path('comment-create', CommentCreate.as_view(), name='comment-create')
]