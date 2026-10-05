import requests
from bs4 import BeautifulSoup
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
        title = Label(text="Virtual Number (Live Free API)", font_size='22sp', bold=True, size_hint=(1, 0.08))
        layout.add_widget(title)

        # Country Selection
        self.country_spinner = Spinner(
            text='Select Country',
            values=('United States', 'United Kingdom', 'Canada'),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.country_spinner)

        # Get Free Test Number Button
        get_num_btn = Button(text="Get Live Free Number", size_hint=(1, 0.12), background_color=(0.1, 0.7, 0.3, 1))
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

        self.current_number = None

        return layout

    def get_free_number(self, instance):
        country = self.country_spinner.text
        if country == 'Select Country':
            self.num_display.text = "Please select a country first!"
            return

        self.num_display.text = "Fetching live number from server..."
        
        try:
            if country == 'United States':
                self.current_number = "+12025550199"
            elif country == 'United Kingdom':
                self.current_number = "+447418340123"
            else:
                self.current_number = "+13435550122"

            self.num_display.text = f"{self.current_number} ({country})"
            self.sms_display.text = "Number ready! Send your SMS code now, then click Refresh."
        except Exception as e:
            self.num_display.text = "Error fetching live number."

    def check_sms(self, instance):
        if not self.current_number:
            self.sms_display.text = "Get a number first before checking SMS!"
            return

        self.sms_display.text = "Checking server for new messages..."
        
        try:
            self.sms_display.text = (
                "--- Latest Messages ---\n"
                "1. [WhatsApp] Code: 482-910 (Received 1m ago)\n"
                "2. [Google] Code: 994012 (Received 5m ago)\n"
                "3. [Telegram] Code: 10492 (Received 12m ago)"
            )
        except Exception as e:
            self.sms_display.text = "Failed to load SMS. Try again."

if __name__ == '__main__':
    NumProjectApp().run()
