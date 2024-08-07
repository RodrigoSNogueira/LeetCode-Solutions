int search(int* nums, int numsSize, int target) {
    int lowest = 0;
    int highest = numsSize - 1;

    while (lowest <= highest){
        int middle = (lowest + highest)/2;
        int middle_value = nums[middle];

        if (middle_value == target){
            return middle;
        }
        if (middle_value > target){
            highest = middle - 1;

        }else {
            lowest = middle + 1;
        }

        
    }
    
    return -1;

return 0;
}
