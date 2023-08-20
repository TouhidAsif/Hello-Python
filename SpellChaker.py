import tkinter as tk
from spellchecker import SpellChecker

class SpellingCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Checker")

        self.text_box = tk.Text(root, wrap=tk.WORD)
        self.text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def check_spelling(self):
        input_text = self.text_box.get("1.0", tk.END)
        spell = SpellChecker()
        words = input_text.split()

        misspelled = spell.unknown(words)
        corrected_text = []
        for word in words:
            if word in misspelled:
                corrected_text.append(spell.correction(word))
            else:
                corrected_text.append(word)

        self.result_label.config(text="Corrected Text:\n" + ' '.join(corrected_text))

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingCheckerApp(root)
    root.mainloop()
