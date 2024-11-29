# -*- coding: utf-8 -*-

#Button parameters:
#1. Text: Click Me
#2. Font Size: 14.0px
#3. Border: 2px green solid
#4. Background color: yellow


class Button:
    def __init__(self, text, font_size=12.0, border_width=1,
                 border_color="red", border_type="solid", bg_color="blue"):
        self.text = text
        self.font_size = font_size
        self.border_width = border_width
        self.border_color = border_color
        self.border_type = border_type
        self.bg_color = bg_color

    def display_info(self):
        info = (
            "Button parameters:\n"
            "1. Text: {}\n"
            "2. Font Size: {}px\n"
            "3. Border: {}px {} {}\n"
            "4. Background color: {}".format(
                self.text, self.font_size, self.border_width,
                self.border_color, self.border_type, self.bg_color
            )
        )
        return info

# Тестування класу
button = Button("Click Me", font_size=14.0, border_width=2, border_color="green", bg_color="yellow")
print(button.display_info())

