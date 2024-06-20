class fileComponent extends HTMLElement {
    constructor () {
        super()

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.fileComponentTemplate)

    }

    connectedCallback () {
        
        let removeButton = this.shadow.querySelector(".removeButton")
        let deleteFolderWindow = document.querySelector(".removeFile")
        
        removeButton.addEventListener("click", () => {
            document.querySelector("#File_to_remove").value = this.getAttribute("fileId")
            let spanToAddFolderName = document.querySelector(".fileToRemove");
            spanToAddFolderName.textContent = this.getAttribute("fileTitle")
            deleteFolderWindow.classList.toggle("invisible")
        })


        let closeWindowButton = document.querySelector(".removeFile_content_buttons-button")
        closeWindowButton.addEventListener("click" ,() => {
            document.querySelector(".removeFile").classList.add("invisible")
        })

        this.shadow.querySelector(".file").addEventListener("mouseover", ()=> {
            removeButton.classList.remove("invisible")
        })

        this.shadow.querySelector(".file").addEventListener("mouseout", () => {
            removeButton.classList.add("invisible")
        })
    }

    get fileComponentTemplate (){
        const fileComponentDiv = document.createElement ("div")
        fileComponentDiv.classList.add("file")
        fileComponentDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/dashboard/fileManager/fileComponent.css");
            </style>

            <a href = "${ this.getAttribute("fileUrl") }" download>
                <div class="file_fileImg">
                    <img src="${this.getAttribute("fileImgSrc")}" class="file_logo"/>
                <div>
                <div class="file_fileName">
                    <p>
                        ${this.getAttribute("fileTitle")}
                    </p>
                <div>
            </a>
            <button class="removeButton invisible">
                <img src = "${this.getAttribute("deleteIcon")}"/>
            </button> 
               

        `


        return fileComponentDiv
    }
} 

customElements.define ("file-component", fileComponent)