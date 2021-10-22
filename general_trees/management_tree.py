class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        # if child in self.children:
        #     return
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def _return_factor(self, parameter):
        factor1 = 0
        factor2 = 0
        if parameter == "name":
            factor1 += 1
        elif parameter == "designation":
            factor2 += 1
        elif parameter == "both":
            factor1 += 1
            factor2 += 1
        # else:
        #     raise NameError("No such parameter")

        return factor1, factor2

    def print_tree(self, parameter):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        factor1, factor2 = self._return_factor(parameter)

        print(prefix + factor1 * self.name + factor2 *
              (" (" + self.designation + ") "))

        if self.children:
            for child in self.children:
                child.print_tree(parameter)


def build_management_tree():
    ceo = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(TreeNode("Aamir", "Application Head"))

    infr_head = TreeNode("Vishwa", "Infrastructure Head")
    infr_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infr_head.add_child(TreeNode("Abhijit", "App Manager"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Wagas", "Policy Manager"))

    cto.add_child(infr_head)
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo


if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
    pass
