from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

class NumProjectApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(text="Virtual Number App", font_size='22sp', bold=True, size_hint=(1, 0.1))
        layout.add_widget(title)

        # Country Selection
        self.country_spinner = Spinner(
            text='Select Country',
            values=('United States', 'United Kingdom', 'Egypt', 'Canada'),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.country_spinner)

        # Get Number Button
        get_num_btn = Button(text="Get New Number", size_hint=(1, 0.12), background_color=(0.2, 0.6, 1, 1))
        get_num_btn.bind(on_press=self.get_number)
        layout.add_widget(get_num_btn)

        # Number Display
        self.num_display = TextInput(text="", readonly=True, hint_text="Received number will appear here...", multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.num_display)

        # SMS Display Box
        self.sms_display = TextInput(text="", readonly=True, hint_text="Verification Code (SMS) will appear here...", multiline=True, size_hint=(1, 0.38))
        layout.add_widget(self.sms_display)

        # Refresh SMS Button
        check_sms_btn = Button(text="Refresh SMS", size_hint=(1, 0.12), background_color=(0.1, 0.8, 0.4, 1))
        check_sms_btn.bind(on_press=self.check_sms)
        layout.add_widget(check_sms_btn)

        return layout

    def get_number(self, instance):
        country = self.country_spinner.text
        if country == 'Select Country':
            self.num_display.text = "Please select a country first!"
        else:
            self.num_display.text = f"+123456789 (Test - {country})"

    def check_sms(self, instance):
        self.sms_display.text = "Waiting for SMS... No new messages yet."

if __name__ == '__main__':
    NumProjectApp().run()
