class folderComponent extends HTMLElement {
    constructor() {
        super()
        
        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.folderTemplate)

    }

    get folderTemplate () {
        let folderDiv = document.createElement("div");
        folderDiv.classList.add("folder")

        folderDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/dashboard/fileManager/folderComponent.css");
            </style>

            <a href = "/dashboard/folders/${this.getAttribute("folderId")}">
                <div class="folder_folderImg">
                    <img src="${this.getAttribute("folderImgSrc") }"/>
                <div>
                <div class="folder_folderName">
                    <p>
                        ${this.getAttribute("folderTitle")}
                    </p>
                <div>
            </a>
        `

        return folderDiv
    }
}

customElements.define("folder-component", folderComponent)