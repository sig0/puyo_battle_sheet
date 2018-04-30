class puyofu:

    def __init__(self):
        self.path = ""
        self.puyofu = ""
        self.battle_list = []


def puyofu2battle_list(puyofu):
    all_lines = "\t".join(puyofu)
    battle_text = [x for x in all_lines.split("=== end ===") if x != []]
    battle_list = [x.split('\t') for x in battle_text]
    return battle_list


def text2class():


if __name__ == "__main__":
    with open("kame-decisions.txt") as f:
        puyofu = [x for x in f]
        battle_list = puyofu2battle_list(puyofu)
        [print(x) for x in battle_list[1]]
