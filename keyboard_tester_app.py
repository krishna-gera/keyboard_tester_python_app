import tkinter as tk
from pynput import keyboard

class KeyboardTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Tester")
        self.current_screen = None
        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()
        self.current_screen = "start"
        
        start_label = tk.Label(self.root, text="Welcome to Keyboard Tester", font=("Arial", 24))
        start_label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start", command=self.create_layout_selector)
        start_button.pack(pady=10)

    def create_layout_selector(self):
        self.clear_screen()
        self.current_screen = "layout_selector"

        layout_label = tk.Label(self.root, text="Select Keyboard Layout", font=("Arial", 24))
        layout_label.pack(pady=20)

        layouts = ["QWERTY", "AZERTY", "DVORAK", "Mac"]
        self.selected_layout = tk.StringVar(value=layouts[0])

        for layout in layouts:
            layout_radio = tk.Radiobutton(self.root, text=layout, variable=self.selected_layout, value=layout)
            layout_radio.pack(anchor=tk.W)

        next_button = tk.Button(self.root, text="Next", command=self.create_keyboard_tester)
        next_button.pack(pady=10)

    def create_keyboard_tester(self):
        self.clear_screen()
        self.current_screen = "keyboard_tester"

        keyboard_label = tk.Label(self.root, text="Press any key on your keyboard", font=("Arial", 24))
        keyboard_label.pack(pady=20)

        self.key_display = tk.Label(self.root, text="", font=("Arial", 16), bg="lightgrey", width=30, height=2)
        self.key_display.pack(pady=10)

        self.draw_keyboard()

        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def draw_keyboard(self):
        self.keyboard_frame = tk.Frame(self.root, bg="darkgray")
        self.keyboard_frame.pack(pady=20)

        self.keys = [
            ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Win', 'Alt', ' ', 'Alt', 'Win', 'Menu', 'Ctrl']
        ]

        self.key_buttons = {}
        for row in self.keys:
            row_frame = tk.Frame(self.keyboard_frame, bg="darkgray")
            row_frame.pack()
            for key in row:
                key_button = tk.Button(row_frame, text=key, width=5, height=2, bg="black", fg="white",
                                       command=lambda k=key: self.key_display.config(text=f"Key Pressed: {k}"))
                key_button.pack(side=tk.LEFT, padx=2, pady=2)
                self.key_buttons[key] = key_button  # Store reference to the button

    def on_key_press(self, key):
        try:
                key_char = key.char
                self.key_display.config(text=f"Key Pressed: {key_char}")
                if key_char.upper() in self.key_buttons:
                    self.key_buttons[key_char.upper()].config(bg="cyan", fg="black")  # Highlight the pressed key
        except AttributeError:
            self.key_display.config(text=f"Special Key Pressed: {key}")
            if hasattr(key, 'name') and key.name in self.key_buttons:
                self.key_buttons[key.name].config(bg="cyan", fg="black")  # Highlight special key

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardTesterApp(root)
    root.mainloop()