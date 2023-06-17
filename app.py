from gcode_analyzer import Analyzer
from tkinter import Tk, Label, Button, filedialog

class GCodeAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GCode Analyzer")

        self.filename_label = Label(root, text="")
        self.filename_label.pack()

        self.time_label = Label(root, text="")
        self.time_label.pack()

        self.filament_label = Label(root, text="")
        self.filament_label.pack()

        self.browse_button = Button(root, text="Browse", command=self.browse)
        self.browse_button.pack()

    def browse(self):
        filename = filedialog.askopenfilename()
        if not filename:
            return
        self.filename_label['text'] = f"File: {filename}"

        try:
            analyzer = Analyzer(filename)
            self.time_label['text'] = f"Estimated Print Time: {analyzer.get_formatted_time()}"
            self.filament_label['text'] = f"Filament Usage: {analyzer.get_filament_usage() / 1000:.2f} meters"
        except IOError:
            self.time_label['text'] = f"Error: {filename} does not exist"
            self.filament_label['text'] = ""


if __name__ == "__main__":
    root = Tk()
    app = GCodeAnalyzerApp(root)
    root.mainloop()
