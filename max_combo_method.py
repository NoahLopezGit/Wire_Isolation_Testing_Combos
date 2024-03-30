import itertools

def tested_combos(pins, combos):
    tested_combos = []
    for combo in combos:
        pin1, pin2 = combo
        if (pin1 in pins) != (pin2 in pins):
            tested_combos.append(combo)
    return tested_combos

def remove_combos(tested_combos, combos):
    return [combo for combo in combos if combo not in tested_combos]

# generate all pairs for a given pin count
pin_count=50
combos =  list(itertools.combinations(range(1,pin_count+1),2))

#iterate over each pin, add pin if it increases the tested combos
#stop if end of pins is reached or pin_count//2 pins are added
sets = []
while len(combos)>0:
    pins = []
    previous_amount_tested = 0
    for pin in range(1,pin_count+1):
        if len(pins)>pin_count//2:
            break
        new_amount_tested = len(tested_combos(pins + [pin], combos))
        if new_amount_tested > previous_amount_tested:
            pins.append(pin)
        previous_amount_tested = new_amount_tested
    sets.append(pins)
    combos = remove_combos(tested_combos(pins, combos), combos)

print(sets)
print(len(sets))