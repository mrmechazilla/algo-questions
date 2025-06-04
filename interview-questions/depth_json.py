def depth_json(obj, depth=0):
    if not isinstance(obj, (dict, list)):
        return depth

    if (isinstance(obj, list) and len(obj) == 0) or (isinstance(obj, dict) and len(obj.keys()) == 0):
        return depth + 1
    else:
        max_depth = depth
        values = obj.values() if isinstance(obj, dict) else obj
        for v in values:
            local_depth = depth_json(v, depth + 1)
            if local_depth > max_depth:
                max_depth = local_depth
        return max_depth
    
# Test Examples

print(depth_json([]) == 1)
print(depth_json([1, 2, 3, 4, 5]) == 1)
print(depth_json([{ 'a': [] }, ["abc"]]) == 3)
print(depth_json([{ 'a': { 'b': 1, 'c': 2 } }, ["abc"]]) == 3)
print(depth_json([{ 'a': { 'b': 1, 'c': 2 } }, ["abc", {}]]) == 3)
print(depth_json([{ 'a': { 'b': [10, 20], 'c': 2 } }, ["abc"]]) == 4)
print(depth_json([{ 'a': { 'b': [10, 20, {}], 'c': 2 } }, ["abc"]]) == 5)
print(depth_json([{ 'a': { 'b': [10, 20, { 'd': [] }], 'c': 2 } }, ["abc"]]) == 6)
print(depth_json([{ 'a': { 'b': [10, 20, { 'd': [{}] }], 'c': 2 } }, ["abc"]]) == 7)
print(depth_json([{ 'a': { 'b': [10, 20, { 'd': [{ 'e': [] }] }], 'c': 2 } }, ["abc"]]) == 8)
print(depth_json([{ 'a': { 'b': [10, 20, { 'd': [{ 'e': [{}] }] }], 'c': 2 } }, ["abc"]]) == 9)