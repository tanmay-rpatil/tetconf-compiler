# Tetris

## TADS Language
The language is a declarative language, that specifies how a tetris game needs to be configured. The TADS compiler will scan and parse a `.tads` file which will pick up configuration parameters and generate a python tetris game.

---
---

## Offered Primitives

### Comments

Comments are single line or in-line.

All characters following a `//` till end of the line is treated as a comment and hence ignored.

Examples
```
//Single line comment
ghost = 0; //in-line comment
```

---

### Strings
Can only include alphabets (any case), underscores, digits, spaces and tabs.

Strings are enclosed within double quotes `"` only.

Example String: 

```
"A_String 	123"
```

---

### Macros
Macro identifier is @[A-Za-z_][A-Za-z_0-9]*@
Example Macro:
```
@ON@ 1;
ghost = @ON@;
```
This replaces "@ON@" with "1".

---

### Pieces

Pieces can be selected from the default tetrominoes, in form of an array.
Each array element is a pair with tetromino name, a color, defined in hex(6 digit hex, for instance `#008080` for teal).

For example:

```
 pieces = [{"L",#008080}, {"I",#808080}, {"O",#800080}]; 
```

If array is blank (`pieces=[];`) then the default 7 are set with default colors.

If a color field is left blank then a default color is applied to it. (`pieces=[{"L",}];`)

---

### Key Bindings 

The actions which are available are:
- rotate
- go_left
- go_right
- soft_drop
- hard_drop
- pause

Can be assigned to keys, for example:
``` 
rotate = "K_UP"; 
```
The values specified should be the key names defined in [pygame docs](https://www.pygame.org/docs/).
If any keybinding is unspecified then the default key binding is used. The defaults are:

---

### Difficulty Settings

- Speed can be set to `noob` , `ez` , `god` levels in increasing order of speed.
	Syntax example,
	```
	speed = ez;
	``` 

- The bias of Piece Generation Algorithm can be toggled on or off:
    - 0 indicates off: all pieces are generated randomly with equal probability.
    - 1 indicates on:  pieces `O`, `I` shall be generated with low probability, `J`, `L` with higher probability and `S`, `Z` with the hightest probability.
	
	Syntax example,
	```
	bias = 0;
	``` 

- Disco mode can be toggled on or off:
    - 0 indicates off: Normal color scheme is followed where each type of block has a static color.
    - 1 indicates on:  The color of all blocks and the grid frame all flash random colors each frame.
	Syntax example,
	```
	disco_mode = 0;
	``` 

- Ghost mode can be toggled on or off:
    - 0 indicates off: The predicted position of the current block piece won't be showed.
    - 1 indicates on: The predicted position shall be displayed.
	Syntax example,
	```
	ghost_mode = 0;
	``` 

---

### Additional Settings

- The Sound configurations can be toggled on or off.
	0 for off, 1 for on. Syntax example,

```
sound = 1; //toggles music
```

---

### Scoring Levels

The `scoring` array accepts integer values for points.

The ith item of the array is the value of points awarded for clearing i rows.

The 0th item represents the score for settling of a piece that clears .

```
scoring = [0, 40, 100, 300, 1200, 5000];
``` 

---
---

## Modes for programming

### Arrays

Arrays are used to specify tetromino types available in-game, and for specifying scoring levels.

For example, 
```
 pieces = [{"L",#008080}, {"I",#808080}, {"O",#800080}]; 
```

### Booleans/Toggles

For simple on/off configuration parameters. 

- 0 is treated as `true/on`
- 1 is treated as `false/off`

For example, to set ghost pieces as on, but sound as off, we use :

```
// toggles
ghost = 1; //ghost piece shown 
sound = 0; //music on
```

### Keywords Provided
- board
- rotate
- go_left
- go_right
- soft_drop
- hard_drop
- pause
- ghost 
- sound
- disco_mode
- speed