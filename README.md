# Tetris



## Offered Primitives

The compiler will scan and parse a ```.tads``` file which will pick up configuration parameters and generate a pyhton tetris game.

### Pieces

Pieces can be selected from the default tetrominoes, in form of an array.
Each array element is a pair with tetromino name, a color, defined in hex(6 digit hex, for instance ```#008080``` for teal).

For example:

```
 pieces = [{L,#106b7793}, {I,#106b7793}, {O,#106b7793}]; 
```

If array is blank (```pieces=[];```) then the default 7 are set with default colors.

If a color field is left blank then a default color is applied to it. (```pieces=[{L,}];```)



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
rotate = KEY_UP; 
```
The values specified should be the key names defined in [pygame docs](https://www.pygame.org/docs/).
If any keybinging is unspecified then the default key binding is used. The defaults are:





