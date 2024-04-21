const DateTime = luxon.DateTime;
let currentDate = DateTime.local().setLocale('ru');
const nowDate = currentDate;


const byId = id => document.getElementById(id);
const log = (...messages) => {
    const now = DateTime.now().toFormat("yyyy-MM-dd | HH:mm |");
    console.log(now, ...messages);
};


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

async function _fetch(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('Failed to fetch meals');
    }
    return await response.json();
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

    static makeRow(inside, {fs = 5, py = 2, ps = 3, pe = 2} = {}) {
        return `
        <div class="row mb-2">
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

    static switch(id, labelId, text, checked, enabled=true) {
        return `
        <div class="form-check form-switch fs-5 d-flex align-items-center">
          <input class="form-check-input" type="checkbox" role="switch" 
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
          <textarea class="form-control" placeholder="123" id="${id}" style="height: 100px"></textarea>
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


