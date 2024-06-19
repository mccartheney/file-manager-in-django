class headerComponent extends HTMLElement{
    constructor () {
        super()

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow.append(this.headerTemplate)

    }

    connectedCallback () {
        let userButton = this.shadow.querySelector(".header_dropdown_image");
        let options = this.shadow.querySelector(".header_dropdown_options")

        userButton.addEventListener("click", () => {
            options.classList.toggle("hidden");
        })
    }

    get headerTemplate () {
        const headerElement = document.createElement("header")

        headerElement.innerHTML = `
        
            <style>
                @import url("/static/css/components/dashboard/header.css");
            
            </style>

            <div class="header_title">
                <h2>
                    ${this.getAttribute("title")}
                </h2>
            </div>

            <div class="header_dropdown">
                <button class="header_dropdown_image">
                    <img src="${this.getAttribute("userImage")}" />
                </button>

                <div class="header_dropdown_options hidden">
                    <div class="header_dropdown_options_section">
                        <a href = "/user">
                            <button>
                                <img src="${this.getAttribute("settingIcon")}" />
                                
                                Reset Password
                            </button>
                        </a>
                    </div>

                    <div class="header_dropdown_options_section">
                        <a href="/logout">
                            <button>
                                <img src="${this.getAttribute("logOutIcon")}" />
                                Sign Out
                            </button>
                        </a>
                    </div>
                </div>
            </div>



        `
        return headerElement
    }
}

customElements.define("header-component", headerComponent)