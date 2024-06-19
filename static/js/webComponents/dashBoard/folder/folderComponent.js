class folderComponent extends HTMLElement {
    constructor() {
        super()
        
        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.folderTemplate)



    }

    connectedCallback () {
        let removeButton = this.shadow.querySelector(".removeButton")
        let deleteFolderWindow = document.querySelector(".removeFolder")

        removeButton.addEventListener("click", () => {
            document.querySelector("#folder_to_remove").value = this.getAttribute("folderId")
            let spanToAddFolderName = document.querySelector(".folderToRemove");
            spanToAddFolderName.textContent = this.getAttribute("folderTitle")
            deleteFolderWindow.classList.toggle("invisible")
        })

        let editButton = this.shadow.querySelector(".editButton")
        let closeEdit = document.querySelector(".close_folder_edit")
        let editFolderWindow = document.querySelector(".content_area_fileManagement_header_createArea_createFolder_editFolder")

        editButton.addEventListener("click", () => {
            document.querySelector("#folder_id_to_rename").value = this.getAttribute("folderId")
            editFolderWindow.classList.toggle("hidden")
        })
        
        closeEdit.addEventListener("click",() => {
            editFolderWindow.classList.add("hidden")
        })

        this.shadow.querySelector(".folder").addEventListener("mouseover",() => {
            removeButton.classList.remove("invisible")
            editButton.classList.remove("invisible")
        })

        this.shadow.querySelector(".folder").addEventListener("mouseout", () => {
            removeButton.classList.add("invisible")
            editButton.classList.add("invisible")
        })

    }

    get folderTemplate () {
        let folderDiv = document.createElement("div");
        folderDiv.classList.add("folder")

        folderDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/dashboard/fileManager/folderComponent.css");
            </style>

            <a href = "/dashboard/folders/${ this.getAttribute("folderId")}">
                <div class="folder_folderImg">
                    <img src="${this.getAttribute("folderImgSrc") }"/>
                <div>
                <div class="folder_folderName">
                    <p>
                        ${this.getAttribute("folderTitle")}
                    </p>
                <div>
            </a>
            <button class="removeButton invisible">
                <img src = "${this.getAttribute("deleteIcon")}"/>
            </button>    
            <button class="editButton invisible">
                <img src = "${this.getAttribute("editIcon")}"/>
            </button>    
        `

        return folderDiv
    }
}

customElements.define("folder-component", folderComponent)