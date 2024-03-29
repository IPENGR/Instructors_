const threeSumClosest = function(nums,target){
    nums.sort((a,b)=>a-b)

   for(let i =0;i<nums.length-2;i++){
    let left=i+1;
    let right = nums.length-1

    while(left<right){
        const closestSum = nums[i] + nums[left] + nums[right]
        if (Math.abs(target-currentSum)<(Math.abs(target-closestSum))){
        currentSum = closestSum
        }
        if(currentSum<closestSum){
            left++
        }else {
            right --
        }
    }
   }
}