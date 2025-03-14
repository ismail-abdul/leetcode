public class BuddyStrings {
    public static void main(String args[]) {
        BuddyStringsProgram("kebab", "kebab");
    }
    public static boolean BuddyStringsProgram(String s, String goal) {
        if (s.length != s.goal) {
            return false;
        } 

        ArrayList<String> mismatches = new ArrayList<String>(); 
        Arraylist<String> uniques = new Arraylist<String>();

        for (int i = 0; i < s.length; i++) {
            if (s.substring(i) != goal.substring(i) ) {
                uniques.add(s.substring(i));
                mismatches.add(i);
            }
        }

        if (mismatches.length == 1 || mismatches.length > 2 ) {
            return false;
        } else if ( mismatches.length == 2 ){
            int a = mismatches.get(0);
            int b = mismatches.get(1);
        }
        
    }
}