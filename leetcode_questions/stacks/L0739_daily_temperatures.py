def dailyTemperatures(temperatures):
    # Initialize the result list with zeros
    result = [0] * len(temperatures)
    # Stack to store indices of the temperatures
    stack = []

    # Iterate over the temperatures list with index
    for current_index, current_temp in enumerate(temperatures):
        # While there are elements in the stack and the current temperature is higher than the temperature at the index stored in the stack
        while stack and current_temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            # Calculate the number of days until a warmer temperature
            result[prev_index] = current_index - prev_index
        # Push the current index onto the stack
        stack.append(current_index)

    return result


# Example usage
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# Print the result of calling dailyTemperatures with the example list
print(dailyTemperatures(temperatures))
