from django.urls import path
from mainapp import views
from django.views.decorators.cache import cache_page
from mainapp.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('docsite/', views.DocSiteView.as_view(), name='docsite'),

    # Courses
    path('courses/',cache_page(3600)(views.CoursesListView.as_view()), name='courses'),
    # path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('news/<int:pk>/detail/', views.CourseDetailView.as_view(), name='courses_detail'),
    path('courses/feedback/', views.CourseFeedbackCreateView.as_view(), name='course_feedback'),

    # News
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/add/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/detail/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # Logs
    path('logs/', views.LogView.as_view(), name='logs_list'),
    path('logs/download/', views.LogDownloadView.as_view(), name='logs_download'),

    # path('news/<pk>', views.ListView.as_view(), name='news_detail'),
]