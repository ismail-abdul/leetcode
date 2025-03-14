# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

Initially I though of checking each possible string combination for `s` and comparing it to `goal`. But that would've been $$O(n^2)$$.

After running a few test cases, I concluded that there were a few cases to consider. All of which surrounded how many letters were "out of place" or just plain wrong in `s`. 

Ultimately, I thought if I could determine how many letters were out of place, I'd have been able to solve the problem properly.

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```javascript []
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
    if (s.length != goal.length || s.length === undefined || goal.length === undefined) 
        return false;
    
    var mistakes = [];
    var uniques = new Set([]);

    for (let i = 0; i<s.length; i++){
        uniques.add(s[i]);
        if (s[i] != goal[i]) { mistakes.push(i); }
    }
    console.log(uniques);
    console.log("uniques: " + uniques.toString() + uniques.size);
    console.log("mistakes: " + mistakes + mistakes.length);

    /*WHY IS THIS NOT ZERO. WTFFFFFFFFFFFFFFF. PAIN. BANKAI!!!!!! */
    if (mistakes.length === 0 ) {
        //analyse the number of unique letters in s.
        if (uniques.size === undefined) {
            console.log("No letters exist to swap");
            return false;
        }
        if (uniques.size === s.length) {
            //all the letters are distinct.
            console.log("Same letters. All distinct. No swaps possible");
            return false;
        } 
        else if (uniques.size < s.length) {
            //assuming uniques isn't empty. Not all the letters are the same in s. Or 
            console.log("At least one letter swap possible.");
            return true;
        } else {
            console.log("This shouldn't be possible. Uniques should never be longer than s.");
            return false;
        }
        
    } else if (mistakes.length === 1) {
        console.log("Only one character is out of place. No possible swaps")
        return false;
    } else if (mistakes.length === 2) { 
        /* 
            check what happens when characters are swapped.
            there's probably a way to build the strings with them swapped but i cba
        */
        if (
            s[mistakes[0]] === goal[mistakes[1]] &&
            s[mistakes[1]] === goal[mistakes[0]]
        ) {
            console.log("out of place characters are diff");
            return true;
        } else if (
            s[mistakes[1]] === goal[mistakes[1]] && 
            s[mistakes[0]] === goal[mistakes[0]]
        ) {
            console.log("out of place characters are the same");
            return true;
        } else {
            return false;
        }
    } else {
        console.log("Wrong amount of o.o.p chars.")
        return false;
    }

    

};
```