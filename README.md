# Tetris

## TADS Language
The language is a declarative language, that specifies how a tetris game needs to be configured. The TADS compiler will scan and parse a ```.tads``` file which will pick up configuration parameters and generate a python tetris game.

---
---

## Offered Primitives

### Comments

Comments are single line or in-line.

All characters following a ```//``` till end of the line is treated as a comment and hence ignored.

---

### Strings
Can only include alphabets (any case), underscores, digits, spaces and tabs.

Strings are enclosed within double quotes ```"``` only.

Example String: 

```
"A_String 	123"
```

---

### Pieces

Pieces can be selected from the default tetrominoes, in form of an array.
Each array element is a pair with tetromino name, a color, defined in hex(6 digit hex, for instance ```#008080``` for teal).

For example:

```
 pieces = [{"L",#008080}, {"I",#808080}, {"O",#800080}]; 
```

If array is blank (```pieces=[];```) then the default 7 are set with default colors.

If a color field is left blank then a default color is applied to it. (```pieces=[{L,}];```)

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

### Toggles

Some configurations can be toggled on or off.
- ghost 
- sound

0 for off, 1 for on. For example,

```
// toggles
ghost = 0; //ghost piece shown or not
sound = 0; //toggles music
```

---

### Difficulty Levels

Difficulty can be set to ```noob``` , ```ez``` , ```god``` levels in increasing order of difficulty.
For example,
```
difficulty = ez;
``` 

---

### Scoring Levels

The ```scoring``` array accepts integer values for points.

The ith item of the array is the value of points awarded for clearing i rows.

The 0th item represents the score for settling of a piece that clears .

```
scoring = [0, 40, 100, 300, 1200, 5000];
``` 

Examples
```
//Single line comment
ghost = 0; //in-line comment
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

- 0 is treated as ```true/on```
- 1 is treated as ```false/off```

For example, to set ghost pieces as on, but sound as off, we use :

```
// toggles
ghost = 1; //ghost piece shown 
sound = 0; //music on
```
