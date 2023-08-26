# This is a sample Python script.
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def loadJSON():
    f = open('formulas.json')
    data = json.load(f)
    f.close()
    return data


def invertJSON(formulas):
    stack = [(formulas, None)]
    inverted_dict = {}
    while stack:
        d, parent_key = stack.pop()
        for k, v in d.items():
            if parent_key is not None:
                inverted_dict.setdefault(k, {}).update({parent_key: {}})
            if isinstance(v, dict):
                stack.append((v, k))

    # Output the inverted dictionary
    #print(inverted_dict.keys())
    return inverted_dict



def findFormulaFromTags(inverted_dict, formulas):
    '''Allows searching through the formula list through the use of Tags'''

    #Creates a list of all the tags from the inverted dictionary.
    tags = [v for v in list(inverted_dict.keys()) if "Tag - " in v]

    #Allows users to search by picking an initial tag.
    print(tags)
    tagChoice = input("Please select a number from 1 to "  + str(len(tags)) +" to pick a tag: ")
    tagPath = [tags[int(tagChoice) - 1]]

    #Give all results from the chosen tag, and allows user to pick the formula they want.
    print(list(inverted_dict[tagPath[0]].keys()))
    tagChoice = input("Please select a number from 1 to "  + str(len(list(inverted_dict[tagPath[0]]))) +" to pick a tag: ")
    tagPath.append(list(inverted_dict[tagPath[0]].keys())[int(tagChoice) - 1])

    #Works the original dictionary from inside out, so to speak, using the inverted dictionary to recreate the path.
    temp = list(inverted_dict[tagPath[0]].keys())[0]
    while "Formulas" not in tagPath:
        tagPath.append(list(inverted_dict[temp].keys())[0])
        temp = list(inverted_dict[temp].keys())[0]

    #Works through the created path to output the formula and all relevant info.
    choice = formulas
    for i in range(len(tagPath) - 1, 0, -1):
        choice = choice[tagPath[i]]
    print(choice)


def findFormulaFromTextSearch(formulas):
    '''Allows searching through the formula list through the use of text keywords.'''

    #Creates a list of all formulas.
    a = []
    for i in range(0, len(list(formulas.values())[0])):
        for j in range(0, len(list(list(formulas.values())[0].values())[i])):
            a.append(list(list(list(formulas.values())[0].values())[i].values())[j])

    #Creates a list of formula names (searchedItem), and a separate list of all their relevant info.
    searchedItem = [[i for i in x] for x in a]
    b = a[0]
    b.update(a[1])

    #Asks the user to give a keyword to filter off of, and then filters the list of formulas.
    textChoice = input("Please enter a keyword to search for a formula: ")
    searchedItem = [i for i in [item for row in searchedItem for item in row] if textChoice in i]

    #Displays the filtered equations from the text input and asks the user to choose a formula from this list.
    print(searchedItem)
    itemChoice = input("Please enter a number from 1 - " + str(len(searchedItem)) + " to choose your formula: ")

    #Returns the chosen formula and all relevant info.
    print(b[searchedItem[int(itemChoice) - 1]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formulas = loadJSON()
    inverted_dict = invertJSON(formulas)
    #findFormulaFromTags(inverted_dict, formulas)
    findFormulaFromTextSearch(formulas)
    #print(formulas)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
