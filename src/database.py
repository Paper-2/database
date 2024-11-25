import sqlite3


class Database:
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect('recipes_data.db')
        self.cursor = self.connection.cursor()

        self.__create_table()

    def __create_table(self):
     
        self.cursor.execute("DROP TABLE IF EXISTS Cuisines") # drops the old table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Cuisines
        (cui_type TEXT, rec_name TEXT, ingredients_list TEXT, directions TEXT, link TEXT, is_favorite INTEGER DEFAULT 0)
        ''') # makes a new table 
        
        
        try:
            # Italian Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Italian', 'Air Fryer Chicken Parmesan',
                            '2 boneless skinless chicken breasts, kosher salt, black pepper, all-purpose flour, eggs, panko breadcrumbs, Parmesan cheese, olive oil, crushed red pepper, garlic powder, marinara sauce, mozzarella cheese',
                            ' Gather all ingredients.\nOn a cutting board, butterfly chicken by cutting each breast in half widthwise to create 4 thin pieces of chicken; season both sides with 1/2 teaspoon of the salt and 1/4 teaspoon of the black pepper.\n Place flour, egg, and panko in 3 separate shallow dishes. Add Parmesan, oil, crushed red pepper, and garlic powder to panko; stir to coat. Add remaining 1/4 teaspoon salt and remaining 1/4 teaspoon black pepper to flour; stir to combine. Working with 1 chicken piece at a time, dredge chicken in flour; shake off excess. Dip in egg; let excess drip off. Dredge in panko mixture to coat; place on a plate.\n Preheat a 6-quart air fryer to 400 degrees F (200 degrees C) for 2 minutes. Working in two batches, add 2 chicken cutlets to the air fryer basket in a single layer. Cook until chicken is golden brown on both sides, about 5 minutes per side.\n  Top each chicken piece with 1/4 cup marinara and 1/4 cup mozzarella cheese.\n Snugly fit all 4 breasts in a single layer in air fryer basket; cook at 400 degrees F (200 degrees C) until cheese is melted and browned and a thermometer inserted into the thickest portion of chicken registers 165 degrees F (73 degrees C), 2 to 3 minutes.',
                         'https://www.allrecipes.com/air-fryer-chicken-parmesan-recipe-8698442'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Italian', 'Pizza on the Grill',
                            'warm water, active dry yeast, white sugar, all-purpose flour, olive oil, kosher salt, garlic minced, fresh basil, tomatoes, black olives, roasted red peppers, mozzarella cheese',
                            ' Gather all ingredients.\nMake dough: Pour warm water into a large bowl; dissolve yeast and sugar in warm water. Let stand until yeast softens and begins to form a creamy foam, about 5 to 10 minutes.\nMix in flour, 1 tablespoon olive oil, and salt until dough pulls away from the sides of the bowl.\nTurn onto a lightly floured surface. Knead until smooth, about 8 minutes.\nPlace dough in a well-oiled bowl and cover with a damp cloth.\nSet aside to rise until doubled, about 1 hour. Punch down; knead in garlic and basil. Set aside to rise for 1 more hour, or until doubled again.\nMeanwhile, make garlic oil: Combine 1/2 cup olive oil with minced garlic in a microwave-safe cup or bowl. Heat for 30 seconds in the microwave.\nPreheat an outdoor grill for high heat; brush the grate with garlic oil.\nMake pizzas: Punch down dough and divide in half. Form each half into an oblong shape 3/8 to 1/2 inch thick.\nCarefully place one piece of dough on the hot grill. Dough will begin to puff almost immediately. When the bottom crust has lightly browned, turn dough over using two spatulas.\nWorking quickly, brush garlic oil over crust.\nTop with 1/2 of each of the following: tomato sauce, chopped tomatoes, olives, red peppers, cheese, and basil.\nClose the lid and cook until cheese melts. Remove from grill and set aside to cool for a few minutes. Repeat with second piece of dough\n'
                         ,'https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Italian', 'World\'s Best Lasagna',
                            'Italian sausage, ground beef, minced onion, garlic, crushed tomatoes, tomato sauce, tomato paste, water, sugar, parsley, basil, salt, Italian seasoning, fennel seeds, black pepper, lasagna noodles, ricotta cheese, egg, mozzarella cheese, Parmesan cheese',
                            'Gather all your ingredients.\nCook sausage, ground beef, onion, and garlic in a Dutch oven over medium heat until well browned.\nStir in crushed tomatoes, tomato sauce, tomato paste, and water. Season with sugar, 2 tablespoons parsley, basil, 1 teaspoon salt, Italian seasoning, fennel seeds, and pepper. Simmer, covered, for about 1 ½ hours, stirring occasionally.\nBring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes. Drain noodles, and rinse with cold water.\nIn a mixing bowl, combine ricotta cheese with egg, remaining 2 tablespoons parsley, and 1/2 teaspoon salt.\nPreheat the oven to 375 degrees F (190 degrees C).\nTo assemble, spread 1 ½ cups of meat sauce in the bottom of a 9x13-inch baking dish. Arrange 6 noodles lengthwise over meat sauce, overlapping slightly. Spread with 1/2 of the ricotta cheese mixture. Top with 1/3 of the mozzarella cheese slices. Spoon 1 ½ cups meat sauce over mozzarella, and sprinkle with 1/4 cup Parmesan cheese.\nRepeat layers, and top with remaining mozzarella and Parmesan cheese. Cover with foil: to prevent sticking, either spray foil with cooking spray or make sure the foil does not touch the cheese.\nBake in the preheated oven for 25 minutes. Remove the foil and bake for an additional 25 minutes.\nRest lasagna for 15 minutes before serving.',
                         'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Italian', 'Shrimp Scampi with Pasta',
                            'linguine pasta, butter, extra-virgin olive oil, shallots, garlic, red pepper flakes, shrimp, kosher salt, white wine, lemon, parsley',
                            'Gather ingredients.\nBring a large pot of salted water to a boil; cook linguine in boiling water until nearly tender, 6 to 8 minutes. Drain.\nMelt 2 tablespoons butter with 2 tablespoons olive oil in a large skillet over medium heat.\nCook and stir shallots, garlic, and red pepper flakes in the hot butter and oil until shallots are translucent, 3 to 4 minutes.\nSeason shrimp with kosher salt and black pepper; add to the skillet and cook until pink, stirring occasionally, 2 to 3 minutes. Remove shrimp from skillet and keep warm.\nPour white wine and lemon juice into skillet and bring to a boil while scraping the browned bits of food off of the bottom of the skillet with a wooden spoon.\nMelt 2 tablespoons butter in skillet, stir 2 tablespoons olive oil into butter mixture, and bring to a simmer.\nToss linguine, shrimp, and parsley in the butter mixture until coated; season with salt and black pepper. Drizzle with 1 teaspoon olive oil to serve.\nServe hot and enjoy!',
                         'https://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Italian', 'The Best Meatballs',
                            'ground beef, ground veal, ground pork, Romano cheese, eggs, garlic, parsley, stale bread, water, olive oil',
                            'Gather all ingredients.\nCombine beef, veal, and pork in a large bowl. Mix in cheese, eggs, garlic, parsley, salt, and pepper.\nAdd bread crumbs and slowly mix in water, 1/2 cup at a time, until mixture is moist but still holds its shape (I usually use about 1 1/4 cups of water); shape into meatballs.\nHeat olive oil in a large skillet; add meatballs in batches and cook until browned on all sides, slightly crisp, and cooked through, about 10 to 15 minutes. Drain on paper towels.\n',
                         'https://www.allrecipes.com/recipe/40399/the-best-meatballs/'))

            # Indian Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Indian', 'Butter Chicken (Murgh Makhani)',
                            'garam masala, tandoori masala, Madras curry powder, cumin, cardamom, cayenne pepper, chicken thighs, butter, onion, garlic, lemon juice, ginger, tomato puree, yogurt, cashews, cilantro',
                            'Gather the ingredients.\nMake a spice mix by combining garam masala, tandoori masala, curry powder, cumin, cardamom, cayenne, salt, and black pepper in a small bowl; set aside.\nPlace chicken in a large bowl and add 1/2 of the spice mixture; turn to coat evenly.\nMelt 1 tablespoon butter in a large skillet over medium heat. Add chicken; cook and stir until lightly browned, about 10 minutes. Remove from heat.\nMelt remaining 2 tablespoons butter in a large saucepan over medium heat. Add onion; cook and stir until soft and translucent, about 5 minutes. Stir in remainder of the spice mixture, garlic, lemon juice, and ginger; cook and stir until combined, about 1 minute.\nStir tomato puree into onion mixture and cook, stirring frequently, about 2 minutes. Pour in half-and-half and yogurt. Reduce heat to low and simmer sauce, stirring frequently, about 10 minutes. Remove from heat.\nBlend cashews in a blender until finely ground. Add sauce to the blender; puree until smooth.\nPour blended sauce over chicken in the skillet. Simmer until thickened, 10 to 15 minutes. Garnish with cilantro.',
                         'https://www.allrecipes.com/recipe/246717/indian-butter-chicken-chicken-makhani/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Indian', 'Chicken Tikka Masala',
                            'yogurt, lemon juice, cumin, cinnamon, cayenne pepper, black pepper, ginger, chicken breasts, garlic, jalapeno, paprika, tomato sauce, heavy cream, cilantro',
                            'Combine yogurt, lemon juice, 2 teaspoons cumin, cinnamon, cayenne, black pepper, ginger, and 1 teaspoon salt in a large bowl.\nStir in chicken, cover, and refrigerate for 1 hour.\nPreheat a grill for high heat.\nLightly oil the grill grate. Thread chicken onto skewers, and discard marinade.\nGrill until juices run clear, about 5 minutes on each side.\nMelt butter in a large heavy skillet over medium heat. Sauté garlic and jalapeño for 1 minute. Season with remaining 2 teaspoons cumin, paprika, and remaining 1 teaspoon salt. Stir in tomato sauce and cream. Simmer on low heat until sauce thickens, about 20 minutes.\nAdd grilled chicken, and simmer for 10 minutes. Transfer to a serving platter, and garnish with fresh cilantro.\nServe over rice.',
                         'https://www.allrecipes.com/recipe/45736/chicken-tikka-masala/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Indian', 'Red Lentil Curry',
                            'red lentils, water, vegetable oil, onion, curry paste, curry powder, turmeric, cumin, chili powder, salt, sugar, garlic, ginger, tomato puree',
                            'Gather all ingredients.\nWash lentils in cold water until water runs clear.\nPut lentils in a pot with enough water to cover; bring to a boil and reduce heat to medium-low. Cover and simmer, adding water as needed to keep lentils covered, until tender, 15 to 20 minutes. Drain.\nHeat vegetable oil in a large skillet over medium heat; cook and stir onions in hot oil until caramelized, about 20 minutes.\nMix together curry paste, curry powder, turmeric, cumin, chili powder, salt, sugar, garlic, and ginger in a large bowl; stir into onions.\nIncrease heat to high and cook, stirring constantly, until fragrant, 1 to 2 minutes.\nStir in tomato puree and lentils; cook until warmed through.\nServe and enjoy!',
                         'https://www.allrecipes.com/recipe/16641/red-lentil-curry/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Indian', 'Green Onion Garlic Naan Bread',
                            'bread flour, kosher salt, baking powder, Greek yogurt, garlic, green onions, melted butter',
                            'Place bread flour in a bowl. Add salt and baking powder and give it a good whisk until evenly combined.\nAdd in Greek yogurt gently, followed by garlic and green onions. Take a wooden spoon and slowly start mixing everything together. Keep mixing, stirring, and pressing until a shaggy dough forms.\nTransfer dough to a work surface and use your hands to press dough together. Knead for a few minutes until dough becomes elastic and a little bit sticky. Add a bit more flour as necessary but try to keep extra flour at an absolute minimum. Knead until dough is a little bit stretchy, 3 to 5 minutes.\nWrap in plastic and allow to rest on the counter for 15 to 20 minutes.\nTake a bench scraper and cut into 6 equal pieces. Take 1 portion and roll into a ball. Place onto a generously floured surface. Use a rolling pin to roll out nice and thin, about 1/8 inch or less. Its ok if the naan is not a perfect circle. You will need extra flour for rolling out as the dough is sticky, but try to use as little as possible.\nHeat a cast iron skillet over medium-high heat until hot. Transfer dough circles into the hot dry skillet and cook until little bubbles form on the surface and the underside is lightly browned, about 1 minute. Flip naan over and cook for 1 more minute. Press down slightly with a spatula to increase the heat during cooking. Flip over twice more and cook for an additional 15 seconds per side, but make sure not to overcook to preserve the texture. Naan should still be flexible when you remove it from the skillet onto a plate.\nCover with a kitchen towel to keep warm and moist while you cook the other naan breads. Stack all 6 naan breads on top of each other and keep covered with a kitchen towel.\nWhen you are finished cooking all 6 naan breads, unstack breads and brush the first naan bread on both sides with a little bit of melted butter. Stack second piece of naan on top and only brush the top side. Keep stacking and buttering all the naan breads. Fold each naan into a triangle and serve.',
                         'https://www.allrecipes.com/recipe/8467738/green-onion-garlic-naan-bread/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Indian', 'Golden Butter Rice',
                            'butter, ginger, turmeric, cayenne pepper, brown sugar, salt, basmati rice, water, walnuts, green onions',
                            'Melt butter in a pan or pot with a tight-fitting lid over medium heat. As soon as butter starts to bubble, add in ginger, turmeric, cayenne, brown sugar, and salt. Cook, whisking, for 1 minute.\nAdd rice, and stir until every grain is coated with butter. Stir in water, and bring to a boil over high heat. As soon as it begins to boil, gently shake and swirl the pan to settle rice into an even layer, then reduce heat to medium-low.\nCover tightly and simmer for 15 minutes. Turn off heat, and let rest, covered, for 10 minutes. DO NOT lift the lid or try to stir yet.\nNow, remove the lid and use a fork to fluff and separate rice grains. Season to taste, and serve immediately, garnished with walnuts and green onions',
                         'https://www.allrecipes.com/golden-butter-rice-recipe-8599188'))

            # Mexican Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Mexican', 'The Best Chimichangas',
                            'kosher salt, black pepper, garlic powder, chicken breasts, olive oil, onion, garlic, ancho chili powder, cumin, water, chicken bouillon, green chiles, all-purpose flour, peanut oil, flour Tortillas, refried beans, pepper jack cheese',
                            'Sprinkle salt, pepper, and garlic powder evenly over one side of the chicken breasts.\nHeat olive oil in a large deep skillet over medium-high heat. Add chicken, seasoned side down, into skillet, and cook, undisturbed, until browned, 3 to 4 minutes. Flip chicken over and push to one side of the pan.\nAdd onion, garlic, chili powder, and cumin to the skillet and cook for 1 minute.  Add 2 cups water and bouillon and gently stir until well combined.\nBring mixture to a simmer. Reduce heat, cover, and simmer gently until chicken is no longer pink at the center and juices run clear, about 20 minutes. An instant-read thermometer inserted near the center should read 165 degrees F (74 degrees C).\nRemove chicken from pan and increase heat to medium-high; cook until broth mixture is reduced by about half. Shred chicken and add back to the pan, along with green chiles. Stir until well combined and remove from heat.\nWhisk flour and remaining water together in a small bowl until smooth; set aside. Heat oil for frying in a large saucepan or Dutch oven over medium-high heat to 350 degrees F (175 degrees C). Set a wire rack over a rimmed baking sheet.\nPlace tortilla on work surface and spread about 3 tablespoons beans in the center. Top with 1/4 cup shredded cheese and 1/3 to 1/2 cup well-drained shredded chicken. Brush flour mixture lightly around edges of top half of tortilla. Fold sides of tortilla in just over edges of filling and fold bottom of tortilla up over filling.  Press back on the tortilla to push the filling tightly together and continue to roll upwards. Lightly press the edges of the tortilla to seal tightly and set aside, seam side down. Repeat with remaining ingredients.\nCarefully place 2 burritos into hot oil and cook, turning occasionally, until golden brown and toasted on the outside, about 2 minutes. Drain on the prepared baking sheet. Bring oil back up to temperature and repeat with remaining burritos.\nTop as desired with warm queso, pico de gallo, cilantro and shredded lettuce, or other toppings, and serve immediately.',
                         'https://www.allrecipes.com/the-best-chimichangas-recipe-8637540'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Mexican', 'Traditional Mexican Street Tacos',
                            'corn Tortillas, cooked chicken, cilantro, white onion, guacamole, lime',
                            'Place a paper towel on a microwave-safe plate and top with tortillas; heat in the microwave for 10 seconds.\nPlace chicken in a microwave-safe bowl; heat in the microwave until heated through, 30 seconds to 1 minute.\nLayer chicken, cilantro, onion, and guacamole, in that order, onto each tortilla. Squeeze lime juice over each taco.\n',
                         'https://www.allrecipes.com/recipe/257988/traditional-mexican-street-tacos/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Mexican', 'Enchiladas Verdes',
                            'tomatillos, serrano peppers, garlic, vegetable oil, corn Tortillas, water, chicken bouillon, shredded chicken, lettuce, cilantro, crema, cotija cheese',
                            'Cover a large griddle with aluminum foil and preheat to medium-high.\nCook tomatillos, serrano peppers, and garlic on the hot griddle, turning occasionally, until toasted and blackened — about 5 minutes for garlic, 10 minutes for peppers, and 15 minutes for tomatillos. Remove to a bowl and allow to cool.\nHeat oil in a small, deep skillet to 350 degrees F (175 degrees C).\nLightly fry tortillas, one at a time, in hot oil until warmed through, 3 to 5 seconds per side. Drain on a paper towel-lined plate.\nPlace toasted tomatillos, serrano peppers, and garlic in a blender. Add water and blend until smooth; pour into a saucepan over medium heat and bring to a boil. Dissolve chicken bouillon in the mixture, reduce heat, and cook at a simmer until slightly thickened, about 10 minutes.\nSoak tortillas in sauce, one at a time, for a few seconds. Fill each tortilla with shredded chicken and sprinkle with sauce. Roll up tortillas and place seam-side down in a serving dish.\nSpoon a generous amount of sauce over rolled tortillas. Top with lettuce, cilantro, crema, and cotija cheese. Pour remaining sauce on top or serve on the side',
                         'https://www.allrecipes.com/recipe/213700/enchiladas-verdes/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Mexican', 'Beef Tamales',
                            'boneless chuck roast, garlic, dried corn husks, dried ancho chiles, vegetable oil, all-purpose flour, beef broth, garlic, oregano, cumin seeds, ground cumin, red pepper flakes, vinegar, lard, masa harina',
                            'Place beef and garlic in a large pot. Cover with cold water and bring to a boil over high heat; reduce heat, cover, and simmer until beef is tender and shreds easily, about 3 1/2 hours. Remove beef from pot, reserving 5 cups cooking liquid and discarding garlic. Allow meat to cool slightly; shred finely with forks.\nMeanwhile, place corn husks in a large container and cover with warm water; soak, weighed down with an inverted plate and a heavy can, until soft and pliable, about 3 hours.\nToast ancho chiles in a cast iron skillet; cool, then remove stems and seeds. Crumble and grind in a clean coffee grinder or with a mortar and pestle.\nHeat oil in a large skillet; stir in flour and allow to brown slightly. Pour in 1 cup beef broth and stir until smooth. Mix in ground chiles, garlic, oregano, cumin seeds, ground cumin, red pepper flakes, vinegar, and salt. Stir shredded beef into skillet and cover. Let simmer for 45 minutes.\nPlace lard and salt in a large mixing bowl; beat with an electric mixer on high speed until fluffy. Add masa harina and beat at low speed until well mixed. Pour in reserved cooking liquid, a little at a time, until mixture is the consistency of soft cookie dough.\nDrain water from corn husks. One at a time, flatten out each husk, with the narrow end facing you, and spread approximately 2 tablespoons masa mixture onto the top 2/3 of the husk. Spread about 1 tablespoon of meat mixture down the middle of the masa. Roll up the corn husk starting at one of the long sides. Fold the narrow end of the husk onto the rolled tamale and tie with a piece of butchers twine.\nPlace tamales in a steamer basket. Steam over boiling water for approximately one hour, until masa is firm and holds its shape, adding more water if needed so the steamer does not boil dry. Serve immediately, allowing each person to unwrap their own tamales.',
                         'https://www.allrecipes.com/recipe/34759/beef-tamales/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Mexican', 'Fabulous Wet Burritos',
                            'ground beef, onion, garlic, cumin, salt, pepper, refried beans, green chile peppers, chili, tomato soup, enchilada sauce, flour Tortillas, lettuce, tomatoes, Mexican cheese blend, green onions',
                            'Crumble ground beef into a skillet over medium-high heat. Cook and stir until evenly browned. Add onion and cook until translucent. Drain grease, and season with garlic, cumin, salt, and pepper. Stir in refried beans and green chilies until well blended. Turn off heat but keep warm.\nCombine canned chili, condensed soup, and enchilada sauce in a saucepan. Mix well and cook over medium heat until heated through. Turn off the heat and keep warm.\nPlace warmed tortilla on a plate and spoon a generous 1/2 cup of the ground beef mixture onto the center. Top with a portion of lettuce and tomato to your liking. Roll up tortilla around the filling, while tucking in the sides. Spoon a generous amount of the sauce over the top and sprinkle with a portion of cheese and green onions. Heat in the microwave until cheese is melted, about 30 seconds. Repeat with remaining tortillas and fillings.',
                         'https://www.allrecipes.com/recipe/70404/fabulous-wet-burritos/'))


            # Japanese Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Japanese', 'Chicken Katsu',
                            'chicken breasts, salt, pepper, all-purpose flour, egg, panko bread crumbs, oil for frying',
                            'Season chicken breasts on both sides with salt and pepper. Place flour, beaten egg, and panko crumbs into separate shallow dishes. Coat chicken breasts in flour, shaking off any excess; dip into egg, and then press into panko crumbs until well coated on both sides.\nHeat oil in a large skillet over medium-high heat. Place chicken in the hot oil, and fry until golden brown, 3 or 4 minutes per side. Transfer to a paper towel-lined plate to drain.',
                         'https://www.allrecipes.com/recipe/72068/chicken-katsu/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Japanese', 'Japanese-Style Rolled Omelet (Tamagoyaki)',
                            'eggs, water, soy sauce, mirin, kosher salt, sugar, cayenne pepper, sesame oil, vegetable oil, furikake',
                            'Add eggs to a bowl, along with water, soy sauce, mirin, salt, sugar, and cayenne. Use a fork to beat eggs until whites are completely incorporated. Transfer egg mixture into a pourable measuring cup.\nSet a 10-inch non-stick pan over medium heat. Mix sesame and vegetable oil in a small bowl, and use a brush to oil the pan.\nPour in 1/3 of egg mixture. Tilt the pan to cover the bottom with eggs. Cook until omelet is about halfway set, then use a spatula to turn over about 1 inch of edge toward the center on 3 sides to square the shape on those 3 sides. If eggs seem to be cooking too fast, reduce heat to medium-low. Use a spatula to roll the omelet toward the rounder side, to form a rectangular roll, about 2 inches wide by 8 inches long.\nSlide omelet over to about 3 inches from the edge of the pan, and brush more oil over the pan surface. Pour the second 1/3 of eggs around the omelet. Lift omelet slightly with the spatula so that some eggs flow underneath. Raise heat back to medium, if it was reduced. When egg layer is halfway set, use a spatula to roll this layer up and over the already-folded omelet in the pan, and continue to roll into a rectangle.\nAdd remaining 1/3 of egg mixture, and repeat cooking and rolling steps to make the final layer.\nTransfer omelet onto plastic wrap, and use it to shape the omelet, before wrapping and rolling it into a tight package; cover with a towel and let rest for 5 minutes.\nUnwrap, slice into 6 or 8 pieces, and serve on a warm plate. Sprinkle with furikake.',
                         'https://www.allrecipes.com/japanese-style-rolled-omelet-tamagoyaki-recipe-8644676'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Japanese', 'Onigiri (Japanese Rice Balls)',
                            'short-grain white rice, water, salt, bonito shavings, nori, sesame seeds',
                            'Wash rice in a mesh strainer until water runs clear. Combine washed rice and 4 1/2 cups water in a saucepan. Bring to a boil over high heat, stirring occasionally. Reduce heat to low; cover, and simmer rice until water is absorbed, 15 to 20 minutes. Let rice rest for 15 minutes to continue to steam and become tender. Allow cooked rice to cool.\nCombine remaining 1 cup water with salt in a small bowl; use to dampen hands before handling rice. Divide cooked rice into 8 equal portions. Use one portion of rice for each onigiri.\nDivide one portion of rice in two. Create a dimple in rice and fill with a heaping teaspoon of bonito flakes. Cover with remaining portion of rice and press lightly to enclose filling inside rice ball. Gently press rice to shape into a triangle; wrap with a strip of nori and sprinkle with sesame seeds. Repeat with remaining portions of rice.',
                         'https://www.allrecipes.com/recipe/140422/onigiri-japanese-rice-balls/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Japanese', 'Spicy Tuna Sushi Roll',
                            'glutinous white rice, water, rice vinegar, tuna, mayonnaise, chili powder, wasabi paste, nori, cucumber, carrot, avocado',
                            'Bring the rice, water, and vinegar to a boil in a saucepan over high heat. Reduce heat to medium-low, cover, and simmer until the rice is tender, and the liquid has been absorbed, 20 to 25 minutes. Let stand, covered, for about 10 minutes to absorb any excess water. Set rice aside to cool.\nLightly mix together the tuna, mayonnaise, chili powder, and wasabi paste in a bowl, breaking the tuna apart but not mashing it into a paste.\nTo roll the sushi, cover a bamboo sushi rolling mat with plastic wrap. Lay a sheet of nori, rough side up, on the plastic wrap. With wet fingers, firmly pat a thick, even layer of prepared rice over the nori, covering it completely. Place about 1 tablespoon each of diced cucumber, carrot, and avocado in a line along the bottom edge of the sheet, and spread a line of tuna mixture alongside the vegetables.\nPick up the edge of the bamboo rolling sheet, fold the bottom edge of the sheet up, enclosing the filling, and tightly roll the sushi into a thick cylinder. Once the sushi is rolled, wrap it in the mat and gently squeeze to compact it tightly. Cut each roll into 6 pieces, and refrigerate until served.'
                         ,'https://www.allrecipes.com/recipe/190943/spicy-tuna-sushi-roll/'))


            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('Japanese', 'Miso Soup',
                            'water, dashi granules, miso paste, silken tofu, green onions',
                            'Gather all ingredients.\nCombine water and dashi granules in a medium saucepan over medium-high heat; bring to a boil.\nReduce heat to medium and whisk in miso paste.\nStir in tofu.\nSeparate the layers of green onions, and add them to the soup. Simmer gently for 2 to 3 minutes before serving.'
                         , 'https://www.allrecipes.com/recipe/13107/miso-soup/'))

            # German Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('German', 'German Pork Chops and Sauerkraut',
                            'pork chops, sauerkraut, red apple, onion, brown sugar, caraway seeds',
                            'Preheat the oven to 350 degrees F (175 degrees C).\nHeat a large nonstick skillet over medium-high heat. Brown pork chops on both sides, about 5 minutes per side. Place chops into a 9x13-inch baking dish.\nMix sauerkraut, apple, onion, brown sugar, and caraway seeds in a bowl until well combined, and spread the sauerkraut mixture over the pork chops. Cover the dish with aluminum foil\nBake in the preheated oven until the pork is no longer pink inside, about 45 minutes. An instant-read thermometer inserted into the center of a chop should read 145 degrees F (63 degrees C).',
                         'https://www.allrecipes.com/recipe/216330/german-pork-chops-and-sauerkraut/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('German', 'Creamy Dill German Potato Salad',
                            'yellow potatoes, mayonnaise, Greek yogurt, dill pickle brine, Dijon mustard, eggs, onion, dill pickles',
                            'Add potatoes to a large pot and cover with salted water. Bring to a boil over medium-high heat. Reduce heat to medium-low, and cook until easily pierced with a fork but still firm, 15 to 25 minutes. Drain potatoes, and set aside to cool.\nMeanwhile, whisk the mayonnaise, yogurt, pickle brine, and Dijon mustard together in a large bowl until well blended. Peel and roughly chop 2 of the hard boiled eggs. Stir in chopped eggs, onion, and pickles.\nWhen potatoes are cool enough to handle, peel and cut them into bite-sized pieces. Add potatoes to the bowl with the dressing, and gently toss to coat evenly.\nSeason to taste with salt and pepper, and slice the remaining hard boiled egg for a garnish on the potato salad. May be served immediately or chilled in the fridge.',
                         'https://www.allrecipes.com/creamy-dill-german-potato-salad-recipe-8660093'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('German', 'Wiener Schnitzel',
                            'veal cutlets, all-purpose flour, eggs, Parmesan cheese, milk, parsley, salt, pepper, nutmeg, bread crumbs, butter, lemon',
                            'Place veal cutlets between 2 sheets of heavy plastic on a solid, level surface. Firmly pound cutlets with the smooth side of a meat mallet to a 1/4-inch thickness. Dip cutlets in flour to coat; shake off excess.\nBeat eggs, Parmesan cheese, milk, parsley, salt, pepper, and nutmeg together in a shallow bowl until combined. Place bread crumbs on a plate.\nDip each cutlet into the egg mixture, then press in bread crumbs to coat. Place coated cutlets on a plate and refrigerate for 1 hour to overnight.\nMelt butter in a large skillet over medium heat. Cook breaded cutlets in butter until browned, about 3 minutes per side. Transfer cutlets to a serving platter and pour pan juices over them. Garnish with lemon slices.',
                         'https://www.allrecipes.com/recipe/78117/wienerschnitzel/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('German', 'German Zwiebelkuchen (Onion Pie)',
                            'onions, bacon, sour cream, eggs, all-purpose flour, salt, caraway seed, pastry for pie',
                            'Preheat the oven to 425 degrees F (220 degrees C). Line a 15x10-inch pan or large pizza pan with prepared dough, making sure dough extends up sides of pan.\nSauté onion in a skillet until translucent and pour cooked onion into a large mixing bowl. Place bacon in a large, deep skillet. Cook over medium high heat until evenly brown. Drain, chop and add to onion; mix well.\nStir in sour cream. Beat eggs enough to break up yolks, then mix in to pie mixture. Add flour to thicken mixture (onions will create a lot of water), then add salt. Mix well and pour mixture into prepared pan. Sprinkle top with caraway seed.\nBake in preheated oven until onions start to turn golden brown on top, about 1 hour.',
                         'https://www.allrecipes.com/recipe/24674/german-zwiebelkuchen-onion-pie'))
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
                        ('German', 'German Currywurst',
                            'tomato sauce, kielbasa, chili sauce, onion salt, white sugar, black pepper, paprika, curry powder',
                            'Preheat oven to Broil/Grill.\nPour tomato sauce into a large saucepan, then stir in the chili sauce, onion salt, sugar and pepper. Let simmer over medium heat, occasionally stirring; bring to a gentle boil and reduce heat to low. Simmer another 5 minutes.\nMeanwhile, broil/grill kielbasa sausage for 3 to 4 minutes each side, or until cooked through. Slice into pieces 1/4 inch to 1/2 inch thick.\nPour tomato sauce mixture over sausage, then sprinkle all with paprika and curry powder and serve.',
                         'https://www.allrecipes.com/recipe/24676/german-currywurst/'))
            #Template(delete later)
            #self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
            #                    ('', '',
            #                     '',
            #                     ''))
            #Chinese Dishes
            #self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, directions, link) VALUES (?, ?, ?, ?, ?)',
            #                    ('Chinese', '4-Ingredient Orange Chicken',
            #                     'orange marmalade, Kansas City-style BBQ sauce, low sodium soy sauce, bag frozen fully cooked chicken nuggets, sliced green onions (optional), sesame seeds (optional)',
            #                     'Preheat the oven to 400 degrees F (200 degrees C). Place frozen nuggets in a single layer on a baking sheet.\nBake in the preheated oven until hot and crispy, 11 to 13 minutes, or according to package directions.\nMeanwhile, whisk marmalade, BBQ sauce, and soy sauce together in a small saucepan and heat over low heat until hot, about 5 minutes.\nPlace nuggets in a large bowl. Drizzle sauce over the top. Toss to coat.',
            #                     'https://www.allrecipes.com/4-ingredient-orange-chicken-recipe-8713472'))

            # Commit the changes
            self.connection.commit()

        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_all_recipes(self):
        """
        Retrieves all recipes from the Cuisines table in the database.
        Returns:
            list: A list of tuples, where each tuple represents a row in the Cuisines table.
        """
        
        self.cursor.execute("SELECT * FROM Cuisines")
        return self.cursor.fetchall()
    
    def get_favorite_status(self, recipe_name):
        """
        Retrieves the favorite status of a recipe from the database.

        Args:
            recipe_name (str): The name of the recipe to check.

        Returns:
            int: 1 if the recipe is marked as favorite, 0 otherwise.
        """
        self.cursor.execute("SELECT is_favorite FROM Cuisines WHERE rec_name = ?", (recipe_name,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def set_favorite_status(self, recipe_name, status: int):
        """
        Updates the favorite status of a recipe in the database.

        Args:
            recipe_name (str): The name of the recipe to update.
            status (int): The new favorite status (e.g., 1 for favorite, 0 for not favorite).

        Returns:
            None
        """
        self.cursor.execute("UPDATE Cuisines SET is_favorite = ? WHERE rec_name = ?", (status, recipe_name))
        self.cursor.connection.commit()

    def __close(self):
        self.cursor.close()
        self.connection.close()



    def get_favorite_recipes(self):
        """
        Fetches and returns a list of favorite recipes from the Cuisines table.
        """
        
        self.cursor.execute("SELECT rec_name, ingredients_list, link FROM Cuisines WHERE is_favorite = 1")
        results = self.cursor.fetchall()
        return [(rec_name, ingredients_list, link) for rec_name, ingredients_list, link in results]

    def search_recipes(self, recipe_name, ingredients="", cuisine_selected=""):
        """
        Searches for recipes in the database based on the given criteria.
        Args:
            recipe_name (str): The name of the recipe to search for.
            ingredients (str, optional): A string of ingredients to filter the recipes. Defaults to an empty string.
            cuisine_selected (str, optional): The type of cuisine to filter the recipes. Defaults to an empty string.
            If 'All' is provided, it will be treated as an empty string.
        Returns:
            list[tuple]: A list of tuples where each tuple contains the cuisine type, recipe name, ingredients list, and link.
            """
        if cuisine_selected == 'All':
            cuisine_selected == ""
        query = """
        SELECT rec_name, ingredients_list, link 
        FROM Cuisines 
        WHERE rec_name LIKE ? AND ingredients_list LIKE ? AND cui_type LIKE ?
        """

        self.cursor.execute(query, (f'%{recipe_name}%', f'%{ingredients}%', f'%{cuisine_selected}%'))
        results = self.cursor.fetchall()

        return [("cui_type", rec_name, ingredients_list, link) for  rec_name, ingredients_list, link in results]

if __name__ == "__main__":
    data = Database()
    print(data.search_recipes("", "", "All"))
    data.close()


