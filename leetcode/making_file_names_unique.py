class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        names_count = {}
        
        for name in names:
            unique_name = name
            if name in names_count:
                count = names_count[name]
                while unique_name in names_count:
                    count += 1
                    unique_name = f'{name}({count})'
                names_count[name] = count

            names_count[unique_name] = 0

        # dicts are ordered in p3
        return names_count.keys()