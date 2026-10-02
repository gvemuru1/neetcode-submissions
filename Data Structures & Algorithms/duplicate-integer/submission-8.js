class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const ns = new Set(nums);

        if((nums.length) === ns.size){
            return false;
        }else{
            return true;
            }
    }
}
