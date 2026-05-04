import tkinter as tk
import winsound
import os
import threading
import queue
import sys

class ZeniraEngine:
    def __init__(self, file_name, question_label, user_entry, result_display, go_btn):
        self.file_name = file_name
        self.question_label = question_label
        self.user_entry = user_entry
        self.result_display = result_display
        self.go_btn = go_btn
        self.input_queue = queue.Queue()
        self.output_text = []

    def custom_input(self, prompt):
        # Update the question area
        self.question_label.config(text=prompt)
        self.user_entry.delete(0, tk.END)
        
        # Wait for the user to click SUBMIT
        val = self.input_queue.get()
        
        # Clear screen ONLY AFTER submission to keep the next step fresh
        self.output_text = [] 
        self.result_display.config(text="")
        return val

    def custom_print(self, *args):
        text = " ".join(map(str, args))
        self.output_text.append(text)
        # Displays your options (1, 2, 3) in the result area
        self.result_display.config(text="\n".join(self.output_text))

    def run(self):
        try:
            # encoding="utf-8" prevents crashes from emojis/symbols
            with open(self.file_name, "r", encoding="utf-8") as f:
                code = f.read()
            
            exec(code, {
                'input': self.custom_input,
                'print': self.custom_print,
                '__name__': '__main__',
                'tk': tk
            })
            
            self.user_entry.pack_forget()
            self.go_btn.pack_forget()
            self.question_label.config(text="✨ Task Complete ✨")

        except Exception as e:
            self.result_display.config(text=f"Logic Error: {e}")

def run_set(file_name, bg_color, display_text):
    for widget in app.winfo_children():
        widget.pack_forget()

    app.config(bg=bg_color)
    
    # Sound: Professional beep when entering a module
    winsound.Beep(1000, 150) 

    # Header
    tk.Label(app, text=display_text, font=("Arial Black", 32, "bold"), 
             bg=bg_color, fg="#4b4b4b", pady=30).pack()

    # Question Label
    q_label = tk.Label(app, text="Zenira is ready...", font=("Segoe UI", 20, "bold"), 
                       bg=bg_color, fg="#4b4b4b", wraplength=380)
    q_label.pack(pady=10)

    # Result/Options Display
    r_display = tk.Label(app, text="", font=("Segoe UI", 16, "bold"), 
                         bg=bg_color, fg="#2c3e50", wraplength=380, justify="center")
    r_display.pack(pady=10)

    # Input Box
    u_entry = tk.Entry(app, font=("Segoe UI", 18, "bold"), bd=0, highlightthickness=2, 
                       highlightbackground="white", justify="center")
    u_entry.pack(pady=10, padx=40, fill="x")
    u_entry.focus_set()

    engine = ZeniraEngine(file_name, q_label, u_entry, r_display, None)

    def on_submit():
        val = u_entry.get()
        if val:
            engine.input_queue.put(val)

    # Submit Button
    submit_btn = tk.Button(app, text="SUBMIT ✨", font=("Segoe UI", 14, "bold"), bg="white", 
                           fg="#4b4b4b", relief="flat", padx=40, pady=10, command=on_submit)
    submit_btn.pack(pady=15)
    engine.go_btn = submit_btn

    threading.Thread(target=engine.run, daemon=True).start()

    # Back to Menu
    tk.Button(app, text="⬅ Back", font=("Segoe UI", 11, "bold"), bg="white", 
              fg="#4b4b4b", command=lambda: (app.destroy(), os.startfile("Z.py")), 
              relief="flat", padx=10).pack(side="bottom", pady=40)

def play_startup_sound():
    try:
        # Check if running as .exe or .py to find startup.wav
        if hasattr(sys, '_MEIPASS'):
            sound_path = os.path.join(sys._MEIPASS, "startup.wav")
        else:
            sound_path = "startup.wav"
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except:
        # Backup system sound if magic sound is missing
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)

# --- MAIN MENU (SKY BLUE) ---
app = tk.Tk()
app.title("Zenira")
app.geometry("450x750")
app.config(bg="#E0F7FA")

play_startup_sound()

tk.Label(app, text="ZENIRA", font=("Arial Black", 52, "bold"),
         bg="#E0F7FA", fg="#4b4b4b", pady=60).pack(fill="x")

btn_style = {"font": ("Segoe UI", 15, "bold"), "width": 22, "pady": 18, 
             "fg": "#4b4b4b", "relief": "flat", "cursor": "hand2", "bd": 0}

# The 4 integrated modules: Learn Quest, Day Flow, Mind Anchor, Book Bloom
tk.Button(app, text="LEARN QUEST", bg="#FFD1DC", **btn_style,
          command=lambda: run_set("Learn Quest.py", "#FFD1DC", "Learn Quest 🌸")).pack(pady=12)

tk.Button(app, text="DAY FLOW", bg="#FFF9AE", **btn_style,
          command=lambda: run_set("Day Flow.py", "#FFF9AE", "Day Flow ☀️")).pack(pady=12)

tk.Button(app, text="MIND ANCHOR", bg="#B2F2BB", **btn_style,
          command=lambda: run_set("Mind Anchor.py", "#B2F2BB", "Mind Anchor 🌿")).pack(pady=12)

tk.Button(app, text="BOOK BLOOM", bg="#E0BBE4", **btn_style,
          command=lambda: run_set("Book Bloom.py", "#E0BBE4", "Book Bloom 🔮")).pack(pady=12)

app.mainloop()


           
    
