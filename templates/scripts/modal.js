
class Modal {
    #oldOkText;
    #oldDeleteText;
    #oldOkDisabled;
    #oldDeleteDisabled;

    constructor(modalId, title='', okHidden=true, deleteHidden=true, cancelHidden=false) {
        this.modalId = `${modalId}-modal`;
        this.bodyId = `${this.modalId}-body`;
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

        let wrapper = byId(`wrapper-${this.modalId}`)
        if (wrapper) {
            wrapper.innerHTML = `
            <div class="modal fade" id="${this.modalId}" ${deleteHidden ? 'data-bs-backdrop="static" data-bs-keyboard="false"' : '' }
                 tabindex="-1" aria-labelledby="${this.modalId}-title" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="${this.modalId}-title">${title}</h1>
                            <button tabindex="-1" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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

        this.modalObj.addEventListener('hide.bs.modal', event => {
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
}
