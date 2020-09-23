from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def like_numbers(context, likers, followers):
    # print(f"likers: {likers}")
    print(f"followers: {followers}")
    numbers = likers.count()
    # print(numbers)
    if not likers:
        return ""
    else:
        for num, liker in enumerate(likers):
            if followers:
                if liker in followers and num == 1:
                    return f"Liked by {liker} and other {numbers-1}"

        return f"{numbers} likes"
