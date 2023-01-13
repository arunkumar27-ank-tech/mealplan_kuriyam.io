from django.urls import path
from mealplanapp.views import create_user_account, list_user_accounts, login, template_login, load_login_page, \
    create_meal_plan, list_user_meal_plans, delete_meal_plan, update_meal_plan, create_each_day_meal_plan, \
    update_each_meal_plan, delete_each_meal_plan, get_each_day_meal_plan, load_calorie_page

urlpatterns = [
    path('login/', login),
    path('create/', create_user_account),
    path('list/', list_user_accounts),
    path('meal-list/', list_user_meal_plans),
    path('delete/meal/<str:_id>/', delete_meal_plan),
    path('update/meal/<str:_id>', update_meal_plan),
    path('create-daily/meal/', create_each_day_meal_plan),
    path('get/meal-plan/<str:_id>', get_each_day_meal_plan),
    path('daily/delete/meal/<str:_id>/', delete_each_meal_plan),
    path('daily/update/meal/<str:_id>', update_each_meal_plan),
    path('template/login/', template_login, name='login'),
    path('load/login-page/', load_login_page, name='pagelogin'),
    path('meal/create/', create_meal_plan),
    path('load/calorie/', load_calorie_page, name='loadcalorie')
]
