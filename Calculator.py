from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Calculator(App):
    def build(self):
        widget_root = BoxLayout(orientation='vertical')
        label_op = Label(size_hint_y=0.75, font_size=51)
        symbol_button = ('1', '2', '3', '+',
                         '4', '5', '6', '*',
                         '7', '8', '9', '.',
                         '0', '/', '-', '0/p')
        grid_button = GridLayout(cols=4, size_hint_y=2)
        for symbol in symbol_button:
            grid_button.add_widget(Button(text=symbol))

        button_clr = Button(text="CE", size_hint_y=None, height=100)

        def text_print_btn(instance):
            label_op.text += instance.text

        for button in grid_button.children[1:]:
            button.bind(on_press=text_print_btn)

        def label_text_size(lable, new_height):
            lable.fontsize = 0.5 * lable.height

        label_op.bind(height=label_text_size)

        def result(instance):
            try:
                label_op.text = str(eval(label_op.text))
            except Exception as e:
                print(e)

        grid_button.children[0].bind(on_press=result)

        def label_clr(instance):
            label_op.text = " "

        button_clr.bind(on_press=label_clr)

        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)
        widget_root.add_widget(button_clr)
        return widget_root


Calculator().run()
