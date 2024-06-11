class logoComponent extends HTMLElement {
    constructor () {
        super ()
        
        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.logoTemplate)
    }

    get logoTemplate () {
        const logoAnchor = document.createElement("a");
        logoAnchor.href = this.getAttribute("redirect")


        logoAnchor.innerHTML = `
            <style>
                @import url("/static/css/components/logo/logo.css");
            </style>


            <div class="logo">
                <img src="${this.getAttribute("logoImgSrc")}" alt="">
                <p style="text-decoration: none;">
                    McFiles
                </p>
            </div>

        `

        return logoAnchor
    }
}

customElements.define("logo-component", logoComponent)