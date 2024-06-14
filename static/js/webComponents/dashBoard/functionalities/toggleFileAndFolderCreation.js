
window.onload = () => {
    let folderCreator = document.querySelector(".content_area_fileManagement_header_createArea_createFolder");

    let typeOfCreation = document.querySelector(".content_area_fileManagement_header_createArea_dropDown_options")

    document.querySelector(".toggle_dropDown").onclick = () => {
        typeOfCreation.classList.toggle("invisible")
    }


    let folderButton = document.querySelector(".call_folderCreator");
    folderButton.addEventListener("click", () => {

        folderCreator.classList.toggle("hidden")
        typeOfCreation.classList.toggle("invisible")

    })

    let close_folder_creations = document.querySelectorAll(".close_folder_creation");
    close_folder_creations.forEach(element => {
        element.onclick = () => {
            folderCreator.classList.toggle("hidden");
        }
    });
}