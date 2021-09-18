import json

def laminasMarvel(laminas, prices):
    output1 = 0
    output2 = []

    laminas = json.loads(laminas)
    prices = prices.split()
    for price in prices:
        for key in laminas.keys():
        
            if price == key:
                output1 += laminas[key]
                output2.append(price)
    
    return (print(output1), "\n", print(" ".join(output2)))

laminasMarvel(input(), input())