from ..models import Version


class CheckVersion:
    def __init__(self, user_id):
        self.user_id = user_id

    def mode(self):
        version = Version.objects.filter(user=self.user_id).first()
        return version.mode if version else None

    def use_count(self):
        version = Version.objects.filter(user=self.user_id).first()
        return version.use_count if version else None


def add_count(version):
    version.use_count += 1  # Increment use_count
    version.save()  # Save the updated object