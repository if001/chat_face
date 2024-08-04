class History():
    def __init__(self, history_file=""):
        self._history_file = history_file
        self._history = ""

    def get(self):
        return self._history

    def load(self):
        with open(self._history_file, "r") as f:
            self._history = f.read()
    
    def update(self, new_history):
        with open(self._history_file, "w") as f:
            f.write(new_history)
    
    def update_with_load(self, new_history):
        self.update(new_history)
        self.load()

def main():
    h = History("./history/hi.txt")


if __name__ == "__main__":
    main()