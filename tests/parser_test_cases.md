# Comments tests
To test if comments interfere w

IP

```
sound = ON; //enables music
//speed = 1;
```

OP

```
music is enabled
but speed is unaffected
```

# Testing strings

Strings end as soon as a closing double quote is encountered.

By default, python regex match greedily, i.e. it will match till the last double quote found
 because the syntax `{"L",#106b77}, {"I",#106b77}` will give errors as it will try to greedily

IP

```
opening_msg = "this has double ", but gives error ";
closing_msg = "!@#$%^&*(QWERTYUIOPASDFGHJKLZXCVBNM)'/<>" 
pieces = [{"L",#106b77}, {"I",#106b77}];
```

OP

```
opening msg is not set, as string does not include quotes
closing msg is set
pieces L and I are set successfuly to the given colors
```

# Testing arrays

Arrays present a challenge to the parser, as there are many variations and errors possible:

IP

```
board = []; //set to defaults, empty array
scoring = [0, 40]; //scoring upto 2 levels is set, above which defaults are taken 
pieces = [{"L",#FFFFFF}, {"I",#111111}]; //L and I pieces are allowed and colored
pieces = []; //default pieces
scoring = [1,"a"] 
board = {]
pieces = [{"L",#FFFFFF]];
```

OP

```
- Board dims are set to defaults
- scoring upto 2 levels is set, above which defaults are taken
- L and I pieces are allowed and colored
- Default pieces are set
- Syntax error, Scoring is not set. Only integers are allowed 
- Syntax error, as both should be square brackets
- Syntax error, as both should be curly brackets
```

# Test keybinding and valid pieces

Keybindings should match pygame keybindings.
Valid pieces set is:  'L','I','O','J','Z','S','T'

IP

```
rotate = "K_UP";
rotate = "K_INVALIDKEYNAME";
```

OP

```
- First keybinding works, sets up arrow 
- Second key binding is invalid as it is not a key in pygame
```