from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
import string


class MyApp(App):

    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        self.input_text = TextInput(
            hint_text='Ģenerētā parole',
            multiline=False,
            size_hint=(1, 0.2)
        )

        self.label = Label(
            text='Nospied pogu paroles ģenerēšanai',
            size_hint=(1, 0.3)
        )

        generate_button = Button(
            text='Ģenerēt paroli',
            size_hint=(1, 0.2)
        )

        parbaudit_button = Button(
            text='Parbaudīt paroli',
            size_hint=(1, 0.2)
        )

        generate_button.bind(on_press=self.generate_password)

        layout.add_widget(self.input_text)
        layout.add_widget(generate_button)
        layout.add_widget(parbaudit_button)
        layout.add_widget(self.label)

        return layout

    def generate_password(self, instance):
        simboli = (
                string.ascii_letters +
                string.digits +
                string.punctuation
        )
        parole = ""

        for i in range(8):
            parole += random.choice(simboli)
        self.input_text.text = parole
        self.label.text = "Parole izveidota"

    def check_password(self):
        parbaude = self.input_text.text()



MyApp().run()