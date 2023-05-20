import tkinter as tk
import difflib

class SuggestionBox(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suggestions = []
        self.configure(show="")
        self.bind('<KeyRelease>', self.on_key_release)
        self.suggestion_listbox = None

    def set_suggestions(self, suggestions):
        self.suggestions = suggestions

    def show_suggestions(self):
        if self.suggestion_listbox:
            self.suggestion_listbox.destroy()
        self.suggestion_listbox = tk.Listbox(width=self.winfo_width())
        self.suggestion_listbox.place(x=self.winfo_rootx(), y=self.winfo_rooty() + self.winfo_height())
        self.suggestion_listbox.bind('<<ListboxSelect>>', self.on_suggestion_select)

        for suggestion in self.suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def on_suggestion_select(self, event):
        selected_suggestion = self.suggestion_listbox.get(self.suggestion_listbox.curselection())
        self.delete(0, tk.END)
        self.insert(tk.END, selected_suggestion)

    def on_key_release(self, event):
        current_text = self.get().strip().lower()
        matching_suggestions = difflib.get_close_matches(current_text, self.suggestions, n=5, cutoff=0.0)

        if matching_suggestions:
            self.show_suggestions()
            self.suggestion_listbox.delete(0, tk.END)
            for suggestion in matching_suggestions:
                self.suggestion_listbox.insert(tk.END, suggestion)
        else:
            if self.suggestion_listbox:
                self.suggestion_listbox.destroy()


suggestions = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

root = tk.Tk()

suggestion_box = SuggestionBox(root)
suggestion_box.set_suggestions(suggestions)
suggestion_box.pack()

root.mainloop()
