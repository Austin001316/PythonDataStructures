def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1

    for num in nums:
        if num % 2 == 0:
            product = product * num

    return product
    #elif len(even_numbers) and len(result) = 1:
    #    even_numbers.pop[0] * result[0]
    #    final_result.append
    #else len(even_numbers) == 0:
    #    return final_result

        