class SubtitleLine:

    def __init__(self):
        self.subtitleText = ''
        self.index = ''
        self.time_interval = ''

    def set_index(self, index):
        self.index = index

    def set_time(self, time_interval):
        self.time_interval = time_interval

    def add_text_fragment(self, text_fragment):
        if not self.subtitleText:
            self.subtitleText = text_fragment
        else:
            self.subtitleText += ' ' + text_fragment

    def show_subtitle(self):
        print(self.index, self.time_interval)
        print(self.subtitleText)
