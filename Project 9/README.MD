
Write a class called AddThreeGame that allows two players to play a game in which they alternately choose numbers from 1-9.  They may not choose a number that has already been selected by either player.  If at any point exactly three of the player's numbers sum to exactly 15, then that player has won.  If all numbers from 1-9 are chosen, but neither player has won, then the game ends in a draw. Player "first" has the first turn.

The class will need **private** data members for:
1. keeping track of which numbers have been chosen, and by whom
2. the current state, which holds one of the four following values: "FIRST_WON", "SECOND_WON", "DRAW", or "UNFINISHED"
3. keeping track of whose turn it is

Your AddThreeGame class must include the following methods:
* An init method that takes no parameters and initializes all data members.
* A get method named get_current_state, which returns the current state.
* A method named make_move that takes two parameters - a string designating the player making the move, either "first" or "second", and an integer giving their number choice (in that order).  If it is not that player's turn, or if the integer is not in the correct range, or if that integer has already been chosen, or if the game has already been won or drawn, make_move should return False. You can assume the user chooses an integer, but if it's outside the range 1-9, make_move should return False. Otherwise, it should record the move, update the current state if the move caused a win or draw, update which player's turn it is, and return True.

For example, your class could be used as follows:
```
game = AddThreeGame()
game.make_move("first", 2)
game.make_move("second", 5)
result = game.make_move("first", 7)
state = game.get_current_state()
```

Don't know where to start? First try playing a few games on paper to get a feel for how the rules work. Next, try working on the easiest bits first - then you can cross them off and (hopefully) not have to think about them anymore. In this project, the easiest part is the get method, which just needs to return the value of a data member. The next easiest part is the init method, which just needs to initialize all of the data members. Initializing data members isn't usually difficult, but first you'll have to decide what data members you want to use to keep track of things. Most of the work is in the make_move method. Probably the most challenging part of the make_move method is checking (if the proposed move was valid) whether the state of the game has changed to a win or draw. You may find it useful to create an additional method for that, which your make_move method can call. Since the method would be just for internal use by the class, such a method should be **private**. The other parts of make_move are just checking whether the proposed move is valid, recording the move (if it's valid), and **returning either True or False** as appropriate. Remember to test your functions as you go. Do NOT try to code it all at once and then start testing - that's a recipe for frustration, since it makes it much harder to track down bugs. Remember to plan out your tests ahead of time. If you don't know what result you should get before running a test, it can be easy to convince yourself that the result your program gives you looks okay.

Your file must be named: AddThreeGame.py
