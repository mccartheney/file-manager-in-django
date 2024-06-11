class welcomeComponent extends HTMLElement {
    constructor () {
        super ();

        this.shadow = this.attachShadow({mode:"open"})
        this.shadow = this.shadow.append(this.welcomeTemplate)

    }

    
    get welcomeTemplate () {
        const welcomeDiv = document.createElement("div");
        welcomeDiv.classList.add ("welcome")

        welcomeDiv.innerHTML = `
        
            <style>
                @import url("/static/css/components/landingPage/welcome.css")
            </style>

            <div class="welcome_image">
                    <img class="welcome_image-img" src=${this.getAttribute("imgSrc")} alt="">
            </div>

            <div class="welcome_textContent">
                <h1>
                    Mc Files <br>
                    The best and safest place <br>
                    For your Files
                </h1>
                <p>
                    Authentication, secure and upload and download your files. All of <br>
                    it in one app
                </p>


                <a href="/user/register">
                    <button>
                        Register
                    </button>
                </a>

            </div>

            <div class="welcome_video">
                <h1>
                    Video Here
                </h1>
            </div>

        `

        return welcomeDiv
    }
}

customElements.define("welcome-component", welcomeComponent)
