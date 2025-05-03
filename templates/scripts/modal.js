
class Modal {
    #oldOkText;
    #oldDeleteText;
    #oldOkDisabled;
    #oldDeleteDisabled;
    #titleId;
    #titleBtnsId;
    #closeCrossId;

    constructor(modalId, title='', okHidden=true, deleteHidden=true, cancelHidden=false, allowOutsideClick=false) {
        this.modalId = `${modalId}-modal`;
        this.bodyId = `${this.modalId}-body`;
        this.#titleId = `${this.modalId}-titleId`;
        this.#titleBtnsId = `${this.modalId}-titleBtnsId`;
        let button =  byId(`button-${this.modalId}`);
        if (button) {
            if (!title) {
                title = button.innerText;
            }
            if (!button.hasAttribute("data-bs-toggle")) {
                button.setAttribute("data-bs-toggle", 'modal');
            }
            if (!button.hasAttribute('data-bs-target')) {
                button.setAttribute('data-bs-target', `#${this.modalId}`);
            }
        }

        this.#closeCrossId = `${this.modalId}-closeCrossId`;

        if (!deleteHidden) {
            allowOutsideClick = true;
        }

        let wrapper = byId(`wrapper-${this.modalId}`)
        if (wrapper) {
            wrapper.innerHTML = `
            <div class="modal fade" id="${this.modalId}" ${!allowOutsideClick ? 'data-bs-backdrop="static" data-bs-keyboard="false"' : '' }
                 tabindex="-1" aria-labelledby="${this.modalId}-title" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <div id="${this.#titleId}">
                                <h1 class="modal-title fs-5" id="${this.modalId}-title">${title}</h1>
                            </div>
                            <div id="${this.#titleBtnsId}" class="d-none w-100">
                                <div class="d-flex gap-2 justify-content-between w-100">
                                    <div class="d-flex gap-2">
                                        <button id="${this.#titleBtnsId}-move-button" class="btn btn-sm btn-secondary">${Icons.move} Переместить</button>
                                        <button id="${this.#titleBtnsId}-copy-button" class="btn btn-sm btn-secondary">${Icons.copy} Дублировать</button>
                                    </div>
                                    <div class="d-flex gap-2">
                                        <button id="${this.#titleBtnsId}-delete-button" class="btn btn-sm btn-danger">${Icons.delete} Удалить</button>
                                    </div>
                                </div>
                            </div>
                            
                           <button id="${this.#closeCrossId}" tabindex="-1" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div id="${this.bodyId}" class="modal-body">
                        </div>
                        <div class="modal-footer">
                            <button id="${this.modalId}-cancel-button" type="button" class="btn btn-secondary ${cancelHidden ? 'd-none' : ''}" data-bs-dismiss="modal">Отменить</button>
                            <button id="${this.modalId}-delete-button" type="button" class="btn btn-danger ${deleteHidden ? 'd-none' : ''}">Удалить</button>
                            <button id="${this.modalId}-ok-button" type="button" class="btn btn-primary ${okHidden ? 'd-none' : ''}">Подтвердить</button>
                        </div>
                    </div>
                </div>
            </div>`;
        }

        this.modalObj = byId(this.modalId);
        this.modalBody = byId(`${this.bodyId}`);
        this.okButton = byId(`${this.modalId}-ok-button`);
        this.deleteButton = byId(`${this.modalId}-delete-button`);
        this.cancelButton = byId(`${this.modalId}-cancel-button`);

        this.titleMoveButton = byId(`${this.#titleBtnsId}-move-button`);
        this.titleCopyButton = byId(`${this.#titleBtnsId}-copy-button`);
        this.titleDeleteButton = byId(`${this.#titleBtnsId}-delete-button`);

        this.modalOpened = false;

        this.modalBs = new bootstrap.Modal(this.modalObj);

        this.onOpenListeners = [];
        this.onCloseListeners = [];
        this.onOkListeners = [];
        this.onDeleteListeners = [];

        this.modalObj.addEventListener('show.bs.modal', event => {
            this.modalOpened = true;
            this.onOpenListeners.forEach(s => s(event));
        });

        this.modalObj.addEventListener('hide.bs.modal', event => {
            this.modalOpened = false;
            this.onCloseListeners.forEach(s => s(event));
        });

        this.modalObj.addEventListener('hidden.bs.modal', event => {
            this.modalOpened = false;

            if (okHidden) {
                hideElem(this.okButton.id);
            } else {
                showElem(this.okButton.id);
            }

            if (deleteHidden) {
                hideElem(this.deleteButton.id);
            } else {
                showElem(this.deleteButton.id);
            }

            if (cancelHidden) {
                hideElem(this.cancelButton.id);
            } else {
                showElem(this.cancelButton.id);
            }
        });

        this.modalObj.addEventListener('hidden.bs.modal', event => {
            this.setText("");
        });

        this.okButton.addEventListener('click', event => {
            if (this.isOpen()) {
                this.onOkListeners.forEach(s => s(event));
            }
        });

        this.deleteButton.addEventListener('click', event => {
            if (this.isOpen()) {
                this.onDeleteListeners.forEach(s => s(event));
            }
        });
    }

    hideCrossOnMobile() {
        byId(this.#closeCrossId).classList.add('hide-on-mobile');
    }

    isOpen() {
        return this.modalOpened;
    }

    setHtml(html) {
        this.modalBody.innerHTML = html;
    }

    setText(text) {
        this.modalBody.innerText = text;
    }

    hide() {
        this.modalBs.hide();
    }

    show() {
        this.modalBs.show();
    }

    onOpen(func) {
        this.onOpenListeners.push(func);
    }

    onClose(func) {
        this.onCloseListeners.push(func);
    }

    onOkClick(func) {
        this.onOkListeners.push(func);
    }

    onDeleteClick(func) {
        this.onDeleteListeners.push(func);
    }

    setupTitle(type) {
        if (isSelectionActive(type)) {
            hideElem(this.#titleId);
            hideElem(this.#closeCrossId);
            showElem(this.#titleBtnsId);
        } else {
            showElem(this.#titleId);
            showElem(this.#closeCrossId);
            hideElem(this.#titleBtnsId);
        }
    }
}
