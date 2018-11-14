/*
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.
*/





/*
Solution:

1. HASH MAP:
-  Use a hash map to hold character counts. If it's seen, increase count if not seen
set to 1
- Iteratre thru string again if the map has the character then return return
the
*/

function firstUniqueChar(s) {
  const map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      map.set(s[i], 2) // can be any #
    } else {
      map.set(s[i], 1)
    }
  }

  for (let j = 0; j < s.length; j++) {
    if (map.has(s[j]) && map.get(s[j]) == 1) {
      // return 1st time we see a count of 1
      return j;
    }
  }
  return - 1
}
