console.log("teste");
let closeButton = document.querySelector(".removeFolder_content_buttons-button");
let deleteFolderWindow = document.querySelector(".removeFolder")
closeButton =document.querySelector(".removeFolder_content_buttons-button").addEventListener("click", () => {
    deleteFolderWindow.classList.toggle("invisible")
})