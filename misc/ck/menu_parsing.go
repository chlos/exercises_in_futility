/*

You have been tasked with parsing menus from a large restaurant group. Each menu is streamed to clients via a provided interface. You must design object(s) that represents a menu and can be instantiated with data from the provided interface. Your design should contain an appropriate class structure to contain the parsed data, as well as a function or set of functions to perform the parsing.

Consumers will use your object(s) to access a complete representation of the data sent by the menu stream after it has finished loading. Your objects should provide easy access to the full representation of the menu. It should be possible to reconstruct the menu stream from your object.

The menu stream represents a list of menu items. Each item in the stream is a menu item, and each item will be separated by an empty string. The attributes of each item are as follows:

Line 0: The ID of the item
Line 1: The item type, either CATEGORY, DISH or OPTION
Line 2: The name of the item
Line 3: The price of the item for DISH and OPTION. Not present for CATEGORY items.
Any other line: A list of item IDs that are linked to the current item. OPTIONs do not have any linked items.

---
4
DISH
Spaghetti
10.95
2
3

//
2345
CATEGORY
foobar
23
34095

1
CATEGORY
Pasta
4
5

2
OPTION
Meatballs
1.00

3
OPTION
Chicken
2.00

5
DISH
Lasagna
12.00

6
DISH
Caesar Salad
9.75
3

---

Category Pasta
	Dish Spaghetti
		Option Meatballs
		Option Chicken
	Dish Lasagna
...

*/

import "io"

type MenuStream interface {
  nextLine() (string, error)
}

func newMenuStream() MenuStream {
  return &menuStreamImpl{
    lines: []string{"4", "DISH", "Spaghetti", "10.95", "2", "3", "", "1", "CATEGORY", "Pasta", "4", "5", "", "2", "OPTION", "Meatballs", "1.00", "", "3", "OPTION", "Chicken", "2.00", "", "5", "DISH", "Lasagna", "12.00", "", "6", "DISH", "Caesar Salad", "9.75", "3", ""},
  }
}

type menuStreamImpl struct {
  lines []string
}

func (m *menuStreamImpl) nextLine() (string, error) {
  if len(m.lines) == 0 {
    return "", io.EOF
  }
  var result string
  result, m.lines = m.lines[0], m.lines[1:]
  return result, nil
}

type Category struct {
	Name: string,
	Dishes: []int,
}

type Dish struct {
	Name: string,
	Price: string,
	Options: []int,
}

type Option struct {
	Name: string,
	Price: string,
}

type MenuStruct interface {
	Build() (map[int]int, error)
}

type menuStructImpl struct {
	menuStream: &MenuStream,
	categoryIDs: []int,
	categories: map[int]Category,
	dishes: map[int]Dish,
	options: map[int]Option,
}

func NewMenuStuctImpl(stream MenuStream) &menuStructImpl {
	for {
		id, _ := stream.nextLine()
		itemType, _ := stream.nextLine()
		itemName, _ := stream.nextLine()
		if itemType == "DISH" || "OPTION" {
			itemPrice, _ := strem.nextLine()

			ids := []int
			for {
				itemID, _ := stream.nextLine()
				if itemID == "" {
					break
				}
				ids = append(ids, strconv.Atoi(itemID))
			}

			if itemType == "DISH" {
				dishes[strconv.Atoi(itemID)] = Dish{
					Name: itemName,
					Price: itemPrice,
				}
			} else {
				opttions[strconv.Atoi(itemID)]
			}

		} else {

			ids := []int
			for {
				itemID, _ := stream.nextLine()
				if itemID == "" {
					break
				}
				ids = append(ids, strconv.Atoi(itemID))
			}
		}

		line, err := stream.nextLine()
		if line == "" && err == io.EOF {
			break
		}

	}
}