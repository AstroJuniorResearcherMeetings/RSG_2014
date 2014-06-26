# pseudocode for cooking "Ultimate Vegan Pancakes"
# pseudocode has all the elements of a program but is lax on exact syntax
# The hashtag here is representing a comment to be ignored by the computer

# external library to include certain functions
# flip_pancake, mix_ingredients
include CookingLibrary

# define our own conversion functions though a library would likely 
# exist for such a task
function tsp2cup (tsp amount) {
    cup amount_in_cups = amount/48.0
    return amount_in_cups
}

function tbsp2cup (tbsp amount){
    cup amount_in_cups = amount/12.0
    return amount_in_cups
}

# --- program has some start statement ---
Start Baking {
    # --- program has declaration of variables ---
    # dry ingredients
    cup flour = 1.25 # given a type "cup" which is really a floating point value
    tbsp sugar = 2
    tsp salt = 0.25
    tsp baking_powder = 2

    # wet ingredients
    cup almond_milk = 1.25
    tbsp olive_oil = 1
    tsp vanilla = 1

    # parameters of our pan
    float pan_temp=0.0

    # directions:
    cup dry_ingredients = mix_ingredients(flour,sugar,salt,baking_powder)
    cup wet_ingredients = mix_ingredients(almond_milk,olive_oil,vanilla)
    cup ingredients = dry_ingredients + wet_ingredients

    # wait for pan to heat up
    while (pan_temp < 400)
         pan_temp += 10*random # increasing by ~10 degrees every time step
         wait 10 seconds

    cup amount_for_pancake = 1
    cup pancake = 0
    dynamicArray cooked_pancakes

    while (ingredients > 0){
         # check if removing the appropriate amount is too much
         if ((ingredients - amount_for_pancake) < 0) {
              # if it is just use what’s left
              pancake = ingredients
         else {
              # otherwise use the appropriate amount
              pancake = amount_for_pancake
        }
             
        # keep track of total amount left
        ingredients -= amount_for_pancake

        pancake_to_pan(pancake,pan_temp)
        while (n_bubbles < 0){         
            wait 10 seconds
        }

        flip_pancake(pancake)
        wait 20 seconds # to brown
        cooked_pancakes.append(pancake)
    }
    return cooked_pancakes
}

