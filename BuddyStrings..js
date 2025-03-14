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

    /*WHY IS THIS NOT ZERO. WTFFFFFFFFFFFFFFF. PAIN. BANKAI!!!!!! */
    if (mistakes.length === undefined ) {
        //analyse the number of unique letters in s.
        if (uniques.length === undefined) {
            //No letters exist to swap
            return false;
        }
        if (uniques.length === s.length) {
            //all the letters are distinct.
            console.log("Same letters. All distinct. No swaps possible");
            return false;
        } 
        else if (uniques.length < s.length) {
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
    } else if (mistakes.length === 2) { // check what happens when characters are swapped. there's probably a way to build the strings with them swapped but i cbs
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