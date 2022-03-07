# Comments tests
```
//@notamacro@
//not keywords: pause, hard_drop; not strings: "ab_21"; board(30,40);
//not arrays: [12,13]; [{"L",#123456}]
```

# Testing strings

```
"not scanned as keywords: on off board pireces"
```

The Following are invalid tokens

```
"invalid_token 
```

# Testing macro definitions

```
@VALID_MACRO@ 123;
@INVALID 123;
@also_valid@ 123;
```