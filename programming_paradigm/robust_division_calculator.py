def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"Result: {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Inputs must be numeric."
