// Sets a cookie with the given key and value.
function setCookie(key, value) {
    let date = new Date();
    date.setFullYear(date.getFullYear() + 10); // Sets the date 10 years into the future.
    let expires = "expires=" + date.toUTCString();
    document.cookie = key + "=" + value + ";" + expires + ";path=/";
}

// Returns the value of the cookie with the given key, or null if the cookie does not exist.
function getCookie(key, defaultValue) {
    let name = key + "=";
    let cookies = document.cookie.split(';');
    for(let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return defaultValue !== undefined ? defaultValue : null;
}

// Checks if a cookie with the given key exists.
function hasCookie(key) {
    return getCookie(key) !== null;
}

function deleteCookie(name) {
    setCookie(name, '', -1);
}
