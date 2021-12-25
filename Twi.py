import time
import subprocess
import json
import os




class Twi(object):

    """docstring for Twi."""

    def __init__(self,):
        super(Twi, self).__init__()

        self.COMMANDS = {
            "запустить" : (self.runProgramm, 1, "run"),
            "запусти" : (self.runProgramm, 1, "run"),
            "музыка" : (self.playerctl, 2, "player"),
            "скажи" : (self.sey, -1, "sey"),
            "пауза" : (self.playPlayers, 1, "player")
        }

        print(r"""
        TWI ALFA
""")



    def repeatLast(self):
        pass


    def runProgramm(self, name):
        os.system(name)
        # process = subprocess.Popen(name.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()



    def playerctl(self, option="--player=%any", command="play-pause"):
        process = subprocess.Popen("playerctl {} {}".format(option, command).split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output, error)


    def playPlayers(self, player="--player=%any,"):
        self.playerctl(player, "play-pause")
        #process = subprocess.Popen("playerctl --player=%any, play-pause".split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()

    def stopAllPlayers(self,):
        self.playerctl("-a", "stop")

        #process = subprocess.Popen("playerctl -a stop".split(), stdout=subprocess.PIPE)
        #output, error = process.communicate()

    def seyTime(self):
        print(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

    def sey(self, word):
        print(word)




def main():
    twi.seyHi("anon")
    twi.seyTime()

if __name__ == '__main__':
    main()
