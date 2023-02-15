# RobotsGA
Applying genetic algorithm(GA) to Solve the Path Planning Problem


Robot’s world consists of 100 squares laid in a 10*10 grid, where each square can at most have one soda can. From wherever he currently is, he can see the contents of one adjacent site in the north, south, east, and west directions, as well as the contents of the site he’s currently in.

Each individual strategy is a list of 243 actions. Each action consists of one of the following seven choices: move to north, move to south, move to east, move to west, choose a random direction to move in, stay up, or bend down to pick up a can.

Each action may generate a reward or a punishment.

If robot is in the same site as a can and picks it up, he gets a reward of 10 points. However, if he bends down to pick up a can in a site where there is no can, he is fined 1 point.

If he crashes into a wall, he is fined 5 points and bounces back into the current site.
Robot’s reward is maximized when he picks up as many cans as possible, without crashing into any walls or bending down to pick up a can when no can is there.

Apply GA with the following properties to this problem:

Recombination
Single-point

Mutation
Mutate each number in the chromosome with mutation probability and replace it with a randomly generated number between 0 and 6

Mutation prob.
0.5%

Selection
Roulette wheel
