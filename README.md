# Bruhat-Tits
Bruhat-Tits tree plotter (see [wikipedia](https://en.wikipedia.org/wiki/Building_(mathematics))). This is how I generated my profile picture.

## Functions

* angle_rel: utility function to compute the angle between tree branches;
* Tree: draw using PIL the branches of the tree (uses recursion);
* BT_Tree: first draw the base of the tree and then use the `Tree` function to complete the Bruhat-Tits tree.
