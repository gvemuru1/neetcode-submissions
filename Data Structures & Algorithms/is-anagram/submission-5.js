class Solution {
    isAnagram(s, t) {


        if (s.length !== t.length){
            return false;
        };

        const scount = new Map();
        for( const i of s){
            scount.set(i, (scount.get(i) || 0)+1);
        }

        for (const i of t){
            if(!scount.has(i) || scount.get(i) == 0){
                return false;
                }
            scount.set(i, (scount.get(i) || 0) -1);
        }

        return true;



        

        

        
        
    }
}
