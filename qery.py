import json
import Twi




with open("config.json", "r") as config:
    # print(config)
    text = config.read()
    config = json.loads(text)



class Word(object):
    """docstring for Word."""

    def __init__(self, arg):
        super(Word, self).__init__()
        self.arg = arg


class Qery(object):
    """docstring for qery."""

    def __init__(self, words, twi):
        super(Qery, self).__init__()
        self.twi = twi
        self.commandCfg = twi.COMMANDS
        self.words = words
        self.commandNames, self.indexes = self.getAllCommandNames() #FIX all indexes
        self.context = self.getAllContexts()
        #self.qery = self.parseQery()

    def parseQery(self):
        pass

    def getAllCommandNames(self):
        commandsKeys = list(self.commandCfg)
        commands = [word if word in commandsKeys else "" for word in self.words]
        indexes = [self.words.index(word) if word in commandsKeys else "" for word in self.words]
        return commands, indexes #list(dict.fromkeys(commands)), list(dict.fromkeys(indexes))

    def getAllContexts(self):
        commands = self.commandCfg
        context = ["" if command=="" else commands[command][2] for command in self.commandNames]
        return context #list(dict.fromkeys(context))

    def createAllCommands(self):
        l = []
        for i in range(len(self.commandNames)):
            if self.commandNames[i] == "":
                continue
            else:
                print(i)
                print(self.commandNames[i], self.indexes[i], self.context[i])
                l.append(Command(self.commandNames[i], self.indexes[i], self.context[i], self.commandCfg))
        print(l[1].getFrontArgs(self.words))
        print(l[1].getBackArgs(self.words))
        return l

    def runAllCommands(self):
        commands = createAllCommands()
        for command in commands:
            command.run()




class Arg(object):
    """docstring for arg."""

    def __init__(self, name, context):
        super(Arg, self).__init__()
        self.arg = arg


class Command(object):
    """docstring for Command."""

    def __init__(self, name, index, context, cfg):
        super(Command, self).__init__()
        self.context = context
        self.name = name
        self.index = index
        self.ArgCount = cfg[self.name][1]
        self.callback = cfg[self.name][0]

    def getFrontOrBackWords(self, words, position):
        print(words)
        if position == "front":
            return words[self.index+1 : self.index + self.ArgCount+1]
        if position == "back":
            return words[self.index - self.ArgCount : self.index]


    def getFrontArgs(self, words):
        front = self.getFrontOrBackWords(words, "front")
        for word in front:
             print(config[self.context][word])

    def getBackArgs(self, words):
        back = self.getFrontOrBackWords(words, "back")
        for word in back:
            print(config[self.context][word])

    def run(self,):
        pass





def main():
    twi = Twi.Twi()
    q = Qery("кексик сопли торрент запусти браузер моча музыка все пауза".split(), twi)
    print(q.commandNames)
    print(q.getAllContexts())
    print(q.indexes)
    print(q.createAllCommands())

if __name__ == '__main__':
    main()
