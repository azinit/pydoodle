from core.mixins import SingletonMixin
from core.modules import JsonStream


# TODO: Multiple?
class UserInitializer(SingletonMixin):
    DEFAULT_INFO_PATH = "user_info.json"

    def __init__(self, **props):
        self.path = props.get("path", self.DEFAULT_INFO_PATH)
        self.data = self.load()

    def load(self):
        data = JsonStream.read(self.path)
        # for profile in profiles:
        #     if profile["player_name"] == user:
        #         return profile
        # return None
        return data

    def save(self):
        JsonStream.write(self.path, self.data)

    def update_score(self, score):
        self.data["best_score"] = score
        self.save()
