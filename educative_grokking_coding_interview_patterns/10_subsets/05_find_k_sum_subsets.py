def get_k_sum_subsets(set_of_integers, target_sum):
  subsets = []

  all_subsets = [[]]
  for num in set_of_integers:
    tmp_subsets = []
    for subset in all_subsets:
      new_subset = subset + [num]
      tmp_subsets.append(new_subset)
      if sum(new_subset) == target_sum:
        subsets.append(new_subset)
    all_subsets.extend(tmp_subsets)

  return subsets