from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer


class MealsList(APIView):
    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealPK(APIView):
    def get(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(pk=kwargs["pk"])
            serializer = MealSerializer(meal)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Meal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(pk=kwargs["pk"])
            serializer = MealSerializer(instance=meal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Meal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(pk=kwargs["pk"])
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Meal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RatingList(APIView):
    def get(self, request, *args, **kwargs):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingPK(APIView):
    def get(self, request, *args, **kwargs):
        try:
            rate = Rating.objects.get(pk=kwargs["pk"])
            serializer = RatingSerializer(rate)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            rate = Rating.objects.get(pk=kwargs["pk"])
            serializer = RatingSerializer(instance=rate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            rate = Rating.objects.get(pk=kwargs["pk"])
            rate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Rating.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
