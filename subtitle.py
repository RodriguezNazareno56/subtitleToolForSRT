class Subtitle:

    def __init__(self):
        self.subtitleText = ''
        self.index = ''
        self.time_interval = ''

    def addIndex(self, index):
        self.index = index

    def addTime(self, time_interval):
        self.time_interval = time_interval

    def addTextFragment(self, text_fragment):
        self.subtitleText += ' ' + text_fragment

    def showSubtitle(self):
        print(self.index, self.time_interval)
        print(self.subtitleText)