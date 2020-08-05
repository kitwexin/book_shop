from . models import Profile

def create_profile(sender, instance, **kwargs):
    obj, created = Profile.objects.get_or_create(
        user = instance,
        defaults = {},
    )
    if created:
        print('Good!')
    else:
        print('Norm')