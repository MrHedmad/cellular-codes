import math
from mpmath import mpf, nstr, fdiv, log

def progress_bar(
    completed,
    max = 100,
    length = 30,
    title = "",
    break_lines = True,
    tokens = {"start":">> ", "end":"|", "complete":"#", "empty":"-", "tip":"#"},
    include_percentage = True,
    include_raw = True):

    raw_completed = completed

    if completed > max:
        completed = max

    comp_perc = fdiv(log(completed, 10), log(max, 10))

    comp_pips = math.floor(comp_perc * length)
    incomp_pips = length - comp_pips

    if title != "":
        title += ": "
    
    end = ""

    if include_percentage is True:
        end += " " + str(round(comp_perc * 100, 2)) + " %"
        if include_raw is True:
            end += " |"
    else:
        end += ""
    
    if include_raw is True:
        end += " " + nstr(raw_completed) + " / " + nstr(max)

    breaking = "\n" if break_lines is True else ""

    return (
        title + breaking +
        tokens["start"] +
        (comp_pips - 1) * tokens["complete"] +
        tokens["tip"] +
        incomp_pips * tokens["empty"] +
        tokens["end"] +
        end
        )


class Achievement:
    def __init__(self, tiers: list, name: str = None):
        last = 0
        converted = []
        for x in tiers:
            converted.append(mpf(x))
            assert last <= mpf(x)
            last = mpf(x)
        self.tiers = converted
        self.max = sum(converted)
        self.name = name if name is not None else ""
    
    def get_bar(self, progress, length = 50):
        progress = mpf(progress)
        completed = 0
        for tier in self.tiers:
            if tier <= progress:
                completed += 1
                continue
            max = tier
            break
        else:
            max = tier
        b = len(self.tiers)
        tiers = " - Tier " + str(completed) + "/" + str(b)
        return progress_bar(
            progress,
            max = max,
            length = length,
            title = (self.name + tiers)
        )


ach1 = Achievement(['1e3', '1e5', '1e10', '1e50', '1e100'], name="Acquire credits")
print(ach1.get_bar('9.4351e34'))

ach2 = Achievement(
    ['1', '5', '10', '20', '30', 40, 100, 150, 1e10, 1e30],
    name="Level up"
    )

for x in [1, 2, 4, 7, 20, 25, 29.9, 30, 60, 145, 151, 1e7, 1e11, 2.54e13, 9e29, 1e30, 1e35]:
    print(ach2 .get_bar(x))