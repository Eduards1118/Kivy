from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        # Galvenais logs
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Teksta ievade
        self.input_text = TextInput(
            hint_text='Ievadiet tekstu',
            multiline=False,
            size_hint=(1, 0.2)
        )

        # Teksta lauks
        self.label = Label(
            text='Šeit parādīsies teksts',
            size_hint=(1, 0.4)
        )

        # Poga
        send_button = Button(
            text='Sūtīt',
            size_hint=(1, 0.2)
        )

        # Pogas darbība
        send_button.bind(on_press=self.send_text)

        # Elementu pievienošana
        layout.add_widget(self.input_text)
        layout.add_widget(send_button)
        layout.add_widget(self.label)

        return layout

    # Teksta nosūtīšana
    def send_text(self, instance):
        self.label.text = self.input_text.text


if __name__ == '__main__':
    MyApp().run()
