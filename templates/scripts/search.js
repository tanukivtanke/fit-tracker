

const engRow = `qwertyuiop[]asdfghjkl;'zxcvbnm,./` + '`';
const rusRow = `йцукенгшщзхъфывапролджэячсмитьбю.` + 'ё';

const russianToEnglish = {};
const englishToRussian = {};

for (let i = 0; i < engRow.length; i++) {
    russianToEnglish[rusRow[i]] = engRow[i];
    englishToRussian[engRow[i]] = rusRow[i];
}

class SearchFilter {

    static search(list, stringRepresentationFn, query) {
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

        return list.sort((a, b) => {
            if (a.is_deleted && b.is_deleted) {
                return a.id - b.id;
            }
            if (a.is_deleted) {
                return -1;
            }
            if (b.is_deleted) {
                return 1;
            }
            return a.id - b.id;
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
