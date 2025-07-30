# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
distance=float(input("Enter the shipping distnce in km: "))
 # Here is a new update by <your GitHub xoxo>
#added a new line here UNDER XOXO

## Calculate shipping cost
shipping_cost = weight * rate*(distance*.2)

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

