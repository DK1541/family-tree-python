# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:20:51 2024

@author: D K PANDEY
"""

class FamilyMember:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def display_family_tree(person, level=0):
    print("  " * level + "|__" + person.name + " (" + person.gender + ", " + str(person.age) + " years old)")
    for child in person.children:
        display_family_tree(child, level + 1)

def main():
    # Create family members
    grandma = FamilyMember("Grandma", 75, "Female")
    grandpa = FamilyMember("Grandpa", 80, "Male")
    dad = FamilyMember("Dad", 50, "Male")
    mom = FamilyMember("Mom", 45, "Female")
    child1 = FamilyMember("Child1", 25, "Male")
    child2 = FamilyMember("Child2", 22, "Female")
    grandpa.add_child(dad)
    grandma.add_child(dad)
    dad.add_child(mom)
    dad.add_child(child1)
    dad.add_child(child2)

    # Display family tree
    print("Family Tree:")
    display_family_tree(grandma)

if __name__ == "__main__":
    main()
