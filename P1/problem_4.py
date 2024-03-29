class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        return "Invalid group"
    elif user in group.get_users():
        return True
    for group in group.get_groups():
        return is_user_in_group(user, group)

    return False


print(is_user_in_group('sub_child_user', child))
print(is_user_in_group('', child))
print(is_user_in_group(None, ""))

p2 = Group("")
print(is_user_in_group(None, p2))

p3 = Group("abc")
p3.add_user(None)
print(is_user_in_group("abc", p3))
print(is_user_in_group(None, p3))
