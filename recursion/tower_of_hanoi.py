def tower_of_Hanoi(num_disks, a, b, c):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    if num_disks == 1:
        print("move {} disk from {} to {}".format(num_disks, a, b))
        return

    tower_of_Hanoi(num_disks - 1, a, c, b)
    print("move {}th disk from {} to {}".format(num_disks, a, b))
    tower_of_Hanoi(num_disks - 1, c, b, a)


tower_of_Hanoi(3, 'source', 'destination', 'auxiliary')
