from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def like_numbers(context, likers, followers):

    numbers = likers.count()
    if not likers:
        return ""
    else:
        for num, liker in enumerate(likers):
            if liker in followers and num == 1:
                return f"Liked by {liker} and other {numbers-1}"

        return f"{numbers} likes"
