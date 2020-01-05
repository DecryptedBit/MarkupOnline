const modal = document.querySelector("#settings-modal");
const modal_overlay = document.querySelector("#modal-overlay");
const close_btn = document.querySelector("#close-settings-modal");
const open_btn = document.querySelector("#open-settings-modal");

close_btn.addEventListener("click", () => {
    modal.classList.toggle("modal-closed");
    modal_overlay.classList.toggle("modal-closed");
});

open_btn.addEventListener("click", () =>  {
    modal.classList.toggle("modal-closed");
    modal_overlay.classList.toggle("modal-closed");
});