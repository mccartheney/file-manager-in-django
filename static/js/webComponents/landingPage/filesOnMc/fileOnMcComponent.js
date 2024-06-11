class filesOnMcComponent extends HTMLElement {
    constructor () {
        super ();

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.filesOnMCTemplate)

    }

    get filesOnMCTemplate () {
        const filesOnMcDiv = document.createElement("div");
        filesOnMcDiv.classList.add("fileOnMc")

        filesOnMcDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/landingPage/filesOnMc.css")
            </style>

            <div class="filesOnMc_content">
                <div class="filesOnMc_content_header">
                    <h2>
                        Manage Your Files with Mc Files.
                    </h2>
                    <p>
                        Safely store and access your files from anywhere with Mc files.
                    </p>
                </div>

                <div class="filesOnMc_content_pops">
                    <div class="filesOnMc_content_pops_pop">
                        <div class="filesOnMc_content_pops_pop_img register">
                            <img src="${this.getAttribute("register")}" alt="">
                        </div>
                        <p>
                            Quickly sign up to efficiently manage and securely store your files with Mc Files
                        </p>
                    </div>
                    <div class="filesOnMc_content_pops_pop">
                        <div class="filesOnMc_content_pops_pop_img upload">
                            <img src="${this.getAttribute("upload")}" alt="">
                        </div>
                        <p>
                            Easily upload any file type.
                        </p>
                    </div>
                    <div class="filesOnMc_content_pops_pop">
                        <div class="filesOnMc_content_pops_pop_img secure">
                            <img src="${this.getAttribute("lock")}" alt="">
                        </div>
                        <p>
                            Download yours files wherever you are and when you want.
                        </p>
                    </div>
                </div>
            </div>

        `

        return filesOnMcDiv
    }
}

customElements.define("files-on-mc-component", filesOnMcComponent)