class fileComponent extends HTMLElement {
    constructor () {
        super()

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.fileComponentTemplate)
        this.iframe = document.querySelector('iframe');
        this.showFileContent = document.querySelector(".showFileContent")

    }


    getExtension (fileName) {
        // Find the last occurrence of a dot in the file name
        let lastDotIndex = fileName.lastIndexOf('.');

        // If there is no dot, return an empty string
        if (lastDotIndex === -1) {
            return '';
        }

        // Return the substring after the last dot
        return fileName.substring(lastDotIndex + 1);
    }

    connectedCallback () {
        
        let fileName = this.getAttribute("fileTitle")
        let fileExtension = this.getExtension(fileName)
        let fileLogo = this.shadow.querySelector(".file_logo")

        console.log(fileLogo);
        
        if (fileExtension == "svg" ||fileExtension == "png" || fileExtension == "jpeg" || fileExtension == "jpg") {
            fileLogo.src = this.getAttribute("fileImgSrc")
        }else if (fileExtension == "mp3") {
            fileLogo.src = this.getAttribute("fileAudioSrc")
        } else if (fileExtension == "mp4") {
            fileLogo.src = this.getAttribute("fileVideoSrc")
        } else {
            fileLogo.src = this.getAttribute("fileDocumentSrc")            
        }

        let closeWindowButton = document.querySelector(".removeFile_content_buttons-button")

        let removeButton = this.shadow.querySelector(".removeButton")
        let deleteFileWindow = document.querySelector(".removeFile")
        
        this.onclick = (event) => {
            if (deleteFileWindow) {
                if (!deleteFileWindow.classList.contains("invisible")) {
                    return
                }
            }
            
            
            document.querySelector(".showFileContent_header_download").href = this.getAttribute("fileUrl")

            this.iframe.src = this.getAttribute("fileUrl")
            const fileExtension = this.iframe.src.split('.').pop().split(/\#|\?/)[0]
            const fileVisibleExtensions = ["jpg", "png", "jpeg", "svg", "mp3", "mp4"]
            
            if (fileVisibleExtensions.includes(fileExtension)) {
                this.showFileContent.classList.remove("invisible");
            }
        }
        
        
        let closeFilePreviewButton = document.querySelector(".showFileContent_header_close")
        closeFilePreviewButton.addEventListener("click", () => {
            
            this.showFileContent.classList.add("invisible");
        })
        
        closeWindowButton.addEventListener("click" ,() => {
            document.querySelector(".removeFile").classList.add("invisible")
        })
        

        
        
        removeButton.addEventListener("click", () => {
            document.querySelector("#File_to_remove").value = this.getAttribute("fileId")
            let spanToAddFolderName = document.querySelector(".fileToRemove");
            spanToAddFolderName.textContent = this.getAttribute("fileTitle")
            deleteFileWindow.classList.toggle("invisible")
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

            <div>
            <a href = "${ this.getAttribute("fileUrl") }" onclick="return false">
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