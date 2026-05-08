from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

import random
import string


class MyApp(App):

    def build(self):
        # Galvenais logs
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Teksta ievade
        self.input_text = TextInput(
            hint_text='Ievadiet paroli',
            multiline=False,
            size_hint=(1, 0.2)
        )

        # Ziņojuma lauks
        self.label = Label(
            text='Rezultāts parādīsies šeit',
            size_hint=(1, 0.4)
        )

        # Poga paroles ģenerēšanai
        generate_button = Button(
            text='Ģenerēt paroli',
            size_hint=(1, 0.2)
        )

        generate_button.bind(on_press=self.generate_password)

        # Poga paroles pārbaudei
        check_button = Button(
            text='Pārbaudīt paroli',
            size_hint=(1, 0.2)
        )

        check_button.bind(on_press=self.check_password)

        # Elementu pievienošana
        layout.add_widget(self.input_text)
        layout.add_widget(generate_button)
        layout.add_widget(check_button)
        layout.add_widget(self.label)

        return layout

    # Paroles ģenerēšana
    def generate_password(self, instance):
        symbols = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(symbols) for _ in range(8))

        self.input_text.text = password
        self.label.text = 'Parole tika ģenerēta'

    # Paroles pārbaude
    def check_password(self, instance):
        password = self.input_text.text

        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        if has_upper and has_digit and has_symbol:
            self.label.text = 'Parole ir droša'
        else:
            self.label.text = 'Parole nav droša'


if __name__ == '__main__':
    MyApp().run()
