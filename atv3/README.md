# Guided Project - Performance and Complexity Analysis

This guided project was developed based on the "Introduction to Algorithms" course on the dataquest.io platform. It focuses on analyzing the performance and complexity of algorithms, as well as comparing different implementation approaches. The main objectives of this project include:

- Understanding how to analyze the time and space complexity of an algorithm.
- Learning how data pre-processing can significantly speed up an algorithm.
- Exploring data classification techniques and efficient search on classified data.
- Implement efficient algorithms for specific tasks, such as finding pairs of equal values in a list and locating two values whose sum is equal to a given value.

## Data Set

The dataset used in this project comes from a laptop store and includes information such as ID, Brand, Product, Type, Size (in inches), Screen Resolution, CPU and RAM. This data is used to illustrate and analyze the performance of the implemented algorithms.

## Inventory class

To facilitate data processing, a class called `Inventory` was created. This class allows laptops to be instantiated and their characteristics to be manipulated. It has several methods, each with two versions: an initial version and an optimized version. The optimized versions aim to improve the performance of operations.

## Time complexity analysis
The following describes the time complexity of the main functions implemented:

### `get_laptop_from_id`
- **Big O (O)**: O(n), where n is the number of attached laptops. The function goes through the list of laptops to find the laptop with the corresponding ID. In the worst case, it may have to go through the entire list.
- **Big Theta (Θ)**: Θ(n), because the function always needs to go through all the rows to find the laptop or determine that it is not present.
- Big Omega (Ω)**: Ω(1), in the best case, when the desired laptop is in the first position of the list.

### `get_laptop_id_fast`
- **Big O (O)**: O(1). This function uses a `self.id_to_row` dictionary to check for the existence of a laptop with the given ID. The dictionary lookup operation has average complexity O(1).
- Big Theta (Θ)**: Θ(1), because the function always performs a single presence check on the dictionary, regardless of the size of the dictionary.
- **Big Omega (Ω)**: Ω(1), in the worst case, the function only needs one check on the dictionary.

### `check_promotion_dollars`
- **Big O (O)**: The function performs two nested iterations over the list of laptops, where the first iteration has a complexity of O(k), and the second iteration also has a complexity of O(k).
Therefore, the total time complexity is O(k^2), where k is the number of laptops.
- **Big Theta (Θ)**: The time complexity Θ(k^2) is an accurate description of the complexity, because the function always needs to check all possible combinations of prices.
- **Big Omega (Ω)**: The function always needs to check all possible combinations of prices, which implies that the time complexity Ω(k^2) is a precise lower bound for the function.

### `check_promotion_dollars_fast`
- **Big O (O)**: The function iterates over the set self.prices (O(k)) and, for each price, performs a check if dollars - price is present in the set (O(1) on average). Therefore, the total time complexity is O(k), where k is the number of unique prices.
- **Big Theta (Θ)**: The time complexity Θ(k) is an accurate description of the complexity, because the function goes through all the unique prices once.
- **Big Omega (Ω)**: The time complexity Ω(k) is an accurate undercut for the function, because the function always needs to traverse all unique prices.

### `find_laptop_with_price`
- **Big O (O)**: The function iterates over the set self.prices (O(k)) and, for each price, performs a check if dollars - price is present in the set (O(1) on average). Therefore, the total time complexity is O(k), where k is the number of unique prices.
- **Big Theta (Θ)**: The time complexity Θ(k) is an accurate description of the complexity, because the function goes through all the unique prices once.
- **Big Omega (Ω)**: The time complexity Ω(k) is an accurate undercut for the function, because the function always needs to traverse all unique prices.

### `find_first_laptop_more_expensive`
- **Big O (O)**: The function implements a binary search on the list of laptops sorted by price, which results in a complexity of O(log k), where k is the number of laptops.
- **Big Theta (Θ)**: The time complexity Θ(log k) is an accurate description of the complexity, because the function always splits the list of laptops in half at each iteration.
- **Big Omega (Ω)**: The time complexity Ω(log k) is an accurate lower bound for the function, because the binary search is efficient and always halves the search space.

### `find_laptops_in_price_range`
- **Big O (O)**: The function implements a binary search on the list of laptops sorted by price, which results in a complexity of O(log k), where k is the number of laptops.
- **Big Theta (Θ)**: The time complexity Θ(log k) is an accurate description of the complexity, because the function always splits the list of laptops in half at each iteration.
- **Big Omega (Ω)**: The time complexity Ω(log k) is an accurate lower bound for the function, because the binary search is efficient and always halves the search space.

### `find_laptops_in_price_range_fast`
- **Big O (O)**: The function starts by finding the index of the first laptop with a price greater than or equal to min_price using the find_first_laptop_more_expensive function. The complexity of this function is logarithmic in relation to the number of laptops, as it uses binary search on the sorted list, which results in a complexity of O(log n), where n is the number of laptops. The function then goes through the sorted list of laptops until it finds laptops outside the price range. The number of laptops within the price range affects the number of iterations required. Therefore, the loop part has a potential complexity of O(k), where k is the number of laptops within the price range. In short, the total complexity of the function depends on both parts: O(log n) to find the first laptop and O(k) to go through the laptops within the price range. In the worst case, the complexity is O(log n + k).
- **Big Theta (Θ)**: The time complexity Θ(log n + k) is an accurate description of the complexity, as it takes into account both the binary search and the number of laptops within the price range.
- **Big Omega (Ω)**: The time complexity Ω(log n + k) is an accurate lower bound for the function, as the function always needs to find the first laptop with a price greater than or equal to min_price and cycle through the laptops within the price range.

### `is_laptop_match`
- **Big O (O)**: The function performs linear operations to find matches for the amount of RAM and the storage capacity in the laptop description, resulting in O(n + m), where n is the length of the RAM description string and m is the length of the storage description string. Checking the RAM and storage specifications is a constant time operation. Therefore, the total time complexity is O(n + m).
- **Big Theta (Θ)**: The time complexity Θ(n + m) is an accurate description of the complexity, because the function always needs to find matches for RAM and storage, regardless of the exact values.
- **Big Omega (Ω)**: The function always needs to find matches for RAM and storage, which implies that the time complexity Ω(n + m) is a precise lower bound for the function.

### `find_cheapest_laptop_with_specifications`
- **Big O (O)**: The function involves two main steps: filtering laptops that meet the specifications (O(k * (n + m)), where k is the number of laptops, n is the length of the RAM description string and m is the length of the storage description string); finding the cheapest laptop among the filtered laptops (O(k)).
Therefore, the total time complexity is O(k * (n + m)), where k is the number of laptops, n is the length of the RAM description string and m is the length of the storage description string.
- **Big Theta (Θ)**: The time complexity Θ(k * (n + m)) is an accurate description of the complexity, because the function always needs to go through the list of laptops and check the RAM and storage specifications.
- **Big Omega (Ω)**: The function always needs to go through the list of laptops and check the RAM and storage specifications, which implies that the time complexity Ω(k * (n + m)) is an accurate lower bound for the function.
