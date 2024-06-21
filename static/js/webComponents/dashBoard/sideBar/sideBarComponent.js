class sideBarComponent extends HTMLElement {
    constructor() {
        super();

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.sideBarTemplate)
    }
    
    connectedCallback (){
        let anchors = this.shadow.querySelectorAll("a");

        anchors.forEach(anchor => {
            let anchorClass = anchor.classList[0]
            let actualPage = this.getAttribute("actualPage") 
            if (actualPage == anchorClass) {
                anchor.classList.add("activeAnchor")
            }
        });
    }
    
    get sideBarTemplate () {
        let sideBarDiv = document.createElement("div")
        sideBarDiv.classList.add("sideBar");

        sideBarDiv.innerHTML = `

            <style>
                @import url("/static/css/components/dashboard/sidebar.css")
            </style>


            <div class="sideBar_logo">
                <logo-component 
                    redirect="/dashboard" 
                    logoImgSrc="${this.getAttribute("logoImgSrc")}">
                </logo-component>
            </div>

            <nav class="sideBar_nav">
                <a href="/dashboard" class="dashboard">
                    <img src="${this.getAttribute('dashBoardImgSrc')}" />
                    Dashboard
                </a>
                <a href="/dashboard/filemanager" class="fileManager">
                    <img src="${this.getAttribute('fileManagerImgSrc')}" />
                    File Manager
                </a>
                <a href="/dashboard/folders" class="folders">
                    <img src="${this.getAttribute('foldersImgSrc')}" />
                    Folders
                </a>
                <a href="/dashboard/files" class="Files">
                    <img src="${this.getAttribute('filesImgSrc')}" />
                    Files
                </a>
            </nav>
        
        `

        return sideBarDiv
    }
}

customElements.define("sidebar-component", sideBarComponent)