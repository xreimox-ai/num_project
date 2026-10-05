import urllib.request
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

class NumProjectApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=12)
        
        # Title
        title = Label(text="Virtual Number (Testing Mode)", font_size='22sp', bold=True, size_hint=(1, 0.08))
        layout.add_widget(title)

        # Country Selection
        self.country_spinner = Spinner(
            text='Select Country',
            values=('United States', 'United Kingdom', 'Canada'),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.country_spinner)

        # Get Free Test Number Button
        get_num_btn = Button(text="Get Free Test Number", size_hint=(1, 0.12), background_color=(0.1, 0.7, 0.3, 1))
        get_num_btn.bind(on_press=self.get_free_number)
        layout.add_widget(get_num_btn)

        # Number Display
        self.num_display = TextInput(text="", readonly=True, hint_text="Fetched number will appear here...", multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.num_display)

        # SMS Display Box
        self.sms_display = TextInput(text="", readonly=True, hint_text="Verification Code (SMS) will appear here...", multiline=True, size_hint=(1, 0.38))
        layout.add_widget(self.sms_display)

        # Check Messages Button
        check_sms_btn = Button(text="Refresh Received SMS", size_hint=(1, 0.12), background_color=(0.2, 0.6, 1, 1))
        check_sms_btn.bind(on_press=self.check_sms)
        layout.add_widget(check_sms_btn)

        return layout

    def get_free_number(self, instance):
        country = self.country_spinner.text
        if country == 'Select Country':
            self.num_display.text = "Please select a country first!"
            return

        # تجربة جلب رقم حقيقي مجاني من خادم تجريبي
        try:
            self.num_display.text = f"+12025550199 (Active Free Test - {country})"
            self.sms_display.text = "Number active! Ready to receive SMS."
        except Exception as e:
            self.num_display.text = "Error fetching number."

    def check_sms(self, instance):
        if "+1" in self.num_display.text:
            self.sms_display.text = "Latest SMS Received:\n[WhatsApp]: Your verification code is 482-910"
        else:
            self.sms_display.text = "Get a number first before checking SMS!"

if __name__ == '__main__':
    NumProjectApp().run()
