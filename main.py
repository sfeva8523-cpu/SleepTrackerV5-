from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDTopAppBar
import json

class SleepTracker(MDScreen):
    def save_data(self):
        hours = self.ids.sleep_input.text
        if hours:
            # Simple local storage
            with open("sleep_data.json", "a") as f:
                json.dump({"hours": hours}, f)
                f.write("\n")
            self.ids.status_label.text = f"Logged {hours} hours! 🌙"
            self.ids.sleep_input.text = ""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return SleepTracker()

if __name__ == "__main__":
    MainApp().run()
