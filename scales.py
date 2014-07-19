NOTES = "A A# B C C# D D# E F F# G G#"
MAJOR = "W W H W W W H"
def get_scale_steps(s):
    """
    :param s: string of W and H's
    :return: a list of the scale translated into 1 or 2s
    """
    l = s.split()
    #assertion
    a = [e in "WH" for e in l]
    assert all(a)

    steps = []
    for e in l:
        if e == "W":
            steps.append(2)
        else:
            steps.append(1)
    return steps

def get_scale(note,scale,notes=NOTES):
    """

    :param NOTES: The global NOTES
    :param note: A string of the note that will start the scale
    :param scale: A global variable that will be the basis of the scale
    :return: a string of the scale
    """
    notes = notes.split()
    index = notes.index(note)
    notes_list = notes[index:] + notes[:index] + [notes[index]]
    scale_list = get_scale_steps(scale)
    index = 0
    l = [notes_list[index]]

    for e in scale_list:
        index += e
        l.append(notes_list[index])
    return ' '.join(l)

def get_all_scales(major,notes=NOTES):
    for note in notes.split():
        print get_scale(note,major)
    else:
        return "The {} scales have been printed".format(str(major))

print get_scale('C',MAJOR)

print get_all_scales(MAJOR)

