func search(nums []int, target int) int {
	il := 0
	ir := len(nums) - 1
	var im int
	for ir-il > 1 {
		im = (il + ir) / 2
		if nums[im] == target {
			return im
		}
		if nums[im] < target {
			il = im + 1
		} else {
			ir = im
		}
	}

	if nums[il] == target {
		return il
	}
	if nums[ir] == target {
		return ir
	}

	return -1
}