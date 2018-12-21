# Data Structures

Organised to organise data to be processed.
Arrays, linked lists, stacks and queues, trees and hash tables.
To do lists would be represented by arrays; files represented by trees

## Arrays

collection of elements id by index or key

### Single dimension array

`even_elem = array[2n]`

### Multi- dimension array

expressed as `[2,1]`

## Linked Lists

Collection of data elements, called nodes
Contain reference to the next node in the list
Hold whatever data the application needs
A benefit form arrays is:
  That Elements can be easily inserted and removed
  Underlying memory doesn't need to be reorganized. 
Downside:
  Can't do constant-time random item access.
  Item lookup is linear in time complexity(O(n))

## Stacks and Queues

Stack: collection that supports push and pop operations
The last item pushed is the first one popped
Queue: collection that supports adding and removing
First item added is the first item out

### Stacks

#### Stack

Expression processsing
Bakctracking: browser back stack, for example: back button on the browser
First in last out

#### Queue

Order processing
Messaging -> messanger uses a queue to send and list in order sent

#### Hash Table

Associative array (key, value pair) thru the use of a hash
Benefits:
Key-to-value mappings are unique
Speed
Drawbacks:
arrays are more effecient
don't order entries in a predictable way