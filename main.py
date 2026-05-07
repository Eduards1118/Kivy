# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set window background color (RGBA)
Window.clearcolor = (0.15, 0.15, 0.2, 1)  # Dark blue-gray

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        # Label
        self.label = Label(
            text="Enter your name below:",
            font_size=24,
            color=(1, 1, 1, 1)  # White text
        )
        self.add_widget(self.label)

        # Text input
        self.text_input = TextInput(
            hint_text="Type here...",
            multiline=False,
            font_size=20,
            size_hint=(1, 0.2),
            background_color=(0.2, 0.2, 0.3, 1),
            foreground_color=(1, 1, 1, 1),
            padding_y=(10, 10)
        )
        self.add_widget(self.text_input)

        # Button
        self.button = Button(
            text="Submit",
            font_size=20,
            size_hint=(1, 0.3),
            background_normal='',
            background_color=(0.3, 0.6, 0.9, 1)  # Blue
        )
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        """Update label text when button is pressed."""
        name = self.text_input.text.strip()
        if name:
            self.label.text = f"Hello, {name}!"
        else:
            self.label.text = "Please enter your name."


class MyApp(App):
    def build(self):
        self.title = "Kivy UI Example"
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
