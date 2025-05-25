

const engRow = `qwertyuiop[]asdfghjkl;'zxcvbnm,./` + '`';
const rusRow = `йцукенгшщзхъфывапролджэячсмитьбю.` + 'ё';

const russianToEnglish = {};
const englishToRussian = {};

for (let i = 0; i < engRow.length; i++) {
    russianToEnglish[rusRow[i]] = engRow[i];
    englishToRussian[engRow[i]] = rusRow[i];
}

class SearchFilter {

    /**
     * @template T
     * @param {T[]} list
     * @param stringRepresentationFn
     * @param query
     * @param reverse
     * @returns {T[]}
     */
    static search(list, stringRepresentationFn, query, reverse=false) {
        // Helper function to convert query between Russian and English
        function convertQuery(q) {
            return q.split('').map(char =>
                russianToEnglish[char] || englishToRussian[char] || char
            ).join('');
        }

        // Helper function to check if all query parts are in the string
        function allPartsInString(queryParts, str) {
            return queryParts.every(part => str.includes(part));
        }

        // Helper function to normalize the string
        function normalizeString(str) {
            return str.toLowerCase()
                      .replace(/ё/g, 'е')
                      .replace(/й/g, 'и')
                      .trim();
        }

        const originalQueryParts = normalizeString(query).split(/\s+/);
        const convertedQueryParts = originalQueryParts.map(convertQuery).map(normalizeString);

        let revMult = reverse ? -1 : 1;

        return list.sort((a, b) => {
            if (a.out_of_stock !== undefined) {
                if (a.out_of_stock && b.out_of_stock) {
                    return (a.id - b.id) * revMult;
                }
                if (a.out_of_stock) {
                    return -1 * revMult;
                }
                if (b.out_of_stock) {
                    return 1 * revMult;
                }
                return (a.id - b.id) * revMult;


            } else {
                if (a.is_deleted && b.is_deleted) {
                    return (a.id - b.id) * revMult;
                }
                if (a.is_deleted) {
                    return -1 * revMult;
                }
                if (b.is_deleted) {
                    return 1 * revMult;
                }
                return (a.id - b.id) * revMult;
            }


        }).filter(item => {
            const itemString = normalizeString(stringRepresentationFn(item));
            const convertedItemString = normalizeString(convertQuery(itemString));

            return allPartsInString(originalQueryParts, itemString) ||
                   allPartsInString(convertedQueryParts, itemString) ||
                   allPartsInString(originalQueryParts, convertedItemString) ||
                   allPartsInString(convertedQueryParts, convertedItemString);
        });
    }

}

const ALWAYS_FALSE = () => false;
const ALWAYS_TRUE = () => true;

const getItemsList = (
    {
        currDish = null,
        foodFilter = food => !food.is_deleted,
        dishFilter = (dish, parents) => !dish.out_of_stock,
    } = {}) => {

    let elems = [];
    // Collect all valid foods
    if (foodFilter !== ALWAYS_FALSE) {
        for (let food of Object.values(allFoods)) {
            if (foodFilter(food)) {
                elems.push({
                    type: 'FOOD',
                    id: food.id,
                    name: food.name,
                    last_used: food.last_used || null
                });
            }
        }
    } else {
        console.log("Skipped foods");
    }


    let dishParents = currDish ? [currDish.id] : [];
    {
        let dish = currDish;
        while (dish && dish.for_dish) {
            dishParents.push(dish.for_dish);
            dish = allDishes[dish.for_dish];
        }
    }

    // Collect all valid dishes
    for (let dish of Object.values(allDishes)) {
        if (dishParents.includes(dish.id)) {
            continue;
        }
        if (dishFilter(dish, dishParents)) {
            elems.push({
                type: 'DISH',
                id: dish.id,
                name: getDishFullName(dish.id),
                last_used: dish.last_used || null,
                for_dish: dish.for_dish || null
            });
        }
    }

    // Sort the elements based on your criteria
    elems.sort((a, b) => {
        if (a.for_dish && !b.for_dish || !a.for_dish && b.for_dish) {
            if (a.for_dish) {
                return -1;
            } else {
                return 1;
            }
        }

        if (a.last_used && b.last_used) {
            // Both have last_used; sort by most recent date first
            const dateDiff = new Date(b.last_used) - new Date(a.last_used);
            if (dateDiff !== 0) {
                return dateDiff;
            } else {
                // Dates are the same; compare ids in decreasing order
                return b.id - a.id;
            }
        } else if (a.last_used) {
            // Only 'a' has last_used; it comes before 'b'
            return -1;
        } else if (b.last_used) {
            // Only 'b' has last_used; it comes before 'a'
            return 1;
        } else {
            // Neither has last_used; sort by id in decreasing order
            return b.id - a.id;
        }
    });

    return elems;
}
