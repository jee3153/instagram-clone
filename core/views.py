from django.shortcuts import render


def guest_user(username):
    return "Guest user" in username
