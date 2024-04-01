from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

def calculate_purity_875(weight):
    numerator = float(weight)
    denominator = 96
    percentage = 84
    purity = (numerator / denominator) * percentage
    return purity

def calculate_purity_916(weight):
    numerator = float(weight)
    denominator = 96
    percentage = 104.75
    purity = (numerator / denominator) * percentage
    return purity

def calculate_purity_tezab(weight, decimal_point_value):
    numerator = float(weight)
    denominator = 96
    percentage = 95 + (float(decimal_point_value) / 100)
    purity = (numerator / denominator) * percentage
    return purity

class GoldPurityCalculator(GridLayout):
    def __init__(self, purity_type, **kwargs):
        super(GoldPurityCalculator, self).__init__(**kwargs)
        self.cols = 1
        self.purity_type = purity_type

        self.label_weight = Label(text="Enter Gold Weight (grams):")
        self.add_widget(self.label_weight)
        self.entry_weight = TextInput()
        self.add_widget(self.entry_weight)

        if self.purity_type == 'tezab':
            self.label_decimal_point = Label(text="Enter Value After Decimal Point:")
            self.add_widget(self.label_decimal_point)
            self.entry_decimal_point = TextInput()
            self.add_widget(self.entry_decimal_point)

        self.button_calculate = Button(text="Calculate Purity")
        self.button_calculate.bind(on_press=self.calculate_purity)
        self.add_widget(self.button_calculate)

        self.label_formula = Label(text="")
        self.add_widget(self.label_formula)

        self.label_result = Label(text="")
        self.add_widget(self.label_result)

    def calculate_purity(self, instance):
        weight = self.entry_weight.text
        if weight:
            try:
                if self.purity_type == '875':
                    purity = calculate_purity_875(weight)
                    formula = f"Formula: ({weight} / 96) * 84"
                elif self.purity_type == '916':
                    purity = calculate_purity_916(weight)
                    formula = f"Formula: ({weight} / 96) * 104.75"
                elif self.purity_type == 'tezab':
                    decimal_point_value = self.entry_decimal_point.text
                    purity = calculate_purity_tezab(weight, decimal_point_value)
                    formula = f"Formula: ({weight} / 96) * 95.{decimal_point_value}"

                self.label_formula.text = formula
                self.label_result.text = f"Purity: {purity:.3f}"
            except ValueError:
                self.label_result.text = "Invalid input"
        else:
            self.label_result.text = "Please enter weight"

class GoldPurityApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)
        layout.add_widget(Button(text="PURE 875", on_press=lambda instance: self.show_purity_window('875')))
        layout.add_widget(Button(text="PURE 916", on_press=lambda instance: self.show_purity_window('916')))
        layout.add_widget(Button(text="PURE TEZAB", on_press=lambda instance: self.show_purity_window('tezab')))
        return layout

    def show_purity_window(self, purity_type):
        popup_title = f'Pure {purity_type} Calculator'
        popup_content = GoldPurityCalculator(purity_type=purity_type)
        popup = Popup(title=popup_title, content=popup_content, size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    GoldPurityApp().run()
