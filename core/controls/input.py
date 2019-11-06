from core.controls import Control, Label


class Input(Control):
    def __init__(self, x, y, width, height, screen, **props):
        Control.__init__(self, x, y, width, height, screen, **props)
        self.label = Label("ZZZ", x, y, self.screen, **props)
        self.max_length = props.get("maxlength", 16)
        self.value = ""
        # self.state.on_focus = True

    """
    ..............................................................................................................
    ................................................ EVENT ......................................................
    ..............................................................................................................
    """

    # def handle_events(self, events):
    #     import pygame
    #     for e in events:
    #         if e.type == pygame.KEYDOWN and e.key == pygame.K_TAB:
    #             # FIXME:
    #             self.state.on_focus = True

    def on_focus(self, **props):
        import pygame
        super().on_focus()
        # FIXME: Extend
        service_keys = [
        ]

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                # TODO: Validate
                # if e.key not in service_keys:
                if e.key == pygame.K_a:
                    print("AAA")
                # if e.key == pygame.K_ESCAPE:
                #     self.state.on_focus = False
                #     self.value = ""
                elif e.key == pygame.K_BACKSPACE:
                    self.value = self.value[:-1]
                # elif e.key == pygame.K_KP_ENTER:
                #     self.state.on_focus = False
                else:
                    if len(self.value) < self.max_length:
                        self.value += e.unicode
                    # print(e.key, pygame.key.name(e.key))
        self.render()
        pygame.display.update()
        print(self.value)

    """
    ..............................................................................................................
    ................................................ UPDATE ......................................................
    ..............................................................................................................
    """

    def update(self, **props):
        super().update(**props)
        # print(self.state.on_focus)
        self.label.update(text=self.value)
        self.activate_bindings()

    def render(self):
        self.screen.draw.rect(self.surface, self.color, self.rect_tuple)
        self.label.render()
