import glob
import json


class Event:

    def __init__(self):
        self.name = ""



class Puyofu:

    def __init__(self):
        self.path = ""
        self.name = ""
        self.battle_list = []
        self.event_list = []
        self.event_list.append(Event())


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)



def puyofu2battle_list(puyofu):
    all_lines = "\t".join(puyofu)
    battle_text = [x for x in all_lines.split("=== end ===") if x != []]
    battle_list = [x.split('\t') for x in battle_text]
    return battle_list


def text2class():
    print("hello")

def default_puyofu_dirs():
    return glob.glob("puyofuData/*")

if __name__ == "__main__":

    dirlist = default_puyofu_dirs()
    for d in dirlist:
        files = glob.glob(d + "/*")

    p1 = Puyofu()
    print(p1.toJSON())
