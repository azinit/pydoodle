class SceneMananger(object):
    def __init__(self):
        from core.examples.scene_demo.core.scenes import TitleScene
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
