# Solution

This Repo is a solution for the Kata: https://github.com/emilybache/GildedRose-Refactoring-Kata


### Refactor -> From Shop to Item

The major change, appart of adding the new funcionality, was to refactor the code.

I've considered that the logic must be not in the shop on itself. 
It has to be something controlled by the Item, for some reasons:

- In real life, is the Item who controls its own quality and sell_in parameters independently of the place. If I've got a cheese, it's the cheese who increase its quality by itself, not the shop where it is.
- If tomorrow they want to add 20 different type of Objects with different logic, we'll no have way to improve the update_quality method.

So, I decide to heridate from Item (in order to not modify it) and add the funcionality based on the type.
The shop only will loop though the Items, and execute its update_quality method.

For now, its fine to increase/decrease its sell_in inside this method just because is something readable and easy to understand it.

### The name must no decide the type of object
Also, I consider that the name has no to be a property for base the type of object in declaration. If I've a Backstage Brie Conjured Cheese, What's going to happen?

