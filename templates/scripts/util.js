const DateTime = luxon.DateTime;
let currentDate = DateTime.local().setLocale('ru');
const nowDate = currentDate;


const byId = id => document.getElementById(id);
const log = (...messages) => {
    const now = DateTime.now().toFormat("yyyy-MM-dd | HH:mm |");
    console.log(now, ...messages);
};


$(document).on('select2:open', () => {
    document.querySelector('.select2-search__field').focus();
});

const hideElem = elem => {
    if (typeof elem === 'string') {
        elem = byId(elem);
    }
    elem.classList.add('d-none');
};
const showElem = elem => {
    if (typeof elem === 'string') {
        elem = byId(elem);
    }
    elem.classList.remove('d-none');
};

const addListener = (id, event, func) => {
    const elem = typeof id === typeof "" ? byId(id) : id;
    elem.addEventListener(event, () => func(elem));
};
const onLoad = func => addListener(window, 'load', func);
const onInput = (id, func) => addListener(id, 'input', func);
const onChange = (id, func) => addListener(id, 'change', func);
const onClick = (id, func) => addListener(id, 'click', func);

const query = (q, func) => {
    document.querySelectorAll(q).forEach(e => func(e));
};


function extractNumber(str,  {trimZeros = true} = {}) {
    // Extract only numbers
    let numbers = str.match(/\d+/g);

    if (!numbers) {
        return '';
    }

    const res = numbers.join('');
    if (res === '00') {
        return '0';
    }
    if (res === '0') {
        return res;
    }
    if (trimZeros) {
        return res.replace(/^0+/, '');
    } else {
        return res;
    }
}


function handleNumberField(fieldId, min=null, max=null, trimZeros=true, defaultValue=null, allowNegative=false) {
    let elem;
    if (typeof fieldId === typeof '') {
        elem = byId(fieldId);
    } else {
        elem = fieldId;
    }

    let newValue = elem.value;
    let isNegative = allowNegative && newValue[0] === '-';
    if (isNegative && newValue === '-') {
        return defaultValue;
    }

    let fixed = extractNumber(newValue, {trimZeros: trimZeros});

    let maxLen = `${max}`.length;
    if (max !== null && fixed.length > maxLen) {
        fixed = fixed.substring(0, maxLen);
    }
    if (max !== null && fixed.length > 0 && parseInt(fixed) > max) {
        fixed = `${max}`;
    }
    if (min !== null && fixed.length > 0 && parseInt(fixed) < min) {
        fixed = `${min}`;
    }
    if (isNegative) {
        fixed = "-" + fixed;
    }
    if (fixed !== newValue) {
        elem.value = fixed;
    }
    fixed = parseInt(fixed);
    return Number.isInteger(fixed) ? fixed : defaultValue;
}


function handleFloatField(fieldId, min=null, max=null, autoDot=false) {
    let elem;
    if (typeof fieldId === typeof '') {
        elem = byId(fieldId);
    } else {
        elem = fieldId;
    }

    let newValue = elem.value;

    let cleaned = newValue.replace(/[^0-9.]/g, '');

    if (cleaned === ".") {
        cleaned = "0.";
    }

    cleaned = cleaned.replace(/^\.+/, '');
    cleaned = cleaned.replace(/^0+/, '0');

    if (cleaned.length > 1 && cleaned.startsWith("0") && !cleaned.startsWith("0.")) {
        cleaned = "0";
    }

    if (cleaned.length > 0) {
        let parts = cleaned.split('.');

        if (parts.length > 1) {
            // Take the first part (stripping leading zeros) and the first digit of the second part only
            cleaned = parts[0] + '.' + parts[1].substring(0, 1);
        } else {
            // If there is no dot, still strip leading zeros
            cleaned = parts[0];
        }

        let float = parseFloat(cleaned);

        if (max != null && float > max) {
            if (autoDot && float / 10 < max) {
                float /= 10;
                cleaned = parseInt(float) + "." + Math.round((float - parseInt(float)) * 10);
            } else {
                cleaned = "" + max;
            }
        }
        if (min != null && float < min) {
            cleaned = "" + min;
        }
    }

    if (newValue !== cleaned) {
        elem.value = cleaned;
    }

    return cleaned ? parseFloat(cleaned) : null;
}


