def username(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return {'username': username}
