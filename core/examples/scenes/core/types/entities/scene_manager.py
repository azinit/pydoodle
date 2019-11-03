class SceneMananger(object):
    def __init__(self):
        from core.examples.scenes.core.types.entities import TitleScene
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