const shiftDateByOneDay = (date, forward) => {
  if (forward) {
    return date.plus({ days: 1 });
  } else {
    return date.minus({ days: 1 });
  }
}

const mapToId = (array) => {
    return array.reduce((acc, item) => {
      acc[item.id] = item;
      return acc;
    }, {});
}

let _reqId = 0;

async function _fetch(url) {

    let reqId = ++_reqId;
    console.log(`[${reqId}] GET ${url}`);

    const response = await fetch(url);
    if (!response.ok) {
        console.log(`[${reqId}] RESPONSE ${response.ok}`);
        throw new Error('Failed to fetch meals');
    }

    let res = await response.json();

    console.log(`[${reqId}] RESPONSE ${response.ok} ${JSON.stringify(res)}`);

    return res;
}

async function _post(url, json) {

    let reqId = ++_reqId;
    console.log(`[${reqId}] POST ${url} ${JSON.stringify(json)}`);

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });

    if (!response.ok) {
        console.log(`[${reqId}] RESPONSE ${response.ok}`);
        throw new Error('Failed to fetch meals');
    }

    let res = await response.json();

    console.log(`[${reqId}] RESPONSE ${response.ok} ${JSON.stringify(res)}`);

    return res;
}

async function _delete(url, json) {

    let reqId = ++_reqId;
    console.log(`[${reqId}] DELETE ${url}`);

    const response = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });

    if (!response.ok) {
        console.log(`[${reqId}] RESPONSE ${response.ok}`);
        throw new Error('Failed to fetch meals');
    }

    let res = await response.json();

    console.log(`[${reqId}] RESPONSE ${response.ok} ${JSON.stringify(res)}`);

    return res;
}




class HtmlPresets {
    static spinner = `
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>`;

    static spinnerCenter() {
        return `
        <div class="d-flex align-items-center justify-content-center w-100">
             ${HtmlPresets.spinner}
        </div>
        `;
    }

    static middleAbsoluteSpinner(forcedRatio=null) {
        return `
        <div class="d-flex align-items-center justify-content-center h-100 w-100 position-absolute" data-loader
                    ${forcedRatio !== null ? `style="aspect-ratio: ${forcedRatio};"` : ''}>
             ${HtmlPresets.spinner}
        </div>
        `;
    }

    static makeSpinnerSpan(classes='') {
        return `<span class="spinner-border spinner-border-sm ${classes}" aria-hidden="true"></span>`
    }

    static hostLink(url) {
        return `https://${window.location.hostname}${url}`;
    }

    static newTabLink = `target="_blank" rel="noopener noreferrer"`;

    static makeRow(inside, {fs = 5, py = 2, ps = 3, pe = 2, id=''} = {}) {
        return `
        <div ${id ? `id="${id}"` : ''} class="row mb-2">
            <div class="col">
                <div class="py-${py} ps-${ps} pe-${pe} fs-${fs} border border-dark rounded-2 d-flex justify-content-between align-items-center div-hover">
                    ${inside}
                </div>
            </div>
        </div>
        `;
    }

    static select(id, enabled, inside, styles='', classes='') {
        return `
        <div class="d-inline-block form-floating mb-1" ${styles ? `style="${styles}"` : ''}>
            <select id="${id}" class="form-select py-1 border-dark border-opacity-50 ${classes}" 
                style="height: auto; min-height: auto" ${enabled ? '' : 'disabled'}>
                ${inside}
            </select>
        </div>`;
    }

    static option(value, selected, name, enabled=true) {
        return `
        <option value="${value}" ${selected ? "selected" : ""} ${enabled ? '' : 'disabled'}>${name}</option>
        `;
    }

    static switch(id, labelId, text, checked, enabled=true, fs=5, data) {
        return `
        <div class="form-check form-switch fs-${fs} d-flex align-items-center">
          <input class="form-check-input" type="checkbox" role="switch" ${data}
            ${id ? `id="${id}"` : ''}
            ${checked ? 'checked' : ''} 
            ${enabled ? '' : 'disabled'}
          >
          
          ${id
             ? `<label ${labelId ? `id="${labelId}"` : ''} class="form-check-label ms-2" for="${id}">${text}</label>`
             : ''
          }
        </div>`;
    }

