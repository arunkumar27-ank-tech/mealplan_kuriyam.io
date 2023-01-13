from mealplanapp.models import UserAccount, MealPlan, EachDayMealTable
from rest_framework import serializers


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.mealPlanName = validated_data["mealPlanName"]
        instance.perDayCalories = validated_data["perDayCalories"]
        instance.startDate = validated_data["startDate"]
        instance.endDate = validated_data["endDate"]
        instance.save()
        return instance


class EachDayMealTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EachDayMealTable
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.mealName = validated_data["mealName"]
        instance.caloriesInTaken = validated_data["caloriesInTaken"]
        instance.date = validated_data["date"]
        instance.save()
        return instance

