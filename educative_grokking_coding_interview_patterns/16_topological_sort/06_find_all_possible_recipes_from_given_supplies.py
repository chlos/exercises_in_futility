import collections
from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        # build graph and in-degree count
        graph_ingredient_to_recipe = collections.defaultdict(set)
        in_degrees = collections.defaultdict(int)
        for recipe, curr_ingredients in zip(recipes, ingredients):
            for ingredient in curr_ingredients:
                graph_ingredient_to_recipe[ingredient].add(recipe)
            in_degrees[recipe] = len(curr_ingredients)

        # topological sort
        res = []
        supplies_queue = collections.deque(supplies)  # start with 'supplies' as sources
        while supplies_queue:
            supply = supplies_queue.popleft()
            for recipe in graph_ingredient_to_recipe[supply]:
                in_degrees[recipe] -= 1
                if in_degrees[recipe] <= 0:
                    supplies_queue.append(recipe)
                    res.append(recipe)

        return res
