from django.shortcuts import render
from mealplanapp.models import UserAccount, MealPlan, EachDayMealTable
from mealplanapp.serializers import UserAccountSerializer, MealPlanSerializer, EachDayMealTableSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist


@api_view(["POST"])
def create_user_account(request):
    payload = request.data
    check_username = UserAccount.objects.filter(userName=payload["userName"])
    if len(check_username) > 0:
        raise ValidationError("username already taken, try other usernames")
    serializer = UserAccountSerializer(data=payload)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)
    return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_user_accounts(request):
    query = UserAccount.objects.filter(isActive=True)
    serializer = UserAccountSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if username is None:
        raise ValidationError("username cannot be none")
    if password is None:
        raise ValidationError("password cannot be none")
    query = UserAccount.objects.filter(userName=username)
    if len(query) == 0:
        raise ValidationError("user does not exist")
    if password != query[0]["password"]:
        raise ValidationError("password is wrong, please check")
    else:
        return Response(True, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_meal_plan(request):
    payload = request.data
    serializer = MealPlanSerializer(data=payload)
    serializer.is_valid(raise_exception=True)
    serializer.create(serializer.validated_data)
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def list_user_meal_plans(request):
    username = request.data.get("username")
    query = MealPlan.objects.filter(userId=username)
    serializer = MealPlanSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_meal_plan(request, _id):
    query = MealPlan.objects.get(id=_id)
    query.delete()
    return Response(data={"Meal Plan deleted"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_meal_plan(request, _id):
    query = MealPlan.objects.get(id=_id)
    serializer = MealPlanSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.update(query, request.data)
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(["POST", "GET"])
def create_each_day_meal_plan(request):
    if request.method == "POST":
        payload = request.data
        serializer = EachDayMealTableSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_each_day_meal_plan(request, _id):
    query = EachDayMealTable.objects.filter(userId=_id)
    serializer = EachDayMealTableSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_each_meal_plan(request, _id):
    query = EachDayMealTable.objects.get(id=_id)
    query.delete()
    return Response(data={"Meal Plan deleted"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_each_meal_plan(request, _id):
    query = EachDayMealTable.objects.get(id=_id)
    serializer = EachDayMealTableSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.update(query, request.data)
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


def template_login(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    try:
        query = UserAccount.objects.get(userName=username)
    except ObjectDoesNotExist:
        return render(request, 'mealplanapp/userexisterror.html')
    if password == query.password:
        query = MealPlan.objects.filter(userId=username)
        context = {
            "data": query,
            "user": username
        }
        return render(request, 'mealplanapp/mydailymealplan.html', context=context)
    else:
        return render(request, 'mealplanapp/loginerror.html')


def load_login_page(request):
    return render(request, 'mealplanapp/login.html')


def load_calorie_page(request):
    payload = request.POST
    start_date = payload.get("startdate")
    end_date = payload.get("enddate")
    username = payload.get("user")
    query = EachDayMealTable.objects.filter(date__gte=start_date, date__lte=end_date, userId=username)
    _meal_query = MealPlan.objects.filter(startDate__gte=start_date, userId=username)
    per_day_calorie = _meal_query[0].perDayCalories
    # for data in query:
    #     if data.caloriesInTaken > per_day_calorie:
    #         data["check"] = True
    #     else:
    #         data["check"] = False
    context = {
        "data": query,
        "perDayCalories": per_day_calorie
    }
    return render(request, 'mealplanapp/caloriedetailpage.html', context=context)
