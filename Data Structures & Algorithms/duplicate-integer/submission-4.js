class Solution {
    
    hasDuplicate(nums) {
        const newbaby = new Set()
        nums.forEach((i)=>{
            newbaby.add(i)
        });

        if (nums.length === newbaby.size){
            return false
        }
        else {
        return true }
    }
}
