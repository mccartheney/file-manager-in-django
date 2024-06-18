
window.onload = () => {
    let folderCreator = document.querySelector(".content_area_fileManagement_header_createArea_createFolder");
    let fileUploader = document.querySelector(".content_area_fileManagement_header_createArea_createFolder_uploadFile")

    let typeOfCreation = document.querySelector(".content_area_fileManagement_header_createArea_dropDown_options")

    document.querySelector(".toggle_dropDown").onclick = () => {
        typeOfCreation.classList.toggle("invisible")
    }

    let fileButton = document.querySelector(".call_fileUpload")
    fileButton.addEventListener("click", () => {


        fileUploader.classList.toggle("hidden")
        typeOfCreation.classList.toggle("invisible")

    })

    let closeFileUpload = document.querySelector(".close_UploadFile_edit")
    closeFileUpload.addEventListener("click", ()=> {
        fileUploader.classList.toggle("hidden")
    })

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