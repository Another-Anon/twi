import json
import Twi
import listener
import os
from qery import Qery




with open("config.json", "r") as cfg:
    # print(config)
    text = cfg.read()
    config = json.loads(text)

HOTWORD = config["hotword"]



class TWInterface(object):
    """docstring for Interface."""

    def __init__(self, type:str, twi):
        super(TWInterface, self).__init__()
        self.type = type
        self.twi = twi


    def getAllCommands(self, list_after_hotword):
        commandsKeys = list(COMMANDS)
        l = []
        for word in list_after_hotword:
            if word in commandsKeys:
                l.append((word, list_after_hotword.index(word)))
        return l

    def getWordsFromUser(self):
        if self.type == "voice":
            l = listener.listen()
        if self.type == "text":
            l = input()
            l = l.split()
            if HOTWORD in l:
                return {"words" : l, "hotwordIndex" : l.index(HOTWORD)}
        print(l)
        return l


    def mainLoop(self):
        while True:
            try:
                raw_command = self.getWordsFromUser()
                hotwordIndex = raw_command["hotwordIndex"]
                list_after_hotword = raw_command["words"][hotwordIndex+1:]

                #print(list_after_hotword)

                qery = Qery(list_after_hotword, self.twi)

                print(qery.commands)
                print(qery.getContexts())



            except Exception as e:
                print(e)

def main():
    twi = Twi.Twi()
    app = TWInterface("voice", twi)
    app.mainLoop()


if __name__ == '__main__':
    main()


#   моча жопа гавно сопли моча
#   моча кексик сопли браузер запусти браузер моча музыка все пауза
#   моча кексик жопа гавно сопли моча
#   кексик музыка все пауза
#   ("браузер", "пауза")
#   ("пауза", "браузер")
#   ("моча", "гавно")
