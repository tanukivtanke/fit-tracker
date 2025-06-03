

const selectedItems = {};

const selectItem = (type, id) => {
    let list = selectedItems[type] ?? [];
    if (!list.includes(id)) {
        list.push(id);
        selectedItems[type] = list;
    } else {
        selectedItems[type] = list.filter(i => i !== id);
    }
};

const isItemSelected = (type, id) => {
    return selectedItems[type]?.includes(id) ?? false;
};

const isSelectionActive = (type) => {
    return selectedItems[type]?.length > 0;
};

const getSelectedItems = (type) => {
    return selectedItems[type] ?? [];
};

const clearSelection = (type) => {
    selectedItems[type] = [];
};

class SelectionType {
    static MEAL = 'MEAL';
    static DISH_INGREDIENT = 'DISH_INGREDIENT';
}

const setupLongPress = (element, callback, duration = 250) => {
    let timer;
    let isLongPressActive = false;
    let skipContextMenu = false;
    let startX, startY;
    const moveThreshold = 10; // pixels of movement allowed before canceling long press

    // Handle mouse events
    element.addEventListener('mousedown', (e) => {
        //console.log('mousedown')
        timer = setTimeout(() => {
            isLongPressActive = true;
            callback(e);
        }, duration);
    });

    element.addEventListener('mouseup', () => {
        //console.log('mouseup')
        clearTimeout(timer);
        isLongPressActive = false;
    });

    element.addEventListener('mouseleave', () => {
        //console.log('mouseleave')
        clearTimeout(timer);
        isLongPressActive = false;
    });

    // Handle touch events for mobile
    element.addEventListener('touchstart', (e) => {
        //console.log('touchstart');
        // Store the initial touch position
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        
        timer = setTimeout(() => {
            isLongPressActive = true;
            skipContextMenu = true;
            callback(e);
        }, duration * 1.7);
    });

    element.addEventListener('touchmove', (e) => {
        //console.log('touchmove');
        
        // Get current touch position
        const currentX = e.touches[0].clientX;
        const currentY = e.touches[0].clientY;
        
        // Calculate distance moved
        const deltaX = Math.abs(currentX - startX);
        const deltaY = Math.abs(currentY - startY);
        
        // Check if the touch has moved beyond the threshold
        if (deltaX > moveThreshold || deltaY > moveThreshold) {
            // Movement exceeds threshold, cancel the long press
            clearTimeout(timer);
            isLongPressActive = false;
        }
    });
    
    element.addEventListener('touchend', () => {
        //console.log('touchend')
        clearTimeout(timer);
        isLongPressActive = false;
    });

    element.addEventListener('touchcancel', () => {
        //console.log('touchcancel')
        clearTimeout(timer);
        isLongPressActive = false;
    });

    // Prevent context menu on long press
    element.addEventListener('contextmenu', (e) => {
        //console.log('contextmenu')
        if (isLongPressActive || skipContextMenu) {
            skipContextMenu = false;
            e.stopPropagation();
            e.preventDefault();
        }
    });
};