    static textarea(id, label) {
        return `
        <div class="form-floating">
          <textarea class="form-control" placeholder="123" id="${id}" style="height: 200px"></textarea>
          <label for="${id}">${label}</label>
        </div>
        `;
    }

    static datePicker(id, resetId=null, multipleDates=true) {
        return `
        <div class="row align-items-baseline">
            <div class="col">
                <input class="border border-dark border-opacity-50 rounded-2 p-1 text-center" 
                    id="${id}" type="text" placeholder="Выберите дат${multipleDates ? 'ы' : 'у'}" data-input>
                 ${resetId 
                    ? `<i id="${resetId}" 
                          class="fa-solid fa-xmark border border-dark border-opacity-50 rounded-2 p-1"></i>`
                    : ''
                 }
            </div>
        </div>
        `;
    }

    static statusLed(isOk) {
        return `
        <div class="rounded-circle ${isOk ? 'bg-success' : 'bg-danger'} glowing-circle me-2" 
            style="min-height: 0.8rem; min-width: 0.8rem;"></div>
        `;
    }

    static bordered(text) {
        return `
        <div class="d-inline-block border border-dark border-opacity-50 rounded-2 p-1 me-1">${text}</div>
        `;
    }

    static copyToClipboard(rootId, text) {
        const clipboardId = `${rootId}-copy-clipboard`;
        const textId = `${clipboardId}-text`;
        const copiedId = `${clipboardId}-copied`;

        return `
        <span id="${clipboardId}">
            <span id="${textId}" class="fw-bold">${text}</span>
            <i class="fa-regular fa-clipboard mx-2"></i>
            <span id="${copiedId}" class="d-none">Скопировано!</span>
        </span>`;
    }

    static handleCopyToClipboard(rootId) {
        const clipboardId = `${rootId}-copy-clipboard`;
        const textId = `${clipboardId}-text`;
        const copiedId = `${clipboardId}-copied`;

        tippy(`#${clipboardId}`, {
            content: 'Кликните для копирования!',
        });

        let timeout;

        byId(clipboardId).addEventListener('click', function() {
            // Copy bot username to clipboard
            navigator.clipboard.writeText(byId(textId).innerText).then(function() {
                // Show the copied message
                showElem(copiedId);

                if (timeout) {
                    clearTimeout(timeout);
                }

                // Hide the message after 5 seconds
                timeout = setTimeout(function() {
                    if (byId(copiedId) != null) {
                        hideElem(copiedId);
                    }
                }, 5000);
            }).catch(function(error) {
                console.error('Error copying text: ', error);
            });
        });
    }
}






const adjustSpacing = () => {
  document.querySelectorAll('.low-line-height').forEach(el => {
    const style = window.getComputedStyle(el);
    const lineHeight = parseFloat(style.lineHeight);
    const fontSize = parseFloat(style.fontSize);
    const elHeight = el.clientHeight;

    // Calculate the number of full lines using floor.
    const lines = Math.floor(elHeight / lineHeight);

    // Reset any previously set padding.
    el.style.paddingTop = '';
    el.style.paddingBottom = '';

    console.log('lines:', lines, 'elHeight:', elHeight, 'lineHeight:', lineHeight);

    if (lines > 1) {
      // If you’re aiming to mimic a “normal” line-height (e.g. 1.4)
      // for the first and last lines when the inner lines use 0.9,
      // then calculate the missing space.
      const desiredLineHeight = 1.4;
      const currentInnerLineHeight = 0.9;
      const extraSpace = (desiredLineHeight - currentInnerLineHeight) * fontSize;

      // Add half the extra space to the top and half to the bottom.
      // el.style.paddingTop = (extraSpace / 2) + 'px';
      el.style.paddingBottom = (extraSpace / 2) + 'px';
    }
  });
}


const generateUUID = () => { // Public Domain/MIT
    let d = new Date().getTime();//Timestamp
    let d2 = ((typeof performance !== 'undefined') && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        let r = Math.random() * 16;//random number between 0 and 16
        if(d > 0){//Use timestamp until depleted
            r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {//Use microseconds since page-load if supported
            r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
};

