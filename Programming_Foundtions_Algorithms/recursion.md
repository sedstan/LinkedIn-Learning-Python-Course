# Recursion

This is effectively a case statement in JavaScript

When a function calls itself

e.g. ```function f() {
  ... 
  f()
}```

Find a fiile deeply nested in a tree of directories
make a flow chart of pseudo code

Remember: 1. Recursive functions need to have a breaking condition
          2. This prevents infinite loops and eventual crashes
          3. Each time the cunction is calle, the old arguments are saved
          4. This called the "call stack"

```function countdown(x) {
  if(x === 0)
    print("done!")
    return
  else
    print(x, "...")
    countdown(x-1)
} 
countdown(4)```